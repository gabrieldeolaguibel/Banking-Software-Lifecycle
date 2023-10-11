from iebank_api import app
import pytest
from iebank_api.models import Account

@pytest.fixture
def test_account():
    account = Account(name="Test User", currency="$", country="USA")
    # Save the account to the database if needed
    return account

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

# Test for Creating a New Account with Valid Data:
def test_create_new_account(client):
    data = {
        "name": "John Doe",
        "currency": "€",
        "country": "Spain"
    }
    response = client.post("/accounts", json=data)
    assert response.status_code == 200
    assert response.json()["name"] == data["name"]
    assert response.json()["currency"] == data["currency"]
    assert response.json()["country"] == data["country"]
    assert response.json()["balance"] == 0.0
    assert response.json()["status"] == "Active"

# Test for Fetching Account Details with Valid Account Number:

def test_get_account_details(client, test_account):
    account_number = test_account.account_number
    response = client.get(f"/accounts/{account_number}")
    assert response.status_code == 200
    assert response.json()["name"] == test_account.name
    assert response.json()["currency"] == test_account.currency
    assert response.json()["country"] == test_account.country




