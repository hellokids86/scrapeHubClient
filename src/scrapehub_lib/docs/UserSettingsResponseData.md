# UserSettingsResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scraper_assignments** | **List[str]** |  | [optional] 
**roles** | **List[str]** |  | 
**settings** | **Dict[str, object]** | Construct a type with a set of properties K of type T | [optional] 
**fullname** | **str** |  | [optional] 
**email** | **str** |  | 
**username** | **str** |  | 

## Example

```python
from scrapehub_client.models.user_settings_response_data import UserSettingsResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of UserSettingsResponseData from a JSON string
user_settings_response_data_instance = UserSettingsResponseData.from_json(json)
# print the JSON string representation of the object
print(UserSettingsResponseData.to_json())

# convert the object into a dict
user_settings_response_data_dict = user_settings_response_data_instance.to_dict()
# create an instance of UserSettingsResponseData from a dict
user_settings_response_data_from_dict = UserSettingsResponseData.from_dict(user_settings_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


