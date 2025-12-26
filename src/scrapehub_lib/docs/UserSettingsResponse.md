# UserSettingsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | [optional] 
**data** | [**UserSettingsResponseData**](UserSettingsResponseData.md) |  | 

## Example

```python
from scrapehub_client.models.user_settings_response import UserSettingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserSettingsResponse from a JSON string
user_settings_response_instance = UserSettingsResponse.from_json(json)
# print the JSON string representation of the object
print(UserSettingsResponse.to_json())

# convert the object into a dict
user_settings_response_dict = user_settings_response_instance.to_dict()
# create an instance of UserSettingsResponse from a dict
user_settings_response_from_dict = UserSettingsResponse.from_dict(user_settings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


