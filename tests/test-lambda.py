import requests

LOCAL_TEST = True

def test_lambda( 
        handler_func,
        http_method,
        resource=None,
        body=None,
        url_params=None,
        query_params=None,
        headers=None,
    ):

    url = resource

    if url_params:
        for param_name in url_params:
            url = url.replace('{' + param_name + '}', url_params[param_name])

    if LOCAL_TEST:
        test_json = {
            "resource": resource, # Changed
            "path": url, # Changed
            "httpMethod": http_method, # Changed
            "headers": headers, # Changed
            "multiValueHeaders": {
                "header1": [
                "value1"
                ],
                "header2": [
                "value1",
                "value2"
                ]
            },
            "queryStringParameters": query_params, # Changed
            "multiValueQueryStringParameters": {
                "parameter1": [
                "value1",
                "value2"
                ],
                "parameter2": [
                "value"
                ]
            },
            "requestContext": {
                "accountId": "123456789012",
                "apiId": "id",
                "authorizer": {
                "claims": None,
                "scopes": None
                },
                "domainName": "id.execute-api.us-east-1.amazonaws.com",
                "domainPrefix": "id",
                "extendedRequestId": "request-id",
                "httpMethod": "GET",
                "identity": {
                "accessKey": None,
                "accountId": None,
                "caller": None,
                "cognitoAuthenticationProvider": None,
                "cognitoAuthenticationType": None,
                "cognitoIdentityId": None,
                "cognitoIdentityPoolId": None,
                "principalOrgId": None,
                "sourceIp": "IP",
                "user": None,
                "userAgent": "user-agent",
                "userArn": None,
                "clientCert": {
                    "clientCertPem": "CERT_CONTENT",
                    "subjectDN": "www.example.com",
                    "issuerDN": "Example issuer",
                    "serialNumber": "a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1",
                    "validity": {
                    "notBefore": "May 28 12:30:02 2019 GMT",
                    "notAfter": "Aug  5 09:36:04 2021 GMT"
                    }
                }
                },
                "path": "/my/path",
                "protocol": "HTTP/1.1",
                "requestId": "id=",
                "requestTime": "04/Mar/2020:19:15:17 +0000",
                "requestTimeEpoch": 1583349317135,
                "resourceId": None,
                "resourcePath": "/my/path",
                "stage": "$default"
            },
            "pathParameters": url_params, # Changed
            "stageVariables": None,
            "body": body, # Changed
            "isBase64Encoded": False
        }

        return handler_func(test_json)

    else:
        return requests.request(http_method, 
            url,
            params=query_params,
            json=body,
            headers=headers
        )