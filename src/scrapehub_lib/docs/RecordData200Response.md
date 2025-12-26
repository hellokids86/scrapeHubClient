# RecordData200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 
**records_processed** | **float** |  | 
**code** | **str** |  | 
**trace_id** | **str** |  | [optional] 

## Example

```python
from scrapehub_client.models.record_data200_response import RecordData200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RecordData200Response from a JSON string
record_data200_response_instance = RecordData200Response.from_json(json)
# print the JSON string representation of the object
print(RecordData200Response.to_json())

# convert the object into a dict
record_data200_response_dict = record_data200_response_instance.to_dict()
# create an instance of RecordData200Response from a dict
record_data200_response_from_dict = RecordData200Response.from_dict(record_data200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


