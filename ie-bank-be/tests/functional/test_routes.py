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


# New test 1:
def test_update_account(testing_client):
    
    #GIVEN a Flask application
    #WHEN the '/accounts/<int:id>' page is posted to (PUT)
    #THEN check the response is valid
    
    response = testing_client.put('/accounts/1', json={'name': 'Johnny Doe', 'currency': '€', 'country': 'CountryName'})
    assert response.status_code == 200

# New test 2:
def test_delete_account(testing_client):
    
    #GIVEN a Flask application
    #WHEN the '/accounts/<int:id>' page is posted to (DELETE)
    #THEN check the response is valid
    
    response = testing_client.delete('/accounts/1')
    assert response.status_code == 200



