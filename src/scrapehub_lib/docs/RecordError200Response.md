# RecordError200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 
**data** | [**DefaultSelectionPrisma36ScrapeSessionErrorLogPayload**](DefaultSelectionPrisma36ScrapeSessionErrorLogPayload.md) |  | 
**code** | **str** |  | 
**trace_id** | **str** |  | [optional] 

## Example

```python
from scrapehub_client.models.record_error200_response import RecordError200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RecordError200Response from a JSON string
record_error200_response_instance = RecordError200Response.from_json(json)
# print the JSON string representation of the object
print(RecordError200Response.to_json())

# convert the object into a dict
record_error200_response_dict = record_error200_response_instance.to_dict()
# create an instance of RecordError200Response from a dict
record_error200_response_from_dict = RecordError200Response.from_dict(record_error200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


