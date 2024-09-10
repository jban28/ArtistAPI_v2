import unittest
from test_lib import TestAPIProxy
import json
import sys
sys.path.append('./src/lambda-functions')

class Test_ImageData_GET(TestAPIProxy.TestAPIProxy):
    @classmethod
    def setUpClass(self):
        self.resource = 'image-data'
        self.method = 'GET'
        self.lambda_handler = staticmethod(__import__(self.resource + '_' + self.method).lambda_handler)
        
    def test_valid(self):
        self.assertEqual(
            self.invoke_lambda(
                body=None,
                url_params=None,
                query_params={'artist': 'Test_User'},
                headers=None,
            ),
            {
                'statusCode': 200,
                'body': [ 
                    {
                        "url": "/bodies/shorts_1",
                        "name": "Shorts 1",
                        "srcThumb": "Test_User/thumb/Shorts_1.jpg",
                        "srcFull": "Test_User/full/Shorts_1.jpg",
                        "caption": "Shorts 1; pen on paper; 21 x 21 cm, 2020",
                        "series": "sampleSeries1",
                        "sequence": 2
                    },
                    {
                        "url":"/bodies/trainer_1",
                        "name":"Trainer 1",
                        "srcThumb":"Test_User/thumb/Trainer_1.jpg",
                        "srcFull":"Test_User/full/Trainer_1.jpg",
                        "caption":"Trainer 1; pen on paper; 21 x 21 cm, 2020",
                        "series":"sampleSeries1",
                        "sequence":1
                    }
                ]
            }
        )

    def test_missing_artist(self):
        self.assertEqual(
            self.invoke_lambda(
                body=None,
                url_params=None,
                query_params=None,
                headers=None,
            ),
            {
                'statusCode': 400,
                'body': json.dumps('No artist specified')
            }
        )

    def test_invalid_artist(self):
        self.assertEqual(
            self.invoke_lambda(
                body=None,
                url_params=None,
                query_params={'artist': 'Non_existent_artist'},
                headers=None,
            ),
            {
                'statusCode': 400,
                'body': json.dumps('Artist not found')
            }
        )
    
if __name__ == '__main__':
    unittest.main()