import pytest
import requests

def test_db_locations():
    response = requests.get("https://api.deutschebahn.com/freeplan/v1/location/Berlin")
    assert response.status_code == 200

def test_db_arrivalBoard():
    response = requests.get("https://api.deutschebahn.com/freeplan/v1/arrivalBoard/8011160?date=2022-01-01")
    assert response.status_code == 200

def test_db_departureBoard():
    response = requests.get("https://api.deutschebahn.com/freeplan/v1/departureBoard/8011160?date=2022-01-01")
    assert response.status_code == 200
