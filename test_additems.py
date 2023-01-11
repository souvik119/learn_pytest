import pytest

def test_login():
    print("Login Successful")

@pytest.mark.sanity
def test_logoff():
    print("Logoff Successful")

def test_Calculation():
    assert 2+2 == 4