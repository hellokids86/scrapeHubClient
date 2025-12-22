"""
ScrapeHub Python Robot

A Python framework for building web scrapers that integrate with the ScrapeHub API.
"""

from .ScrapeHubBase import ScrapeHubBase
from .ScrapeHubRunner import ScrapeHubRunner
from .CompleteScrapeInput import CompleteScrapeInput
from .KillRequestedException import KillRequestedException
__version__ = "1.0.0"

__all__ = [
    "ScrapeHubBase",
    "ScrapeHubRunner",
    "CompleteScrapeInput",
    "KillRequestedException",
]
