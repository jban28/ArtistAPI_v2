import unittest
from test_lib import config
import json
import sys
sys.path.append('./src/lambda-functions')

class Test_authenticate(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.lambda_handler = staticmethod(__import__('authenticate.py').lambda_handler)

    def invoke_auth(self, token):
        return self.lambda_handler(
            {
                'authorizationToken': token,
                'methodARN': 'test_method'
            }, 
            'context')
    
    def test_valid(self):
        self.assertEqual(
            self.invoke_auth(config.TEST_AUTH_TOKEN),
            {
                'statusCode': 200,
                'body': {
                    "principalId": "Test_user", # The principal user identification associated with the token sent by the client.
                    "policyDocument": {
                        "Version": "2012-10-17",
                        "Statement": [
                        {
                            "Action": "execute-api:Invoke",
                            "Effect": "Allow",
                            "Resource": 'test_method'
                        }
                        ]
                    },
                    "context": {
                        "artist": "Test_User",
                    }
                }
            }
        )

    def test_not_jwt(self):
        self.assertEqual(
            self.invoke_auth('not a token'),
            {
                'statusCode': 500,
                'body': json.dumps('Invalid token')
            }
        )
