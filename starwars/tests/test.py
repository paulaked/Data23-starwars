import unittest
import pytest
import json
from api import api_call

# test that api call is valid, error code 200
def test_apicode():
    """
    Test that the correct html code is returned
    """
    assert api_call() == "Response<200>"

# test that api call content can be converted into json
def test_convert():
     api_json = api_call()
     assert api_json ==json.loads(api_json)

# test that api call is not empty
def test_apicode_not_empty():
    """
    Test that imported file is not empty
    """
    assert content.api_call != []


# test that ship json has an object id in the pilot section

# check that a corresponding pilot id is the starships json

# call the startships object from mongdo db and compare to the original json

if __name__ == '__main__':
    unittest.main()