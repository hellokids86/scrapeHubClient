"""
ScrapeHub Robot Base Class

This class handles robot operations for ScrapeHub, using environment variables for configuration.
It serves as a base class that can be extended for specific robot implementations.

Features:
- Start a scrape session
- Update scrape progress
- Complete a scrape session
- Record scraped data
- Record errors
- Listen for new messages
- Acknowledge messages
"""

from abc import abstractmethod
import json
import os
import threading
import time
from typing import Optional, Dict, Any, List
from datetime import datetime
from dotenv import load_dotenv

# Try relative imports first (when installed as package)
# Fall back to absolute imports (when running directly)
try:
    from .KillRequestedException import KillRequestedException
    from . import ScrapeHubRunner
except ImportError:
    from KillRequestedException import KillRequestedException
    import ScrapeHubRunner

from ..scrapehub_client import ApiClient, Configuration
from ..scrapehub_client.api import (
    scraping_operations_api,
    scrape_hub_api_messaging_api,
    scrape_hub_api_api
)
from ..scrapehub_client.models import (
    UpdateProgressRequest,
    UpdateType,
    CompleteScrapeRequest,
    RecordDataRequest,
    DataRecord,
    RecordType,
    ChildProductInput,
    ParentProductInput,
    FreeDataInput,
    RecordErrorRequest,
    DefaultSelectionPrisma36ScrapeSessionErrorLogPayload,
    AckMessageRequest,
    ScraperMessageResponse
)
from typing import Union

from ..scrapehub_client.models.pick_scrape_session_error_log_exclude_keyof_scrape_session_error_log_id_or_created_at import PickScrapeSessionErrorLogExcludeKeyofScrapeSessionErrorLogIdOrCreatedAt


class ScrapeHubBase:
    """
    Base class for ScrapeHub robot implementations.
    
    This class provides all the necessary methods to interact with the ScrapeHub API,
    including scraping operations, data recording, error handling, and messaging.
    """
    isRunning = False
    killRequested = False




    def __init__(self, scraper_name: str, load_env: bool = True):
        """
        Initialize the ScrapeHub robot.
        
        Args:
            scraper_name: Name of the scraper (must exist in ScrapeHub)
            load_env: Whether to load environment variables from .env file (default: True)
        """
        if load_env:
            load_dotenv()
        
        if(scraper_name is None or scraper_name.strip() == ""):
            raise ValueError("scraper_name must be provided and cannot be empty.")


        self.scraper_name = scraper_name
        self.api_client: Optional[ApiClient] = None
        self.scraping_api: Optional[scraping_operations_api.ScrapingOperationsApi] = None
        self.messaging_api: Optional[scrape_hub_api_messaging_api.ScrapeHubAPIMessagingApi] = None
        self.hub_api: Optional[scrape_hub_api_api.ScrapeHubAPIApi] = None
        
        # Statistics
        self.success_count = 0
        self.error_count = 0
        self.warning_count = 0
        self.total_count = 0
        
        # Configuration
        self._setup_configuration()
    


    def start(self):
        self.runningThreads = [t for t in self.runningThreads if t.is_alive()]


        if( self.isRunning ):
            print("Scrape is already running.")
            return
        
        if(self.killRequested):
            print("Kill requested, not starting new scrape.")
            self.killRequested = False
            
            return

        try:
            runner = self.get_runner()
            self.runner = runner
            self.start_scrape(runner)


            print ("\nBeginning scraping process... Session ID:", runner.session_id)


            completeMessage = runner.run()
            print ("\nScraping process completed. Completing scrape...")
                # Complete the scrape
            self.complete_scrape(runner, completeMessage)

            print ("\nScrape completed, session ID:", runner.session_id)
            print ("Scrape completed successfully.")

        except KillRequestedException:
            self.isRunning = False
            print("\n✓ Scrape stopped by user request.")

        except Exception as e:
            self.isRunning = False

            print(f"Scraping failed: {e}")

            if(self.runner):
                runner = self.runner
            # Record the error
                self.record_error(runner,
                    error_type="SCRAPING_ERROR",
                    message=str(e),
                    severity="ERROR",
                    context="ScrapeHubBase.start",
                    stack_trace=str(e.__traceback__)
                )
                
                self.complete_scrape(runner,
                        completeMessage={
                            "message": f"Scrape failed: {e}",
                            "status_code": "FAILED"
                        }
                    )
                

    @abstractmethod
    def get_runner(self) -> ScrapeHubRunner:
        """
        Get a ScrapeHubRunner instance for this robot.
        
        Returns:
            ScrapeHubRunner instance
        """
        raise NotImplementedError("get_runner() must be implemented in subclasses.")
    



    def _setup_configuration(self):
        """Set up API client configuration from environment variables."""
        configuration = Configuration()
        
        api_key = os.getenv('SCRAPEHUB_API_KEY')
        
        if not api_key:
            raise ValueError(
                "Missing required environment variables: SCRAPEHUB_API_KEY \n"
                "Please set them in your .env file or environment."
            )
        
        # Set API keys using the security scheme names from the OpenAPI spec
        # These map to headers: api_key -> x-api-key, api_username -> x-api-username
        configuration.api_key['api_key'] = api_key
        configuration.host = os.getenv('SCRAPEHUB_API_HOST', 'https://scrapehub.unxplrd.com/scrapehub/api')
        
        self.api_client = ApiClient(configuration)
        self.scraping_api = scraping_operations_api.ScrapingOperationsApi(self.api_client)
        self.messaging_api = scrape_hub_api_messaging_api.ScrapeHubAPIMessagingApi(self.api_client)
        self.hub_api = scrape_hub_api_api.ScrapeHubAPIApi(self.api_client)

    def start_scrape(self, runner: ScrapeHubRunner, custom_data: Optional[Dict[str, Any]] = None) -> str:
        """
        Start a new scrape session.
        
        Args:
            custom_data: Optional custom data to pass to the scraper
            
        Returns:
            Session ID
            
        Raises:
            Exception: If the scrape session fails to start
        """
        try:
            self.isRunning = True
            self.get_scraper_profile()
            response = self.scraping_api.start_scrape(
                name=self.scraper_name,
                request_body=custom_data
            )
            # Response is wrapped in StartScrape200Response with actual_instance
            start_response = response.actual_instance
            runner.set_session_id(start_response.session_id)
            print(f"✓ Started scrape session: {runner.session_id}")
            return runner.session_id
        except Exception as e:
            print(f"✗ Failed to start scrape: {e}")
            raise
    
    def update_progress(self, runner: ScrapeHubRunner, message: str = "Processing...") -> bool:
        """
        Update the progress of the current scrape session.
        
        Args:
            message: Progress message to display
            
        Returns:
            True if successful, False otherwise
        """
        if not runner.session_id:
            raise ValueError("No active session. Call start_scrape() first.")
        
        try:
            progress_request = UpdateProgressRequest(
                success_count=self.runner.success_count,
                error_count=self.runner.error_count,
                warning_count=self.runner.warning_count,
                total_count=self.runner.total_count,
                message=message,
                update_type=UpdateType("progress")
            )
            
            self.scraping_api.update_progress(
                session_id=runner.session_id,
                update_progress_request=progress_request
            )
            print(f"✓ Updated progress for session: {runner.session_id}")
            return True
        except Exception as e:
            print(f"✗ Failed to update progress: {e}")
            return False

    def complete_scrape(self, runner: ScrapeHubRunner, completeMessage: Dict[str, str]) -> bool:
        """
        Complete the current scrape session.
        
        Args:
            completeMessage: Completion message
            status_code: One of "SUCCESS", "FAILED", "KILL_REQUEST"
            
        Returns:
            True if successful, False otherwise
        """
        if not runner.session_id:
            raise ValueError("No active session. Call start_scrape() first.")
        
        try:
            complete_request = CompleteScrapeRequest(
                success_count=self.runner.success_count,
                error_count=self.runner.error_count,
                warning_count=self.runner.warning_count,
                message=completeMessage.get("message", "Scrape completed"),
                status_code=completeMessage.get("status_code", "SUCCESS")
            )
            
            self.scraping_api.complete_scrape(
                session_id=runner.session_id,
                complete_scrape_request=complete_request
            )
            print(f"✓ Completed scrape session: {runner.session_id}")

            return True
        except Exception as e:
            print(f"✗ Failed to complete scrape: {e}")
            return False
        finally:
            self.isRunning = False
    
    def record_data(self, runner: ScrapeHubRunner, records: List[DataRecord]) -> int:
        """
        Record scraped data.
        
        Args:
            records: List of data records to save
            
        Returns:
            Number of records processed
        """

        # print the records being sent


        # print(f"Recording data: {records}")

        # print the records in json
        
     

        if not runner.session_id:
            raise ValueError("No active session. Call start_scrape() first.")
        
        try:
            data_request = RecordDataRequest(
                session_id=runner.session_id,
                records=records
            )

            # print(f"Recording data (JSON): {json.dumps(data_request.model_dump(by_alias=True), default=str, indent=2)}")
            
            response = self.scraping_api.record_data(record_data_request=data_request)
            record_data_response = response.actual_instance
            return record_data_response.records_processed
        except Exception as e:
            print(f"✗ Failed to record data: {e}")
            raise
    
    def record_child_products(self, runner: ScrapeHubRunner, products: List[ChildProductInput]) -> int:
        """
        Record one or more child products in a single request.
        
        Args:
            products: Single ChildProductInput or list of ChildProductInput objects
            
        Returns:
            Number of records processed
            
        Example:
            # Single product
            product = ChildProductInput(
                scrape_session_id=robot.session_id,
                key="PROD-1",
                sku="SKU-1",
                brand="Brand A",
                cost=10.00
            )
            robot.record_child_products([product])
            
            # Multiple products
            products = [
                ChildProductInput(scrape_session_id=robot.session_id, key="PROD-1", sku="SKU-1"),
                ChildProductInput(scrape_session_id=robot.session_id, key="PROD-2", sku="SKU-2")
            ]
            robot.record_child_products(products)
        """
        # Convert single product to list
        if isinstance(products, ChildProductInput):
            products = [products]
        
        records = []
        for product in products:
            record = DataRecord(
                record_type=RecordType("CHILD_PRODUCT"),
                version="1.0",
                child_product=product
            )
            records.append(record)
        
        return self.record_data(runner, records)
    
    def record_parent_products(self, runner: ScrapeHubRunner, products: Union[ParentProductInput, List[ParentProductInput]]) -> int:
        """
        Record one or more parent products in a single request.
        
        Args:
            products: Single ParentProductInput or list of ParentProductInput objects
            
        Returns:
            Number of records processed
            
        Example:
            # Single product
            product = ParentProductInput(
                scrape_session_id=robot.session_id,
                key="PARENT-1",
                brand="Brand A",
                title="Product Collection",
                description="A great collection"
            )
            robot.record_parent_products(product)
            
            # Multiple products
            products = [
                ParentProductInput(scrape_session_id=robot.session_id, key="PARENT-1", title="Collection 1"),
                ParentProductInput(scrape_session_id=robot.session_id, key="PARENT-2", title="Collection 2")
            ]
            robot.record_parent_products(products)
        """
        # Convert single product to list
        if isinstance(products, ParentProductInput):
            products = [products]
        
        records = []
        for product in products:
            record = DataRecord(
                record_type=RecordType("PARENT_PRODUCT"),
                version="1.0",
                parent_product=product
            )
            records.append(record)
        
        return self.record_data(runner, records)
    
    def record_free_data_items(self, runner: ScrapeHubRunner, items: Union[FreeDataInput, List[FreeDataInput]]) -> int:
        """
        Record one or more free-form data items in a single request.
        
        Args:
            items: Single FreeDataInput or list of FreeDataInput objects
            
        Returns:
            Number of records processed
            
        Example:
            # Single item
            item = FreeDataInput(
                scrape_session_id=robot.session_id,
                key="DATA-1",
                key_name="Custom Data",
                data='{"custom": "value"}'
            )
            robot.record_free_data_items(item)
            
            # Multiple items
            items = [
                FreeDataInput(scrape_session_id=robot.session_id, key="DATA-1", data='{"a": 1}'),
                FreeDataInput(scrape_session_id=robot.session_id, key="DATA-2", data='{"b": 2}')
            ]
            robot.record_free_data_items(items)
        """
        # Convert single item to list
        if isinstance(items, FreeDataInput):
            items = [items]
        
        records = []
        for item in items:
            record = DataRecord(
                record_type=RecordType("FREE_DATA"),
                version="1.0",
                free_data=item
            )
            records.append(record)
        
        return self.record_data(runner, records)
    
    def record_error(self, runner: ScrapeHubRunner, error_type: str, message:str, context: str, severity: str = "ERROR", 
                    details: str = "", stack_trace: str = "") -> bool:
        """
        Record an error during scraping.
        
        Args:
            error_type: Type of error (e.g., "NETWORK_ERROR", "PARSE_ERROR")
            message: Error message
            severity: One of "ERROR", "WARNING", "CRITICAL"
            details: Additional error details
            stack_trace: Stack trace if available
            
        Returns:
            True if successful, False otherwise
        """
        if not runner.session_id:
            raise ValueError("No active session. Call start_scrape() first.")

        if error_type == "KILL_REQUEST":
            return True

        print (f"Recording error: session {runner.session_id} - {error_type}  - Severity: {severity}")
        try:
            error_log = PickScrapeSessionErrorLogExcludeKeyofScrapeSessionErrorLogIdOrCreatedAt(
                session_id=runner.session_id,
                error_type=error_type,
                severity=severity,
                message=message,
                context=context,
                details=details ,
                stack_trace=stack_trace
            )
            
            error_request = RecordErrorRequest(error=error_log)
            
            response = self.scraping_api.record_error(
                record_error_request=error_request
            )

            print ("✓ Recorded error, id:", response.actual_instance.data.id)
            
            
            return True
        except Exception as e:
            print(f"✗ Failed to record error: {e}")
            return False
    
    def get_messages(self) -> List[ScraperMessageResponse]:
        """
        Get all unacknowledged messages for this scraper.
        
        Returns:
            List of message objects
        """
        try:
            response = self.messaging_api.get_messages(scraper_name=self.scraper_name).actual_instance
            if( response.messages is None ):
                return []  
            return response.messages
        except Exception as e:
            print(f"✗ Failed to get messages: {e}")
            return []
    
    def acknowledge_message(self, message_id: str) -> bool:
        """
        Acknowledge a message.
        
        Args:
            message_id: ID of the message to acknowledge
            
        Returns:
            True if successful, False otherwise
        """
        try:
            ack_request = AckMessageRequest(message_id=message_id)
            self.messaging_api.ack_message(ack_message_request=ack_request)
            return True
        except Exception as e:
            print(f"✗ Failed to acknowledge message: {e}")
            return False

    def checkIfKillRequested(self, runner):
        """
        Check if a kill request has been received.
        """
        if self.killRequested:
            self.complete_scrape(runner, completeMessage={
                "message": "Scrape killed by request.",
                "status_code": "KILL_REQUEST"
            })
            self.killRequested = False
            raise KillRequestedException(runner)



    runningThreads = []

    def process_message(self, message: ScraperMessageResponse) -> bool:
        """
        Process a single message. Override this method in subclasses.
        
        Args:
            message: Message object to process
        Returns:
            True if processed successfully, False otherwise
        """
        print(f"Processing message: {message.scraper_name} - {message.id} - {message.message_type}")

        if(message.message_type == "KILL_REQUEST"):
            print("Kill request received. Stopping scrape.")
            self.killRequested = True
            if self.isRunning:
                print("Scrape is currently running. It will be stopped after the current operation.")
            else:
                print("No scrape is currently running.")
            return True
        
        if(message.message_type == "START"):
            print("Start request received. Starting scrape if not already running.")
            if not self.isRunning:
                # do this in a new thread so we don't block processing messages
                thread = threading.Thread(target=self.start)
                thread.start()
                self.runningThreads.append(thread)
                # TODO remove threads that have finished

                
            else:
                print("Scrape is already running.")
            return True

        if(message.message_type == "KILL_REQUEST"):
            print("Kill request received. Stopping scrape.")
            self.killRequested = True
            if self.isRunning:
                print("Scrape is currently running. It will be stopped after the current operation.")
            else:
                print("No scrape is currently running.")
            return True

        # Default implementation does nothing
        return True

    
    def listen_for_messages(self, poll_interval: int = 30, max_iterations: Optional[int] = None):
        """
        Listen for new messages and process them with a callback.
        
        Args:
            callback: Function to call with each message (receives message object)
            poll_interval: Seconds between polls (default: 30)
            max_iterations: Max number of polls (None = infinite)
        """
        iterations = 0
        
        try:
            while max_iterations is None or iterations < max_iterations:
                messages = self.get_messages()
                if not messages:
                    self.runningThreads = [t for t in self.runningThreads if t.is_alive()]
                    print(f"No new messages {time.strftime('%Y-%m-%d %H:%M:%S')}. Active threads: {len(self.runningThreads)}")
                else:
                    for message in messages:
                        try:
                            if message:
                                self.acknowledge_message(message.id)

                            # Call the process_message
                            self.process_message(message)
                            
                            
                            
                        except Exception as e:
                            print(f"✗ Error processing message {message.id}: {e}")
                
                iterations += 1
                
                if max_iterations is None or iterations < max_iterations:
                    time.sleep(poll_interval)
        
        except KeyboardInterrupt:
            print("\nStopped listening for messages.")
    
    def run_cli(self):
        """
        Run the scraper with command line arguments or interactive menu.
        """
        import argparse
        
        parser = argparse.ArgumentParser(description=f"Run the {self.scraper_name} scraper.")
        parser.add_argument("--start", action="store_true", help="Run the scraper immediately once")
        parser.add_argument("--listen", action="store_true", help="Listen for messages (default 10s interval)")
        
        args = parser.parse_args()
        
        if args.start:
            self.start()
        elif args.listen:
            self.listen_for_messages(10)
        else:
            # Interactive menu
            while True:
                print(f"\n--- {self.scraper_name} Scraper Menu ---")
                print("1. Start Scraper (Run Once)")
                print("2. Listen for Messages")
                print("3. Exit")
                
                choice = input("Enter choice (1-3): ").strip()
                
                if choice == "1":
                    self.start()
                    break
                elif choice == "2":
                    try:
                        self.listen_for_messages(10)
                    except KeyboardInterrupt:
                        print("\nStopped listening.")
                    break
                elif choice == "3":
                    print("Exiting.")
                    break
                else:
                    print("Invalid choice. Please try again.")

    def get_scraper_profile(self) -> Optional[Any]:
        """
        Get the profile for this scraper.
        
        Returns:
            Scraper profile object or None if error
        """
        try:
            response = self.hub_api.get_scraper_profile(name=self.scraper_name)
            # Response is wrapped in GetScraperProfile200Response with actual_instance
            profile_response = response.actual_instance
            self.profile = profile_response.data
            print(f"Scraper Type: {self.profile.description}")
            print(f"Description: {self.profile.name}")
            return self.profile
        except Exception as e:
            print(f"✗ Failed to get scraper profile: {e}")
            raise
    
    def __enter__(self):
        """Context manager entry."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit - complete the scrape if active."""
        if self.runner.session_id:
            if exc_type is not None:
                # Exception occurred, mark as failed
                self.complete_scrape(self.runner,
                    message=f"Scrape failed: {exc_val}",
                    status_code="FAILED"
                )
            # If no exception and session still active, let user handle completion
        
        if self.api_client:
            self.api_client.close()
