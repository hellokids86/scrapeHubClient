import sys
import os
# Add the project root to the path so we can import the scrapehubpyrobot module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

import json
import time
from src.scrapehub_lib.scrapehub import CompleteScrapeInput, ScrapeHubBase, ScrapeHubRunner

scraperName = "Example"

class MyScraperHub(ScrapeHubBase):
    def __init__(self):
        super().__init__(scraperName)  # Use your scraper name from ScrapeHub

    def get_runner(self):
        return MyScraperRunner(self)

class MyScraperRunner(ScrapeHubRunner):
     def run(self) -> CompleteScrapeInput:
        
        print(f"Running {scraperName} scraping logic...")
        time.sleep(1)  # Simulate some work being done


        # remember to update the total, success, warning, and error counts as you go
        self.success_count = 0
        self.warning_count = 0
        self.error_count = 0

        # leave this at 0 if you don't know the total upfront. or update as you know more about the total count. This is used to process tracking.
        self.total_count = 10
        self.hub.update_progress(self, "Starting")
        time.sleep(5)  # Simulate some work being done

        print("\nScraping products...")

        # Every so often, check for kill requests, this throws a kill exception if requested. Do this on the within loops or long operations
        self.hub.checkIfKillRequested(self)

        example_child_products = [
            {
                "scrape_session_id": self.session_id,
                "key": "PRODUCT-001",
                "sku": "SKU-001",
                "brand": "Example Brand",
                "title": "Example Product 1",
                "color": "Blue",
                "size1": "Large",
                "cost": 25.00,
                "msrp": 49.99,
                "url": "https://example.com/product/001",
                "parent_sku": "COLLECTION-SKU-001"
            },
            {
                "scrape_session_id": self.session_id,
                "key": "PRODUCT-002",
                "sku": "SKU-002",
                "brand": "Example Brand",
                "title": "Example Product 2",
                "color": "Red",
                "size1": "Medium",
                "cost": 30.00,
                "msrp": 59.99,
                "url": "https://example.com/product/002",
                "parent_sku": "COLLECTION-SKU-001",
            "metafields": json.dumps({"data_type": "application/json", "description": "Metadata about the scrape run"})
            }
        ]

        # Set total count for progress tracking
        self.total_count = len(example_child_products)

        # Record a parent product (collection)
        self.hub.record_parent_products(self, [{
            "scrape_session_id": self.session_id,
            "parent_sku": "COLLECTION-SKU-001",
            "brand": "Example Brand",
            "title": "Summer Collection 2025",
            "description": "Our latest summer products",
            "category": "Apparel",
            "url": "https://example.com/collection",
            "metafields": json.dumps({"data_type": "application/json", "description": "Metadata about the scrape run"})
        }])
        print("✓ Recorded parent product")

        time.sleep(5)  # Simulate some work being done

        self.success_count += 1


        self.hub.checkIfKillRequested(self)


        self.hub.update_progress(self, "Recorded parent product.")
        # Record child products
        self.hub.record_child_products(self, example_child_products)
        print ("✓ Recorded child products")
        self.success_count += len(example_child_products)

        time.sleep(5)  # Simulate some work being done
        self.hub.checkIfKillRequested(self)


        self.hub.update_progress(self, "Recorded child products.")

        # Record some custom data
        custom_data = {
            "scrape_date": "2025-11-11",
            "total_products_found": len(example_child_products),
            "categories": ["Apparel", "Summer"],
            "notes": "Example scrape run"
        }
        
        self.hub.record_free_data_items(self, [{
            "scrape_session_id": self.session_id,
            "key": "SCRAPE-METADATA",
            "key_name": "Scrape Metadata",
            "data": json.dumps(custom_data),
            "metafields": json.dumps({"data_type": "application/json", "description": "Metadata about the scrape run"})
        }])
        
        time.sleep(5)  # Simulate some work being done
        self.hub.checkIfKillRequested(self)


        self.hub.update_progress(self, "Recorded custom metadata.")



        self.success_count += len(example_child_products)

        print("✓ Recorded custom metadata")

        self.hub.update_progress(self, "Completing.")

        time.sleep(5)  # Simulate some work being done
        self.hub.checkIfKillRequested(self)

        # simulate logging an error
        self.hub.record_error(
            self,
            error_type="SCRAPE_ERROR",
            context="An error occurred while scraping Example.",
            severity="ERROR",
            message="An error occurred while scraping Example.",
            details="Stack trace or additional details here.",
            stack_trace="Traceback (most recent call last): ..."
        )



        # Return completion info
        return CompleteScrapeInput(
            message="Example scrape completed successfully.",
            status_code="SUCCESS"
        )


def main():
    scraper = MyScraperHub()
    
    scraper.run_cli()



if __name__ == "__main__":
    main() 
