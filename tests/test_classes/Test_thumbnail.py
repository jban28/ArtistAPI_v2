import unittest
import sys
sys.path.append('./src/lambda-functions')
py_file = __import__('thumbnail')

class Test_thumbnail(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.lambda_handler = staticmethod(py_file.lambda_handler)
        self.test_image_path = './tests/sample-images/Shorts_1.jpg'

class Test_generate_thumbnail(unittest.TestCase):
    pass