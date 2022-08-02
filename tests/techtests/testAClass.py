import unittest
import sys
import os
import json

# import core to test
from core.businesslayer.AClass import AClass
# each file should have a test unit entry to check non regression
# note that mgt_files, mgt_logs, mgt_xxx modules do not need tests as they are already tested into common project !


# use local path as mountpoint to found directories data in test
project_folder = os.path.abspath("app.py")[:-18]
sys.path.append(project_folder)
TEST_PATH1 = './data/test1'
TEST_PATH2 = './data/test2'


class TestAclass(unittest.TestCase):
    def test_explorepath(self):
        # call your code core here
        a = AClass(myparam="p1")
        assert(a is not None)


if __name__ == '__main__':
    unittest.main()
