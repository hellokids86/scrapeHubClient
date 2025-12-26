# AckMessageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_id** | **str** |  | 

## Example

```python
from scrapehub_client.models.ack_message_request import AckMessageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AckMessageRequest from a JSON string
ack_message_request_instance = AckMessageRequest.from_json(json)
# print the JSON string representation of the object
print(AckMessageRequest.to_json())

# convert the object into a dict
ack_message_request_dict = ack_message_request_instance.to_dict()
# create an instance of AckMessageRequest from a dict
ack_message_request_from_dict = AckMessageRequest.from_dict(ack_message_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


