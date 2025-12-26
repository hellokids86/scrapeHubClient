# CompleteScrape200Response


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
from scrapehub_client.models.complete_scrape200_response import CompleteScrape200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CompleteScrape200Response from a JSON string
complete_scrape200_response_instance = CompleteScrape200Response.from_json(json)
# print the JSON string representation of the object
print(CompleteScrape200Response.to_json())

# convert the object into a dict
complete_scrape200_response_dict = complete_scrape200_response_instance.to_dict()
# create an instance of CompleteScrape200Response from a dict
complete_scrape200_response_from_dict = CompleteScrape200Response.from_dict(complete_scrape200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


