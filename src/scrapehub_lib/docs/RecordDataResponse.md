# RecordDataResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | [optional] 
**records_processed** | **float** |  | 

## Example

```python
from scrapehub_client.models.record_data_response import RecordDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RecordDataResponse from a JSON string
record_data_response_instance = RecordDataResponse.from_json(json)
# print the JSON string representation of the object
print(RecordDataResponse.to_json())

# convert the object into a dict
record_data_response_dict = record_data_response_instance.to_dict()
# create an instance of RecordDataResponse from a dict
record_data_response_from_dict = RecordDataResponse.from_dict(record_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


