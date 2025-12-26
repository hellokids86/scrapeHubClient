# AckMessage200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 
**acknowledged_at** | **str** |  | 
**code** | **str** |  | 
**trace_id** | **str** |  | [optional] 

## Example

```python
from scrapehub_client.models.ack_message200_response import AckMessage200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AckMessage200Response from a JSON string
ack_message200_response_instance = AckMessage200Response.from_json(json)
# print the JSON string representation of the object
print(AckMessage200Response.to_json())

# convert the object into a dict
ack_message200_response_dict = ack_message200_response_instance.to_dict()
# create an instance of AckMessage200Response from a dict
ack_message200_response_from_dict = AckMessage200Response.from_dict(ack_message200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


