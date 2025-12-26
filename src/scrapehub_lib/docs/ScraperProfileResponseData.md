# ScraperProfileResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**publish_inventory** | **bool** |  | 
**cron** | **str** |  | [optional] 
**assigned_to** | **List[str]** |  | [optional] 
**settings** | **Dict[str, object]** | Construct a type with a set of properties K of type T | [optional] 
**password** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**notes** | **str** |  | [optional] 
**disabled_date** | **str** |  | [optional] 
**is_disabled** | **bool** |  | 
**type** | **str** |  | 
**description** | **str** |  | [optional] 
**name** | **str** |  | 

## Example

```python
from scrapehub_client.models.scraper_profile_response_data import ScraperProfileResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ScraperProfileResponseData from a JSON string
scraper_profile_response_data_instance = ScraperProfileResponseData.from_json(json)
# print the JSON string representation of the object
print(ScraperProfileResponseData.to_json())

# convert the object into a dict
scraper_profile_response_data_dict = scraper_profile_response_data_instance.to_dict()
# create an instance of ScraperProfileResponseData from a dict
scraper_profile_response_data_from_dict = ScraperProfileResponseData.from_dict(scraper_profile_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


