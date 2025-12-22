from typing import TypedDict


class CompleteScrapeInput(TypedDict):
    """
    Interface for scrape completion data.

    Attributes:
        message: Completion message describing the scrape result
        status_code: Status of the scrape ("SUCCESS", "FAILED", or "KILL_REQUEST")
    """
    message: str
    status_code: str