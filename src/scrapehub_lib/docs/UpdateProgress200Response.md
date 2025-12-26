# UpdateProgress200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 
**session_id** | **str** |  | 
**scrape_session_update_id** | **str** |  | [optional] 
**code** | **str** |  | 
**trace_id** | **str** |  | [optional] 

## Example

```python
from scrapehub_client.models.update_progress200_response import UpdateProgress200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateProgress200Response from a JSON string
update_progress200_response_instance = UpdateProgress200Response.from_json(json)
# print the JSON string representation of the object
print(UpdateProgress200Response.to_json())

# convert the object into a dict
update_progress200_response_dict = update_progress200_response_instance.to_dict()
# create an instance of UpdateProgress200Response from a dict
update_progress200_response_from_dict = UpdateProgress200Response.from_dict(update_progress200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


