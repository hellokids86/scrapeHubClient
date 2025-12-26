# GetUserSettings200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 
**data** | [**UserSettingsResponseData**](UserSettingsResponseData.md) |  | 
**code** | **str** |  | 
**trace_id** | **str** |  | [optional] 

## Example

```python
from scrapehub_client.models.get_user_settings200_response import GetUserSettings200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserSettings200Response from a JSON string
get_user_settings200_response_instance = GetUserSettings200Response.from_json(json)
# print the JSON string representation of the object
print(GetUserSettings200Response.to_json())

# convert the object into a dict
get_user_settings200_response_dict = get_user_settings200_response_instance.to_dict()
# create an instance of GetUserSettings200Response from a dict
get_user_settings200_response_from_dict = GetUserSettings200Response.from_dict(get_user_settings200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


