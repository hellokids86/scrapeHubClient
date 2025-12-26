# scrapehub_client.ScrapeHubAPIMessagingApi

All URIs are relative to */scrapehub/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ack_message**](ScrapeHubAPIMessagingApi.md#ack_message) | **POST** /ackMessage | 
[**get_messages**](ScrapeHubAPIMessagingApi.md#get_messages) | **GET** /getMessages | 
[**send_message**](ScrapeHubAPIMessagingApi.md#send_message) | **POST** /sendMessage | 


# **ack_message**
> AckMessage200Response ack_message(ack_message_request)

Acknowledge a message by its ID

### Example

* Api Key Authentication (api_key):

```python
import scrapehub_client
from scrapehub_client.models.ack_message200_response import AckMessage200Response
from scrapehub_client.models.ack_message_request import AckMessageRequest
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
    api_instance = scrapehub_client.ScrapeHubAPIMessagingApi(api_client)
    ack_message_request = scrapehub_client.AckMessageRequest() # AckMessageRequest | 

    try:
        api_response = api_instance.ack_message(ack_message_request)
        print("The response of ScrapeHubAPIMessagingApi->ack_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScrapeHubAPIMessagingApi->ack_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ack_message_request** | [**AckMessageRequest**](AckMessageRequest.md)|  | 

### Return type

[**AckMessage200Response**](AckMessage200Response.md)

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

# **get_messages**
> GetMessages200Response get_messages(scraper_name)

Get all unacknowledged and non-expired messages for the authenticated user

### Example

* Api Key Authentication (api_key):

```python
import scrapehub_client
from scrapehub_client.models.get_messages200_response import GetMessages200Response
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
    api_instance = scrapehub_client.ScrapeHubAPIMessagingApi(api_client)
    scraper_name = 'scraper_name_example' # str | Optional scraper name to filter messages

    try:
        api_response = api_instance.get_messages(scraper_name)
        print("The response of ScrapeHubAPIMessagingApi->get_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScrapeHubAPIMessagingApi->get_messages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scraper_name** | **str**| Optional scraper name to filter messages | 

### Return type

[**GetMessages200Response**](GetMessages200Response.md)

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

# **send_message**
> SendMessage200Response send_message(send_message_request)

Send a message to a scraper
User must be assigned to the scraper or have admin role

### Example

* Api Key Authentication (api_key):

```python
import scrapehub_client
from scrapehub_client.models.send_message200_response import SendMessage200Response
from scrapehub_client.models.send_message_request import SendMessageRequest
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
    api_instance = scrapehub_client.ScrapeHubAPIMessagingApi(api_client)
    send_message_request = scrapehub_client.SendMessageRequest() # SendMessageRequest | 

    try:
        api_response = api_instance.send_message(send_message_request)
        print("The response of ScrapeHubAPIMessagingApi->send_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScrapeHubAPIMessagingApi->send_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_message_request** | [**SendMessageRequest**](SendMessageRequest.md)|  | 

### Return type

[**SendMessage200Response**](SendMessage200Response.md)

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

