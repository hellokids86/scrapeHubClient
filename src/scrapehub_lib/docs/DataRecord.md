# DataRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**record_type** | [**RecordType**](RecordType.md) |  | 
**version** | **str** |  | 
**child_product** | [**ChildProductInput**](ChildProductInput.md) |  | [optional] 
**parent_product** | [**ParentProductInput**](ParentProductInput.md) |  | [optional] 
**free_data** | [**FreeDataInput**](FreeDataInput.md) |  | [optional] 

## Example

```python
from scrapehub_client.models.data_record import DataRecord

# TODO update the JSON string below
json = "{}"
# create an instance of DataRecord from a JSON string
data_record_instance = DataRecord.from_json(json)
# print the JSON string representation of the object
print(DataRecord.to_json())

# convert the object into a dict
data_record_dict = data_record_instance.to_dict()
# create an instance of DataRecord from a dict
data_record_from_dict = DataRecord.from_dict(data_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


