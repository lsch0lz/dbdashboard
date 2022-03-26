import pytest
import requests

def test_db_api():
    response = requests.get("https://api.deutschebahn.com/freeplan/v1/location/Berlin")
    assert response.status_code == 200