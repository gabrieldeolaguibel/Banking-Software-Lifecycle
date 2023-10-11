from iebank_api import app
from iebank_api.models import Account
from app import db
import pytest

def test_get_accounts(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts' page is requested (GET)
    THEN check the response is valid
    """
    response = testing_client.get('/accounts')
    assert response.status_code == 200

def test_dummy_wrong_path():
    """
    GIVEN a Flask application
    WHEN the '/wrong_path' page is requested (GET)
    THEN check the response is valid
    """
    with app.test_client() as client:
        response = client.get('/wrong_path')
        assert response.status_code == 404

def test_create_account(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts' page is posted to (POST)
    THEN check the response is valid
    """
    response = testing_client.post('/accounts', json={'name': 'John Doe', 'currency': '€', 'country': 'CountryName'}) # Added country
    assert response.status_code == 200

# This test will check if accessing a specific account via its ID returns the correct account details.
def test_get_single_account(client):
    # Create a dummy account
    account = Account(name="Test Account", currency="USD", country="USA")
    db.session.add(account)
    db.session.commit()

    # Fetch the account details via the API
    response = client.get(f"/accounts/{account.id}")

    # Assert that the response contains the correct account details
    assert response.status_code == 200
    assert response.json["name"] == "Test Account"

# This test will check if accessing an account that doesn't exist returns a 404 status code.
def test_account_not_found(client):
    # Try to fetch an account that doesn't exist
    response = client.get("/accounts/9999")

    # Assert that the response returns a 404 status code
    assert response.status_code == 404




