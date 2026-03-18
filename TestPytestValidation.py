#fixtures: provide reusable; code across multiple test case
#fixtures have scope:module /class :run only once time fixtures
#fixtures have scope:function:run multiple time fixture
#fixtures have scope:session:run only once time fixture
import pytest



def test_initialCheck(preSetupWork):
    print('This is first test')

def test_SecondCheck(preSetupWork):
    print('This is second test')
