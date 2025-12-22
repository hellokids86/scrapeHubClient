import sys
import os
# Add the project root to the path so we can import the scrapehubpyrobot module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

import json
import time
import requests
from scrapehubpyrobot.scrapehub.CompleteScrapeInput import CompleteScrapeInput
from scrapehubpyrobot.scrapehub.ScrapeHubBase import ScrapeHubBase
from scrapehubpyrobot.scrapehub.ScrapeHubRunner import ScrapeHubRunner

scraperName = "ccs"

class CcsShoesScraper(ScrapeHubBase):
    def __init__(self):
        super().__init__(scraperName)

    def get_runner(self):
        return CcsShoesRunner(self)

class CcsShoesRunner(ScrapeHubRunner):
    def run(self) -> CompleteScrapeInput:
        print(f"Running {scraperName} scraping logic...")
        
        base_url = "https://shop.ccs.com/collections/shoe-style-skate-shoes/products.json"
        page = 1
        has_more_pages = True
        limit = 250 # Shopify standard max limit is usually 250
        
        self.success_count = 0
        self.error_count = 0
        self.warning_count = 0
        self.total_count = 0 
        
        self.hub.update_progress(self, "Starting scrape via JSON API...")

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }

        while has_more_pages:
            url = f"{base_url}?page={page}&limit={limit}"
            print(f"Scraping page {page}: {url}")
            
            try:
                # Check for kill request
                self.hub.checkIfKillRequested(self)
                
                response = requests.get(url, headers=headers)
                
                if response.status_code != 200:
                    print(f"Failed to fetch page {page}: {response.status_code}")
                    self.hub.record_error(self, "NETWORK_ERROR", f"Failed to fetch page {page}", str(response.status_code))
                    break
                
                data = response.json()
                products = data.get('products', [])
                
                if not products:
                    print(f"No more products found on page {page}. Ending pagination.")
                    has_more_pages = False
                    break
                
                print(f"Found {len(products)} products on page {page}.")
                
                for product in products:
                    try:
                        self.hub.checkIfKillRequested(self)
                        self.process_product_data(product)
                    except Exception as e:
                        print(f"Error processing product on page {page}: {e}")
                        self.error_count += 1
                        self.hub.record_error(self, "PRODUCT_ERROR", f"Error processing product {product.get('id')}", "Processing Loop", details=str(e))
                
                self.hub.update_progress(self, f"Completed page {page}. Success: {self.success_count}")
                page += 1
                time.sleep(1) # Be polite
                
            except Exception as e:
                print(f"Error scraping page {page}: {e}")
                self.hub.record_error(self, "PAGE_ERROR", f"Error scraping page {page}", "Page Loop", details=str(e))
                has_more_pages = False
        
        return CompleteScrapeInput(
            message=f"Scrape completed. Processed {self.success_count} items.",
            status_code="SUCCESS"
        )
    
    def process_product_data(self, product_data):
        product_title = product_data.get('title')
        product_vendor = product_data.get('vendor')
        product_type = product_data.get('product_type')
        product_handle = product_data.get('handle')
        product_id = product_data.get('id')
        
        # Construct URL from handle
        url = f"https://shop.ccs.com/collections/shoe-style-skate-shoes/products/{product_handle}"

        variants = product_data.get('variants', [])
        options = product_data.get('options', [])
        
        child_products = []
        
        for variant in variants:
            # Variant info
            variant_sku = variant.get('sku')
            variant_id = variant.get('id')
            variant_title = variant.get('title') # e.g. "Size 9"
            
            # Price is string in JSON, needs float conversion
            variant_price = float(variant.get('price', 0))
            
            variant_compare_at_price = variant.get('compare_at_price')
            if variant_compare_at_price:
                 variant_compare_at_price = float(variant_compare_at_price)
            else:
                 variant_compare_at_price = variant_price
            
            variant_available = variant.get('available', False)
            variant_barcode = variant.get('barcode', '') # Usually usually populated in JSON
            
            # Extract color and size from options
            color = ""
            size = ""
            
            # Map optionX to option name
            # options: [{"name": "Size", "values": [...]}, {"name": "Color", ...}]
            # variant: {"option1": "9.5", "option2": "Blue", ...}
            
            for i, opt in enumerate(options):
                opt_name = opt.get('name', '').lower()
                opt_val = variant.get(f'option{i+1}')
                
                if 'color' in opt_name:
                    color = opt_val
                elif 'size' in opt_name:
                    size = opt_val
                
                # If size not found in options but variant title looks like a size, use it
                if not size and 'title' not in opt_name and opt_val == variant_title:
                     # Fallback logic
                     pass

            if not size and len(options) == 1 and options[0]['name'] == 'Size':
                 size = variant.get('option1')
            
            if not size:
                size = variant_title # Default fallback

            child_item = {
                "scrape_session_id": self.session_id,
                "key": f"{product_id}-{variant_id}",
                "sku": variant_sku,
                "brand": product_vendor,
                "title": f"{product_title} - {variant_title}",
                "color": color, 
                "size1": size, 
                "cost": variant_price, 
                "msrp": variant_compare_at_price,
                "url": url,
                "parent_sku": str(product_id), 
                "metafields": json.dumps({
                    "upc": variant_barcode,
                    "available": variant_available,
                    "product_type": product_type
                })
            }
            
            child_products.append(child_item)

        if child_products:
            self.hub.record_child_products(self, child_products)
            self.success_count += len(child_products)
            # print(f"Recorded {len(child_products)} variants for {product_title}")

def main():
    scraper = CcsShoesScraper()
    scraper.run_cli()

if __name__ == "__main__":
    main()
