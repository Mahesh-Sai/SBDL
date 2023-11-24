import pytest

from lib.Utils import get_spark_session

'''The fixture is set to the scope of the entire session (scope='session'), 
meaning it will be created once and used for all tests in the session.'''
@pytest.fixture(scope='session')
def spark():
    return get_spark_session("LOCAL")


def test_blank_test(spark):
    print(spark.version)
    assert spark.version == "3.4.1"