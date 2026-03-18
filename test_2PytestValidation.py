#fixtures: provide reusable; code across multiple test case
#fixtures have scope:module /class :run only once time fixtures
#fixtures have scope:function:run multiple time fixture
#fixtures have scope:session:run only once time fixture
import pytest




def test_thirdCheck(preSetupWork):
    print('This is third test')
