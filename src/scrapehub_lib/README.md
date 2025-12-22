# ScrapeHub Python Robot

A Python framework for building web scrapers that integrate with the ScrapeHub API. This package provides base classes and utilities to create robust, scalable scraping robots with built-in progress tracking, error handling, and message processing.

## Overview

ScrapeHub Python Robot consists of two main components:

- **ScrapeHubBase**: Manages API communication, session lifecycle, and data recording
- **ScrapeHubRunner**: Contains your custom scraping logic

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Access to a ScrapeHub API instance

### Install from Repository

**Option 1: Install directly from Git** (recommended)
```bash
pip install git+https://bitbucket.org/hellokids/scrapehubpyrobot.git
```

**Option 2: Clone and install locally**
```bash
# Clone the repository
git clone https://bitbucket.org/hellokids/scrapehubpyrobot.git
cd scrapehubpyrobot

# Install in editable mode (for development)
pip install -e .

# Or install normally
pip install .
```

**Option 3: Manual setup** (for development)

1. Clone the repository
   ```bash
   git clone https://bitbucket.org/hellokids/scrapehubpyrobot.git
   cd scrapehubpyrobot
   ```

2. Create a virtual environment (recommended)
   ```bash
   python -m venv .venv
   
   # Windows
   .venv\Scripts\activate
   
   # Linux/Mac
   source .venv/bin/activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

### Configure Environment Variables
   
   Copy the example environment file and add your credentials:
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and set your ScrapeHub API credentials:
   ```dotenv
   SCRAPEHUB_API_KEY=your-api-key-here
   SCRAPEHUB_API_HOST=https://scrapehub.unxplrd.com/scrapehub/api
   ```

## Creating Your First Scraper

### Step 1: Create Your Hub and Runner Class

Extend `ScrapeHubBase` and implement the `get_runner()` method:

```python


from scrapehub.CompleteScrapeInput import CompleteScrapeInput
from scrapehub.ScrapeHubBase import ScrapeHubBase
from scrapehub.ScrapeHubRunner import ScrapeHubRunner

class MyScraperHub(ScrapeHubBase):
    def __init__(self):
        super().__init__("Example")  # Use your scraper name from ScrapeHub

    def get_runner(self):
        return MyScraperRunner(self)

class MyScraperRunner(ScrapeHubRunner):
     def run(self) -> CompleteScrapeInput:
        
        # simulate updating progress
        self.hub.update_progress(self, "Starting scrape")

        # periodically check for kill requests especially in long loops
        self.hub.checkIfKillRequested(self)


        # Simulate recording a child product
        self.hub.record_child_products(self, [{
            "name": "Child Product 1",
            "price": 19.99,
            "sku": "CP001",
            "key": "CP001",
            "scrapeSessionId": self.session_id
            
        }])

               # Record a parent product (collection)
        self.hub.record_parent_products(self, [{
            "scrape_session_id": self.session_id,
            "parent_sku": "COLLECTION-SKU-001",
            "brand": "Example Brand",
            "title": "Summer Collection 2025",
            "description": "Our latest summer products",
            "category": "Apparel",
            "url": "https://example.com/collection"
        }])
        print("✓ Recorded parent product")
        self.success_count += 1
            
        # Record child products
        self.hub.record_child_products(self, example_child_products)
        print ("✓ Recorded child products")
        self.success_count += len(example_child_products)
        
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
            "data": json.dumps(custom_data)
        }])

        self.success_count += len(example_child_products)

        print("✓ Recorded custom metadata")

        self.hub.update_progress(self, "Completing.")

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

        #returns a successful completion
        return CompleteScrapeInput(
            message="Scrape completed successfully.", status_code="SUCCESS")


def main():
    scraper = MyScraperHub()
    scraper.listen_for_messages(10)
    # manually start scraper by calling start
    # scraper.start() 


if __name__ == "__main__":
    main()



```


## Key Features

### Progress Tracking

Keep ScrapeHub updated on your scraper's progress:

```python
self.hub.update_progress(self, "Processing page 5 of 10...")
```

Update counters as you work:
- `self.success_count` - Successfully processed items
- `self.error_count` - Failed items
- `self.warning_count` - Items with warnings
- `self.total_count` - Total items to process

### Recording Data

#### Child Products
```python
self.hub.record_child_products(self, [
    {
        "scrape_session_id": self.session_id,
        "key": "PRODUCT-001",
        "sku": "SKU-001",
        "brand": "Brand",
        "title": "Product Title",
        "cost": 25.00,
        "msrp": 49.99
    }
])
```

#### Parent Products
```python
self.hub.record_parent_products(self, [
    {
        "scrape_session_id": self.session_id,
        "parent_sku": "COLLECTION-001",
        "brand": "Brand",
        "title": "Collection Title"
    }
])
```

#### Free-form Data
```python
import json

self.hub.record_free_data_items(self, [
    {
        "scrape_session_id": self.session_id,
        "key": "METADATA",
        "key_name": "Scrape Metadata",
        "data": json.dumps({"custom": "data"})
    }
])
```

### Error Handling

Log errors to ScrapeHub:

```python
self.hub.record_error(
    self,
    error_type="NETWORK_ERROR",
    context="Failed to fetch page",
    severity="ERROR",  # or "WARNING", "CRITICAL"
    message="Connection timeout",
    details="Additional context here",
    stack_trace="Full stack trace..."
)
```

### Kill Request Handling

Check for kill requests from ScrapeHub (stops the scraper gracefully):

```python
# Check periodically in loops or long operations
self.hub.checkIfKillRequested(self)
```

This will raise a `KillRequestedException` which is automatically handled.

### Message Listening

Listen for messages from ScrapeHub (e.g., configuration updates, commands):

```python
# Poll for messages every 30 seconds
scraper_hub.listen_for_messages(poll_interval=30)
```

Override `process_message()` in your Hub class to handle custom messages:

```python
class MyScraperHub(ScrapeHubBase):
    def process_message(self, message):
        print(f"Received: {message.content}")
        # Handle the message
        return True
```

## Complete Example

See `scrapehub/exampleRunner.py` for a complete working example that demonstrates:
- Hub and Runner setup
- Progress tracking
- Recording products and custom data
- Error logging
- Message listening

Run it with:
```bash
python -m scrapehub.exampleRunner
```

## Project Structure

```
ScrapeHubPyRobot/
├── scrapehub/                # Main package
│   ├── ScrapeHubBase.py      # Base hub class (API management)
│   ├── ScrapeHubRunner.py    # Base runner class (scraping logic)
│   ├── CompleteScrapeInput.py # Type definition for completion status
│   ├── KillRequestedException.py # Exception for kill requests
│   └── exampleRunner.py      # Complete example implementation
├── scrapehub_client/         # Generated API client
├── .env.example              # Environment variable template
├── requirements.txt          # Python dependencies
├── setup.py                  # Package setup configuration
└── README.md                 # This file
```

## API Client

The `scrapehub_client/` directory contains an auto-generated Python client from the ScrapeHub OpenAPI specification. To regenerate the client after API updates:

```bash
# Windows PowerShell
.\regenerate-client.ps1

# Or manually
npx @openapitools/openapi-generator-cli generate -i openapi.json -g python -o .
```

## Troubleshooting

### Authentication Errors
- Verify your `SCRAPEHUB_API_KEY` is correct in `.env`
- Check that `SCRAPEHUB_API_HOST` points to the correct API endpoint

### Import Errors
- Ensure you've installed all dependencies: `pip install -r requirements.txt`
- Activate your virtual environment

### Session Errors
- Make sure your scraper name matches a scraper registered in ScrapeHub
- Check that the scraper is enabled in the ScrapeHub dashboard

## Contributing

When making changes to the scraper framework:

1. Test with the example runner first
2. Update documentation for new features
3. Ensure backward compatibility

## License

[Add your license here]

## Support

For issues or questions:
- Check the ScrapeHub API documentation
- Review `scrapehub/exampleRunner.py` for implementation patterns
- Contact your ScrapeHub administrator
