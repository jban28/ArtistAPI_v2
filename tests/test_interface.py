from lambda_function_tests import *
import unittest
import test_lib

test_lib.config.TEST_ENV = 'LOCAL'
unittest.main()