# RecordDataRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_id** | **str** |  | 
**records** | [**List[DataRecord]**](DataRecord.md) |  | 

## Example

```python
from scrapehub_client.models.record_data_request import RecordDataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RecordDataRequest from a JSON string
record_data_request_instance = RecordDataRequest.from_json(json)
# print the JSON string representation of the object
print(RecordDataRequest.to_json())

# convert the object into a dict
record_data_request_dict = record_data_request_instance.to_dict()
# create an instance of RecordDataRequest from a dict
record_data_request_from_dict = RecordDataRequest.from_dict(record_data_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


