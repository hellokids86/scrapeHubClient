# GetMessagesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | [optional] 
**messages** | [**List[ScraperMessageResponse]**](ScraperMessageResponse.md) |  | 

## Example

```python
from scrapehub_client.models.get_messages_response import GetMessagesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetMessagesResponse from a JSON string
get_messages_response_instance = GetMessagesResponse.from_json(json)
# print the JSON string representation of the object
print(GetMessagesResponse.to_json())

# convert the object into a dict
get_messages_response_dict = get_messages_response_instance.to_dict()
# create an instance of GetMessagesResponse from a dict
get_messages_response_from_dict = GetMessagesResponse.from_dict(get_messages_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


