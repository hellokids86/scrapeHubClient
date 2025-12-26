# UpdateProgressRequest

Progress update payload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success_count** | **int** |  | 
**error_count** | **int** |  | 
**warning_count** | **int** |  | 
**message** | **str** |  | 
**total_count** | **int** |  | 
**update_type** | [**UpdateType**](UpdateType.md) |  | 

## Example

```python
from scrapehub_client.models.update_progress_request import UpdateProgressRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateProgressRequest from a JSON string
update_progress_request_instance = UpdateProgressRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateProgressRequest.to_json())

# convert the object into a dict
update_progress_request_dict = update_progress_request_instance.to_dict()
# create an instance of UpdateProgressRequest from a dict
update_progress_request_from_dict = UpdateProgressRequest.from_dict(update_progress_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


