# FreeDataInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scrape_session_id** | **str** |  | 
**key** | **str** |  | 
**key_name** | **str** |  | [optional] 
**metafields** | **str** |  | [optional] 
**data** | **str** |  | [optional] 

## Example

```python
from scrapehub_client.models.free_data_input import FreeDataInput

# TODO update the JSON string below
json = "{}"
# create an instance of FreeDataInput from a JSON string
free_data_input_instance = FreeDataInput.from_json(json)
# print the JSON string representation of the object
print(FreeDataInput.to_json())

# convert the object into a dict
free_data_input_dict = free_data_input_instance.to_dict()
# create an instance of FreeDataInput from a dict
free_data_input_from_dict = FreeDataInput.from_dict(free_data_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


