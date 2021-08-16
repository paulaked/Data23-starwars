import validators
import pytest
from app.api import api_request, api_call


# test that api call is valid, error code 200
def test_apicode():
     response, url, status = api_request([], "https://swapi.dev/api/starships")
     assert status == 200 ,   "Check that the request was succesfully completed"

# test that url outpus is a valid url or null
def test_url():
    response, url, status = api_request([], "https://swapi.dev/api/starships")
    assert validators.url(url) or url is None









