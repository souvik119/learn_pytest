import pytest

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

#to use fixture add it as argument
def testAddItemtoCart(setUp):
    print("Item added successfully")

def testRemoveItemfromCart(setUp):
    print("Item removed successfully")