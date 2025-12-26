# AckMessageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | [optional] 
**acknowledged_at** | **str** |  | 

## Example

```python
from scrapehub_client.models.ack_message_response import AckMessageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AckMessageResponse from a JSON string
ack_message_response_instance = AckMessageResponse.from_json(json)
# print the JSON string representation of the object
print(AckMessageResponse.to_json())

# convert the object into a dict
ack_message_response_dict = ack_message_response_instance.to_dict()
# create an instance of AckMessageResponse from a dict
ack_message_response_from_dict = AckMessageResponse.from_dict(ack_message_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


