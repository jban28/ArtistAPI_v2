import unittest
from test_lib import TestAPIProxy, config
import json
import sys
sys.path.append('./src/lambda-functions')

class Test_ImageId_DELETE(TestAPIProxy.TestAPIProxy):
    @classmethod
    def setUpClass(self):
        self.resource = 'image/{id}'
        self.method = 'DELETE'
        lambda_path = self.resource.replace('/', '_').replace('{', '').replace('}','') + '_' + self.method
        self.lambda_handler = staticmethod(__import__(lambda_path).lambda_handler)
    
    def test_valid(self):
        self.assertEqual(
            self.invoke_lambda(
                body=None,
                url_params={'id': config.test_img_db_id},
                query_params=None,
                headers={'Authorization': config.TEST_AUTH_TOKEN},
            ),
            {
                'statusCode': 200,
                'body': json.dumps('Resource deleted successfully')
            }   
        )

    def test_repeat_valid(self):
        self.assertEqual(
            self.invoke_lambda(
                body=None,
                url_params={'id': config.test_img_db_id},
                query_params=None,
                headers={'Authorization': config.TEST_AUTH_TOKEN},
            ),
            {
                'statusCode': 404,
                'body': json.dumps('No image found for this id')
            }   
        )
    
if __name__ == '__main__':
    unittest.main()