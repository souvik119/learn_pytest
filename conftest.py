import pytest

#this setup can be applied to any test file by including it as argument
#@pytest.fixture(autouse=True) for using without having to enter it in arguments everytime
#@pytest.fixture(scope="session") scope defines when the fixture is created and destroyed, can be function, class, session, module, package, default is function scope
@pytest.fixture() 
def setUp():
    print("Launch browser")
    print("Login")
    print("Browse products")
    #before yield is setup
    yield
    #after yield is teardown
    print("Logoff")
    print("Close browser")