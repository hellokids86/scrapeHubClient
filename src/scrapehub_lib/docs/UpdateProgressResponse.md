# UpdateProgressResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | [optional] 
**session_id** | **str** |  | 
**scrape_session_update_id** | **str** |  | [optional] 

## Example

```python
from scrapehub_client.models.update_progress_response import UpdateProgressResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateProgressResponse from a JSON string
update_progress_response_instance = UpdateProgressResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateProgressResponse.to_json())

# convert the object into a dict
update_progress_response_dict = update_progress_response_instance.to_dict()
# create an instance of UpdateProgressResponse from a dict
update_progress_response_from_dict = UpdateProgressResponse.from_dict(update_progress_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


