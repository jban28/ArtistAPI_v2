import unittest
from test_lib import TestAPIProxy
import json
import sys
sys.path.append('./src/lambda-functions')
lambda_handler = __import__('image-data_GET').lambda_handler

class Test_ImageDataId_PUT(TestAPIProxy.TestAPIProxy):
    def test_valid(self):
        self.assertEqual(
            self.invoke_lambda(
                lambda_handler,
                'GET',
                resource=None,
                body=None,
                url_params=None,
                query_params=None,
                headers=None,
            ),
            {
                'statusCode': 200,
                'body': json.dumps('Hello from Lambda!')
            }   
        )
    
if __name__ == '__main__':
    unittest.main()