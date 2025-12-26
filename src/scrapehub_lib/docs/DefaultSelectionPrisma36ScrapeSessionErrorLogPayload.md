# DefaultSelectionPrisma36ScrapeSessionErrorLogPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **str** |  | 
**created_at** | **datetime** |  | 
**details** | **str** |  | 
**stack_trace** | **str** |  | 
**message** | **str** |  | 
**severity** | **str** |  | 
**error_type** | **str** |  | 
**session_id** | **str** |  | 
**id** | **float** |  | 

## Example

```python
from scrapehub_client.models.default_selection_prisma36_scrape_session_error_log_payload import DefaultSelectionPrisma36ScrapeSessionErrorLogPayload

# TODO update the JSON string below
json = "{}"
# create an instance of DefaultSelectionPrisma36ScrapeSessionErrorLogPayload from a JSON string
default_selection_prisma36_scrape_session_error_log_payload_instance = DefaultSelectionPrisma36ScrapeSessionErrorLogPayload.from_json(json)
# print the JSON string representation of the object
print(DefaultSelectionPrisma36ScrapeSessionErrorLogPayload.to_json())

# convert the object into a dict
default_selection_prisma36_scrape_session_error_log_payload_dict = default_selection_prisma36_scrape_session_error_log_payload_instance.to_dict()
# create an instance of DefaultSelectionPrisma36ScrapeSessionErrorLogPayload from a dict
default_selection_prisma36_scrape_session_error_log_payload_from_dict = DefaultSelectionPrisma36ScrapeSessionErrorLogPayload.from_dict(default_selection_prisma36_scrape_session_error_log_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


