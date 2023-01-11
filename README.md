# learn_pytest
learning pytest concepts

# pytest rules
- file name must begin with test_ or end with _test
- each test case must also begin with test
- run all test quickly : pytest
- run all tests verbose : pytest -v
- run all tests verbose and with output : pytest -v -s
- run specific test : pytest -v -s file name
- run specific keyword test : pytest -k keyword
- group test case together : @pytest.mark.namehere and then to run pytest -m marker name
