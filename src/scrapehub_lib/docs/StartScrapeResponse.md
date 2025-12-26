# StartScrapeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | [optional] 
**session_id** | **str** |  | 

## Example

```python
from scrapehub_client.models.start_scrape_response import StartScrapeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StartScrapeResponse from a JSON string
start_scrape_response_instance = StartScrapeResponse.from_json(json)
# print the JSON string representation of the object
print(StartScrapeResponse.to_json())

# convert the object into a dict
start_scrape_response_dict = start_scrape_response_instance.to_dict()
# create an instance of StartScrapeResponse from a dict
start_scrape_response_from_dict = StartScrapeResponse.from_dict(start_scrape_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


