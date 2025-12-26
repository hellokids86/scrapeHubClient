# ScraperProfileResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | [optional] 
**data** | [**ScraperProfileResponseData**](ScraperProfileResponseData.md) |  | 

## Example

```python
from scrapehub_client.models.scraper_profile_response import ScraperProfileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ScraperProfileResponse from a JSON string
scraper_profile_response_instance = ScraperProfileResponse.from_json(json)
# print the JSON string representation of the object
print(ScraperProfileResponse.to_json())

# convert the object into a dict
scraper_profile_response_dict = scraper_profile_response_instance.to_dict()
# create an instance of ScraperProfileResponse from a dict
scraper_profile_response_from_dict = ScraperProfileResponse.from_dict(scraper_profile_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


