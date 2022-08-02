### Tests

2 mandatory repositories

functests : not managed automatically by Jenkins , used only to launch locolly flask/rest

techtests : each class or module (functions) should have a unit test written in pyunit
            and using asset 
            the tests are used to non regression !!!
           
           You do not have to tests each module (sub packages of core) nammed mgt_
           for instance : mgt_logs, mgt_config,...
#
# All tests should process data with local data in tests ! not in prod/val mountpoint.
# A directory data should be used to add data

use local path as mountpoint to found directories data in test :

sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
TEST_PATH1='./data/test1'
TEST_PATH2='./data/test2'
