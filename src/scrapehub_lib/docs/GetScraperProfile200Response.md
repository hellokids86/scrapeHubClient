# GetScraperProfile200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 
**data** | [**ScraperProfileResponseData**](ScraperProfileResponseData.md) |  | 
**code** | **str** |  | 
**trace_id** | **str** |  | [optional] 

## Example

```python
from scrapehub_client.models.get_scraper_profile200_response import GetScraperProfile200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetScraperProfile200Response from a JSON string
get_scraper_profile200_response_instance = GetScraperProfile200Response.from_json(json)
# print the JSON string representation of the object
print(GetScraperProfile200Response.to_json())

# convert the object into a dict
get_scraper_profile200_response_dict = get_scraper_profile200_response_instance.to_dict()
# create an instance of GetScraperProfile200Response from a dict
get_scraper_profile200_response_from_dict = GetScraperProfile200Response.from_dict(get_scraper_profile200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


