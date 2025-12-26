# RecordErrorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | [optional] 
**data** | [**DefaultSelectionPrisma36ScrapeSessionErrorLogPayload**](DefaultSelectionPrisma36ScrapeSessionErrorLogPayload.md) |  | 

## Example

```python
from scrapehub_client.models.record_error_response import RecordErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RecordErrorResponse from a JSON string
record_error_response_instance = RecordErrorResponse.from_json(json)
# print the JSON string representation of the object
print(RecordErrorResponse.to_json())

# convert the object into a dict
record_error_response_dict = record_error_response_instance.to_dict()
# create an instance of RecordErrorResponse from a dict
record_error_response_from_dict = RecordErrorResponse.from_dict(record_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


