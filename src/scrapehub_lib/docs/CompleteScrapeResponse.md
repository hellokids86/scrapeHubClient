# CompleteScrapeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | [optional] 
**session_id** | **str** |  | 

## Example

```python
from scrapehub_client.models.complete_scrape_response import CompleteScrapeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CompleteScrapeResponse from a JSON string
complete_scrape_response_instance = CompleteScrapeResponse.from_json(json)
# print the JSON string representation of the object
print(CompleteScrapeResponse.to_json())

# convert the object into a dict
complete_scrape_response_dict = complete_scrape_response_instance.to_dict()
# create an instance of CompleteScrapeResponse from a dict
complete_scrape_response_from_dict = CompleteScrapeResponse.from_dict(complete_scrape_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


