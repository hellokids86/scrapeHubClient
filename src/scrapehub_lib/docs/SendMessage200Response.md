# SendMessage200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 
**message_id** | **str** |  | 
**code** | **str** |  | 
**trace_id** | **str** |  | [optional] 

## Example

```python
from scrapehub_client.models.send_message200_response import SendMessage200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SendMessage200Response from a JSON string
send_message200_response_instance = SendMessage200Response.from_json(json)
# print the JSON string representation of the object
print(SendMessage200Response.to_json())

# convert the object into a dict
send_message200_response_dict = send_message200_response_instance.to_dict()
# create an instance of SendMessage200Response from a dict
send_message200_response_from_dict = SendMessage200Response.from_dict(send_message200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


