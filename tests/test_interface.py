from test_classes import *
import unittest
import test_lib
import sys

test_lib.config.TEST_ENV = sys.argv.pop(1)
unittest.main()