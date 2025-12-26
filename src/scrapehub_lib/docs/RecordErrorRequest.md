# RecordErrorRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**PickScrapeSessionErrorLogExcludeKeyofScrapeSessionErrorLogIdOrCreatedAt**](PickScrapeSessionErrorLogExcludeKeyofScrapeSessionErrorLogIdOrCreatedAt.md) |  | 

## Example

```python
from scrapehub_client.models.record_error_request import RecordErrorRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RecordErrorRequest from a JSON string
record_error_request_instance = RecordErrorRequest.from_json(json)
# print the JSON string representation of the object
print(RecordErrorRequest.to_json())

# convert the object into a dict
record_error_request_dict = record_error_request_instance.to_dict()
# create an instance of RecordErrorRequest from a dict
record_error_request_from_dict = RecordErrorRequest.from_dict(record_error_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


