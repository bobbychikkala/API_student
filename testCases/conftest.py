import pytest
import requests


@pytest.fixture()
def getResponse():
    url = "http://localhost:3000/student"
    ##send Get request
    resp = requests.get(url)
    return resp