# StartScrape200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 
**session_id** | **str** |  | 
**code** | **str** |  | 
**trace_id** | **str** |  | [optional] 

## Example

```python
from scrapehub_client.models.start_scrape200_response import StartScrape200Response

# TODO update the JSON string below
json = "{}"
# create an instance of StartScrape200Response from a JSON string
start_scrape200_response_instance = StartScrape200Response.from_json(json)
# print the JSON string representation of the object
print(StartScrape200Response.to_json())

# convert the object into a dict
start_scrape200_response_dict = start_scrape200_response_instance.to_dict()
# create an instance of StartScrape200Response from a dict
start_scrape200_response_from_dict = StartScrape200Response.from_dict(start_scrape200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


