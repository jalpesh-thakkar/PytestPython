#fixtures: provide reusable; code across multiple test case
#fixtures have scope:module /class :run only once time fixtures
#fixtures have scope:function:run multiple time fixture
#fixtures have scope:session:run only once time fixture
#assert is check the fixtures value with test cases
import pytest


@pytest.fixture(scope='module')
def preWork():
    print('I setup module instance')
    return "fail"

def test_initialCheck(preWork):
    print('This is first test')
    assert preWork == "fail"

def test_SecondCheck(preSetupWork):
    print('This is second test')
