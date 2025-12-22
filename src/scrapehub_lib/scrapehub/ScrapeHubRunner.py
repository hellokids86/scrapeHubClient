






from abc import abstractmethod
from typing import TYPE_CHECKING

# Try relative imports first (when installed as package)
# Fall back to absolute imports (when running directly)
try:
    from .CompleteScrapeInput import CompleteScrapeInput
except ImportError:
    from CompleteScrapeInput import CompleteScrapeInput

if TYPE_CHECKING:
    try:
        from .ScrapeHubBase import ScrapeHubBase
    except ImportError:
        from ScrapeHubBase import ScrapeHubBase


class ScrapeHubRunner:
    def __init__(self, hub: "ScrapeHubBase"):
        self.hub = hub
        self.success_count = 0
        self.error_count = 0
        self.warning_count = 0
        self.total_count = 0
    
    def set_session_id(self, session_id: str):
        self.session_id = session_id
        

    @abstractmethod
    def run(self) -> CompleteScrapeInput:
        """
        Main scraping logic - override this in your implementation.
        This should do the following: 
        1. Call update_progress() periodically to report progress.
        2. Call record_data() to save scraped items.
        3. Call record_error() to log any errors encountered.
        
        
        session_id: str
            The session ID for the current scrape.

        

        Returns:
            CompleteScrapeInput with completion info (message and status_code)
        """

        raise NotImplementedError("Override this method in your subclass to implement scraping logic.")
        
        