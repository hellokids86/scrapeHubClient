# ChildProductInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scrape_session_id** | **str** |  | 
**sku** | **str** |  | [optional] 
**parent_sku** | **str** |  | [optional] 
**barcode** | **str** |  | [optional] 
**key** | **str** |  | 
**key_name** | **str** |  | 
**brand** | **str** |  | [optional] 
**vendor** | **str** |  | [optional] 
**style** | **str** |  | [optional] 
**color** | **str** |  | [optional] 
**colorcode** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**material** | **str** |  | [optional] 
**size1** | **str** |  | [optional] 
**size2** | **str** |  | [optional] 
**available_date** | **datetime** |  | [optional] 
**cost** | **float** |  | [optional] 
**msrp** | **float** |  | [optional] 
**map_price** | **float** |  | [optional] 
**is_closeout** | **bool** |  | [optional] 
**images** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**metafields** | **str** |  | [optional] 
**data** | **str** |  | [optional] 

## Example

```python
from scrapehub_client.models.child_product_input import ChildProductInput

# TODO update the JSON string below
json = "{}"
# create an instance of ChildProductInput from a JSON string
child_product_input_instance = ChildProductInput.from_json(json)
# print the JSON string representation of the object
print(ChildProductInput.to_json())

# convert the object into a dict
child_product_input_dict = child_product_input_instance.to_dict()
# create an instance of ChildProductInput from a dict
child_product_input_from_dict = ChildProductInput.from_dict(child_product_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


