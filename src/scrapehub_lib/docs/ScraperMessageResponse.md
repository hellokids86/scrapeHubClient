# ScraperMessageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**scraper_id** | **str** |  | 
**scraper_name** | **str** |  | 
**message_type** | [**MessageType**](MessageType.md) |  | 
**message** | **str** |  | [optional] 
**created_at** | **str** |  | 
**expires_at** | **str** |  | [optional] 

## Example

```python
from scrapehub_client.models.scraper_message_response import ScraperMessageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ScraperMessageResponse from a JSON string
scraper_message_response_instance = ScraperMessageResponse.from_json(json)
# print the JSON string representation of the object
print(ScraperMessageResponse.to_json())

# convert the object into a dict
scraper_message_response_dict = scraper_message_response_instance.to_dict()
# create an instance of ScraperMessageResponse from a dict
scraper_message_response_from_dict = ScraperMessageResponse.from_dict(scraper_message_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


