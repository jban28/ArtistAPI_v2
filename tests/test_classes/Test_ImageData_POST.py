import unittest
from test_lib import TestAPIProxy, config
import json
import sys
sys.path.append('./src/lambda-functions')

class Test_ImageData_POST(TestAPIProxy.TestAPIProxy):
    @classmethod
    def setUpClass(self):
        self.resource = 'image-data'
        self.method = 'POST'
        self.lambda_handler = staticmethod(__import__(self.resource + '_' + self.method).lambda_handler)

    def test_valid_new_data(self):
        response = self.invoke_lambda(
                body={
                    "url": "/bodies/7987419-insect-stag-beetle-isolated-in-white",
                    "name": "7987419-insect-stag-beetle-isolated-in-white",
                    "srcThumb": "Test_User/thumb/7987419-insect-stag-beetle-isolated-in-white.jpg",
                    "srcFull": "Test_User/full/7987419-insect-stag-beetle-isolated-in-white.jpg",
                    "caption": "7987419-insect-stag-beetle-isolated-in-white; pen on paper; 21 x 30 cm; 2015",
                    "series": "bodies",
                    "sequence": 12
                },
                url_params=None,
                query_params=None,
                headers={'Authorization': config.TEST_AUTH_TOKEN},
            )
        
        self.assertEqual(
            response['statusCode'], 200 
        )

        response_json = json.parse(response['body'])['id']

        self.assertIn('id', response_json)

        config.test_img_db_id = response_json['id']


    def test_no_body(self):
        self.assertEqual(
            self.invoke_lambda(
                body=None,
                url_params=None,
                query_params=None,
                headers={'Authorization': config.TEST_AUTH_TOKEN},
            ),
            {
                'statusCode': 400,
                'body': json.dumps('No data provided')
            }
        )
    
if __name__ == '__main__':
    unittest.main()