import unittest
from test_lib import TestAPIProxy, config
import json
import sys
sys.path.append('./src/lambda-functions')

class Test_ImageDataId_PUT(TestAPIProxy.TestAPIProxy):
    @classmethod
    def setUpClass(self):
        self.resource = 'image-data/\{id\}'
        self.method = 'PUT'
        self.lambda_handler = staticmethod(__import__(self.resource + '_' + self.method).lambda_handler)
    
    def test_valid(self):
        self.assertEqual(
            self.invoke_lambda(
                body={
                    'caption': 'a different new caption'
                },
                url_params={'id': config.test_img_db_id},
                query_params=None,
                headers=None,
            ),
            {
                'statusCode': 200,
                'body': {
                    "_id": config.test_img_db_id,
                    "url": "/bodies/7987419-insect-stag-beetle-isolated-in-white",
                    "name": "7987419-insect-stag-beetle-isolated-in-white",
                    "srcThumb": "Test_User/thumb/7987419-insect-stag-beetle-isolated-in-white.jpg",
                    "srcFull": "Test_User/full/7987419-insect-stag-beetle-isolated-in-white.jpg",
                    "caption": "a different new caption",
                    "series": "bodies",
                    "sequence": 12
                }
            }   
        )


    def test_invalid_id(self):
        self.assertEqual(
            self.invoke_lambda(
                body={
                    'caption': 'a different new caption'
                },
                url_params={'id': '123456789'},
                query_params=None,
                headers=None,
            ),
            {
                'statusCode': 404,
                'body': json.dumps('No image found for this id')
            }
        )
    
if __name__ == '__main__':
    unittest.main()