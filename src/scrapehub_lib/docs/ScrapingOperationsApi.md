# scrapehub_client.ScrapingOperationsApi

All URIs are relative to */scrapehub/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**complete_scrape**](ScrapingOperationsApi.md#complete_scrape) | **POST** /completeScrape/{sessionId} | 
[**record_data**](ScrapingOperationsApi.md#record_data) | **POST** /recordData | 
[**record_error**](ScrapingOperationsApi.md#record_error) | **POST** /recordError | 
[**start_scrape**](ScrapingOperationsApi.md#start_scrape) | **POST** /startScrape | 
[**update_progress**](ScrapingOperationsApi.md#update_progress) | **POST** /updateProgress/{sessionId} | 


# **complete_scrape**
> CompleteScrape200Response complete_scrape(session_id, complete_scrape_request)

Mark a scrape session as completed

### Example

* Api Key Authentication (api_key):

```python
import scrapehub_client
from scrapehub_client.models.complete_scrape200_response import CompleteScrape200Response
from scrapehub_client.models.complete_scrape_request import CompleteScrapeRequest
from scrapehub_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /scrapehub/api
# See configuration.py for a list of all supported configuration parameters.
configuration = scrapehub_client.Configuration(
    host = "/scrapehub/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with scrapehub_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scrapehub_client.ScrapingOperationsApi(api_client)
    session_id = 'session_id_example' # str | The UUID of the scrape session
    complete_scrape_request = scrapehub_client.CompleteScrapeRequest() # CompleteScrapeRequest | 

    try:
        api_response = api_instance.complete_scrape(session_id, complete_scrape_request)
        print("The response of ScrapingOperationsApi->complete_scrape:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScrapingOperationsApi->complete_scrape: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The UUID of the scrape session | 
 **complete_scrape_request** | [**CompleteScrapeRequest**](CompleteScrapeRequest.md)|  | 

### Return type

[**CompleteScrape200Response**](CompleteScrape200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **record_data**
> RecordData200Response record_data(record_data_request)

Record scraped data for a session. You can send up to 2000 records in a single request.

### Example

* Api Key Authentication (api_key):

```python
import scrapehub_client
from scrapehub_client.models.record_data200_response import RecordData200Response
from scrapehub_client.models.record_data_request import RecordDataRequest
from scrapehub_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /scrapehub/api
# See configuration.py for a list of all supported configuration parameters.
configuration = scrapehub_client.Configuration(
    host = "/scrapehub/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with scrapehub_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scrapehub_client.ScrapingOperationsApi(api_client)
    record_data_request = scrapehub_client.RecordDataRequest() # RecordDataRequest | 

    try:
        api_response = api_instance.record_data(record_data_request)
        print("The response of ScrapingOperationsApi->record_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScrapingOperationsApi->record_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **record_data_request** | [**RecordDataRequest**](RecordDataRequest.md)|  | 

### Return type

[**RecordData200Response**](RecordData200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **record_error**
> RecordError200Response record_error(record_error_request)

Record an error for a scraping session

### Example

* Api Key Authentication (api_key):

```python
import scrapehub_client
from scrapehub_client.models.record_error200_response import RecordError200Response
from scrapehub_client.models.record_error_request import RecordErrorRequest
from scrapehub_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /scrapehub/api
# See configuration.py for a list of all supported configuration parameters.
configuration = scrapehub_client.Configuration(
    host = "/scrapehub/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with scrapehub_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scrapehub_client.ScrapingOperationsApi(api_client)
    record_error_request = scrapehub_client.RecordErrorRequest() # RecordErrorRequest | 

    try:
        api_response = api_instance.record_error(record_error_request)
        print("The response of ScrapingOperationsApi->record_error:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScrapingOperationsApi->record_error: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **record_error_request** | [**RecordErrorRequest**](RecordErrorRequest.md)|  | 

### Return type

[**RecordError200Response**](RecordError200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_scrape**
> StartScrape200Response start_scrape(name, request_body=request_body)

Start a new scrape session

### Example

* Api Key Authentication (api_key):

```python
import scrapehub_client
from scrapehub_client.models.start_scrape200_response import StartScrape200Response
from scrapehub_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /scrapehub/api
# See configuration.py for a list of all supported configuration parameters.
configuration = scrapehub_client.Configuration(
    host = "/scrapehub/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with scrapehub_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scrapehub_client.ScrapingOperationsApi(api_client)
    name = 'name_example' # str | The name of the scraper to run
    request_body = None # Dict[str, object] | Free-form JSON data to pass to the scraper (optional)

    try:
        api_response = api_instance.start_scrape(name, request_body=request_body)
        print("The response of ScrapingOperationsApi->start_scrape:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScrapingOperationsApi->start_scrape: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the scraper to run | 
 **request_body** | [**Dict[str, object]**](object.md)| Free-form JSON data to pass to the scraper | [optional] 

### Return type

[**StartScrape200Response**](StartScrape200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_progress**
> UpdateProgress200Response update_progress(session_id, update_progress_request)

Update progress for a scrape session

### Example

* Api Key Authentication (api_key):

```python
import scrapehub_client
from scrapehub_client.models.update_progress200_response import UpdateProgress200Response
from scrapehub_client.models.update_progress_request import UpdateProgressRequest
from scrapehub_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /scrapehub/api
# See configuration.py for a list of all supported configuration parameters.
configuration = scrapehub_client.Configuration(
    host = "/scrapehub/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with scrapehub_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scrapehub_client.ScrapingOperationsApi(api_client)
    session_id = 'session_id_example' # str | The UUID of the scrape session
    update_progress_request = scrapehub_client.UpdateProgressRequest() # UpdateProgressRequest | 

    try:
        api_response = api_instance.update_progress(session_id, update_progress_request)
        print("The response of ScrapingOperationsApi->update_progress:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScrapingOperationsApi->update_progress: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The UUID of the scrape session | 
 **update_progress_request** | [**UpdateProgressRequest**](UpdateProgressRequest.md)|  | 

### Return type

[**UpdateProgress200Response**](UpdateProgress200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

