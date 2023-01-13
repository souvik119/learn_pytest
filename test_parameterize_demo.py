import pytest

#1st method
#if you want to test with different inputs then parameterize it
# @pytest.fixture(params=["a", "b"])
# def demo_fixture(request):
#     print(request.param)

# def testLogin(demo_fixture):
#     print("Login Successful")

#since parameterized fixture is used here it will run the test case twice, once with "a" and 2nd time with "b"
#2nd method
@pytest.mark.parametrize("a, b, final", [(2, 4, 6), (4, 5, 8), (7, 7, 14)])
def testAdd(a, b, final):
    assert a + b == final

