from lambda_function_tests import *
import unittest
import test_lib

if __name__ == '__main__':
    test_lib.config.LOCAL_TEST = False
    unittest.main()