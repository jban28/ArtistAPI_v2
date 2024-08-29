import unittest
from test_lib import TestAPIProxy
import json
import sys
sys.path.append('./src/lambda-functions')
lambda_handler = __import__('image-data_GET').lambda_handler

class Test_login_POST(TestAPIProxy.TestAPIProxy):
    def test_valid(self):
        self.assertEqual(
            self.invoke_lambda(
                lambda_handler,
                'POST',
                resource=None,
                body=None,
                url_params=None,
                query_params=None,
                headers={'Authorization': 'testUser:password123'},
            ),
            {
                'statusCode': 200,
                'body': json.dumps('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcnRpc3QiOiJUZXN0X1VzZXIifQ.MsysHQTVctUs93RbErKyIhkEb3QCSXxPOMCmJygt4kA')
            }   
        )

    def test_incorrect_user(self):
        self.assertEqual(
            self.invoke_lambda(
                lambda_handler,
                'POST',
                resource=None,
                body=None,
                url_params=None,
                query_params=None,
                headers={'Authorization': 'notTestUser:password123'},
            ),
            {
                'statusCode': 403,
                'body': json.dumps('Incorrect username or password')
            }   
        )

    def test_incorrect_pwd_for_user(self):
        self.assertEqual(
            self.invoke_lambda(
                lambda_handler,
                'POST',
                resource=None,
                body=None,
                url_params=None,
                query_params=None,
                headers={'Authorization': 'TestUser:wrongPwd'},
            ),
            {
                'statusCode': 403,
                'body': json.dumps('Incorrect username or password')
            }   
        )

    def test_incorrect_format(self):
        self.assertEqual(
            self.invoke_lambda(
                lambda_handler,
                'POST',
                resource=None,
                body=None,
                url_params=None,
                query_params=None,
                headers={'Authorization': 'TestUserpassword123'},
            ),
            {
                'statusCode': 403,
                'body': json.dumps('Invalid format for Authorization header. Expected username:password')
            }   
        )
    
if __name__ == '__main__':
    unittest.main()