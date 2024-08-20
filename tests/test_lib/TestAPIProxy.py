import unittest
import requests
import json
from . import config

class TestAPIProxy(unittest.TestCase):
    def invoke_lambda(
        self,
        handler_func,
        http_method,
        resource,
        body=None,
        url_params=None,
        query_params=None,
        headers=None,
    ):
        path = resource

        if url_params:
            for param_name in url_params:
                path = path.replace('{' + param_name + '}', url_params[param_name])

        if config.TEST_ENV == 'LOCAL':
            test_json = {
                "resource": resource, # Changed
                "path": path, # Changed
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

            return handler_func(test_json, 'context')

        elif (config.TEST_ENV == 'DEV' or config.TEST_ENV == 'LIVE'):
            base_url = 'https://78lf70b7ha.execute-api.eu-west-2.amazonaws.com/'
            base_url += 'live' if config.TEST_ENV == 'LIVE' else 'dev'
            
            full_url = base_url + path
            
            response =  requests.request(http_method, 
                full_url,
                params=query_params,
                json=body,
                headers=headers
            )

            return {
                "statusCode": response.status_code,
                "body": response.text
            }

        else:
            raise ValueError('Unexpected value for test environment, expected \
                "LOCAL", "DEV" or "LIVE" but got "' + config.TEST_ENV + '"')