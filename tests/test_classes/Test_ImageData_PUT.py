import unittest
from test_lib import TestAPIProxy, config
import json
import sys
sys.path.append('./src/lambda-functions')

class Test_ImageData_PUT(TestAPIProxy.TestAPIProxy):
    @classmethod
    def setUpClass(self):
        self.resource = 'image-data'
        self.method = 'PUT'
        self.lambda_handler = staticmethod(__import__(self.resource + '_' + self.method).lambda_handler)
    
    def test_valid(self):
        response = self.invoke_lambda(
                body={
                    '_id': config.test_img_db_id,
                    'caption': 'a new caption'
                },
                url_params=None,
                query_params=None,
                headers={'Authorization': config.TEST_AUTH_TOKEN},
            )
        
        self.assertEqual(response['statusCode'], 200)
    
if __name__ == '__main__':
    unittest.main()