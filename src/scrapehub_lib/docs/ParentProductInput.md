# ParentProductInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scrape_session_id** | **str** |  | 
**parent_sku** | **str** |  | 
**brand** | **str** |  | [optional] 
**vendor** | **str** |  | [optional] 
**style** | **str** |  | [optional] 
**model** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**bullets** | **str** |  | [optional] 
**category** | **str** |  | [optional] 
**sub_category** | **str** |  | [optional] 
**department** | **str** |  | [optional] 
**season** | **str** |  | [optional] 
**images** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**metafields** | **str** |  | [optional] 
**data** | **str** |  | [optional] 

## Example

```python
from scrapehub_client.models.parent_product_input import ParentProductInput

# TODO update the JSON string below
json = "{}"
# create an instance of ParentProductInput from a JSON string
parent_product_input_instance = ParentProductInput.from_json(json)
# print the JSON string representation of the object
print(ParentProductInput.to_json())

# convert the object into a dict
parent_product_input_dict = parent_product_input_instance.to_dict()
# create an instance of ParentProductInput from a dict
parent_product_input_from_dict = ParentProductInput.from_dict(parent_product_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


