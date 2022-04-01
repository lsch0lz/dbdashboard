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

def test_marudor_details():
    response = requests.get("https://marudor.de/api/hafas/v2/details/ice23")
    assert response.status_code == 200

def test_marudor_reihung():
    response = requests.get("https://marudor.de/api/reihung/v4/runsPerDate/2022-03-24T11:50:00.000Z")
    assert response.status_code == 500
