# CompleteScrapeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success_count** | **int** |  | 
**error_count** | **int** |  | 
**warning_count** | **int** |  | 
**message** | **str** |  | [optional] 
**status_code** | **str** |  | 

## Example

```python
from scrapehub_client.models.complete_scrape_request import CompleteScrapeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CompleteScrapeRequest from a JSON string
complete_scrape_request_instance = CompleteScrapeRequest.from_json(json)
# print the JSON string representation of the object
print(CompleteScrapeRequest.to_json())

# convert the object into a dict
complete_scrape_request_dict = complete_scrape_request_instance.to_dict()
# create an instance of CompleteScrapeRequest from a dict
complete_scrape_request_from_dict = CompleteScrapeRequest.from_dict(complete_scrape_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


