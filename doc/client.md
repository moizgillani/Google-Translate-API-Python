
# Client Class Documentation

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| `http_client_instance` | `HttpClient` | The Http Client passed from the sdk user for making requests |
| `override_http_client_configuration` | `bool` | The value which determines to override properties of the passed Http Client from the sdk user |
| `http_call_back` | `HttpCallBack` | The callback value that is invoked before and after an HTTP call is made to an endpoint |
| `timeout` | `float` | The value to use for connection timeout. <br> **Default: 60** |
| `max_retries` | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 0** |
| `backoff_factor` | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 2** |
| `retry_statuses` | `Array of int` | The http statuses on which retry is to be done. <br> **Default: [408, 413, 429, 500, 502, 503, 504, 521, 522, 524]** |
| `retry_methods` | `Array of string` | The http methods on which retry is to be done. <br> **Default: ['GET', 'PUT']** |
| `x_rapidapi_key` | `string` | your api key<br>*Default*: `'934533e5acmshf8fc49652f327f6p114b48jsn7b772d101303'` |
| `x_rapid_api_host` | `string` | api key host<br>*Default*: `'google-translate1.p.rapidapi.com'` |
| `content_type` | `string` | content type<br>*Default*: `'x-www-form-urlencoded'` |

The API client can be initialized as follows:

```python
from googletranslateapi.googletranslateapi_client import GoogletranslateapiClient
from googletranslateapi.configuration import Environment

client = GoogletranslateapiClient(
    x_rapidapi_key='934533e5acmshf8fc49652f327f6p114b48jsn7b772d101303',
    x_rapid_api_host='google-translate1.p.rapidapi.com',
    content_type='x-www-form-urlencoded',
    environment=Environment.PRODUCTION
)
```

## Google Translate API Client

The gateway for the SDK. This class acts as a factory for the Controllers and also holds the configuration of the SDK.

## Controllers

| Name | Description |
|  --- | --- |
| test | Gets TestController |

