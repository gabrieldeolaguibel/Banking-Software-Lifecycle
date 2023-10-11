from iebank_api import app
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

# This test will check the response when an existing account is updated via a PUT request to the /accounts/<account_id> endpoint.
def test_update_account(client):
    # Create a new account
    response = client.post('/accounts', json={
        'name': 'John Doe',
        'balance': 1000.0,
        'country': 'US'
    })
    account_id = response.json['id']

    # Update the account
    response = client.put(f'/accounts/{account_id}', json={
        'name': 'Jane Doe',
        'balance': 1500.0,
        'country': 'UK'
    })

    assert response.status_code == 200
    assert response.json['name'] == 'Jane Doe'
    assert response.json['balance'] == 1500.0
    assert response.json['country'] == 'UK'


# This test will check the response when an account is deleted via a DELETE request to the /accounts/<account_id> endpoint.
def test_delete_account(client):
    # Create a new account
    response = client.post('/accounts', json={
        'name': 'John Doe',
        'balance': 1000.0,
        'country': 'US'
    })
    account_id = response.json['id']

    # Delete the account
    response = client.delete(f'/accounts/{account_id}')

    assert response.status_code == 200
    assert response.json['message'] == f"Account {account_id} has been deleted."




