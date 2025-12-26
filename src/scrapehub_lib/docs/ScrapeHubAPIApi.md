# scrapehub_client.ScrapeHubAPIApi

All URIs are relative to */scrapehub/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_scraper_profile**](ScrapeHubAPIApi.md#get_scraper_profile) | **GET** /scraperProfile | 
[**get_user_settings**](ScrapeHubAPIApi.md#get_user_settings) | **GET** /userSettings | 
[**get_version**](ScrapeHubAPIApi.md#get_version) | **GET** /version | 


# **get_scraper_profile**
> GetScraperProfile200Response get_scraper_profile(name)

Get a scraper profile by name

### Example

* Api Key Authentication (api_key):

```python
import scrapehub_client
from scrapehub_client.models.get_scraper_profile200_response import GetScraperProfile200Response
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
    api_instance = scrapehub_client.ScrapeHubAPIApi(api_client)
    name = 'name_example' # str | The name of the scraper

    try:
        api_response = api_instance.get_scraper_profile(name)
        print("The response of ScrapeHubAPIApi->get_scraper_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScrapeHubAPIApi->get_scraper_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the scraper | 

### Return type

[**GetScraperProfile200Response**](GetScraperProfile200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_settings**
> GetUserSettings200Response get_user_settings()

Get the authenticated user's settings

### Example

* Api Key Authentication (api_key):

```python
import scrapehub_client
from scrapehub_client.models.get_user_settings200_response import GetUserSettings200Response
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
    api_instance = scrapehub_client.ScrapeHubAPIApi(api_client)

    try:
        api_response = api_instance.get_user_settings()
        print("The response of ScrapeHubAPIApi->get_user_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScrapeHubAPIApi->get_user_settings: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetUserSettings200Response**](GetUserSettings200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_version**
> VersionResponse get_version()

Get the current API version

### Example

* Api Key Authentication (api_key):

```python
import scrapehub_client
from scrapehub_client.models.version_response import VersionResponse
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
    api_instance = scrapehub_client.ScrapeHubAPIApi(api_client)

    try:
        api_response = api_instance.get_version()
        print("The response of ScrapeHubAPIApi->get_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScrapeHubAPIApi->get_version: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**VersionResponse**](VersionResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

