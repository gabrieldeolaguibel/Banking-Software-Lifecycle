from iebank_api.models import Account
import pytest

def test_create_account():
    """
    GIVEN a Account model
    WHEN a new Account is created
    THEN check the name, account_number, balance, currency, status and created_at fields are defined correctly
    """
    account = Account('John Doe', '€', 'CountryName')
    assert account.name == 'John Doe'
    assert account.currency == '€'
    assert account.account_number != None
    assert account.balance == 0.0
    assert account.status == 'Active'

# New Test: Test for Account Model Initialization:
# initialization of an account object with specific values and checks if the fields are set correctly.
def test_account_initialization():
    account = Account(name="John Doe", currency="€", country="Spain")
    assert account.name == "John Doe"
    assert account.currency == "€"
    assert account.country == "Spain"
    assert account.balance == 0.0
    assert account.status == "Active"
    assert len(account.account_number) == 20


# New Test: Test for Account Model String Representation:
# This test is important because the string representation of an object is often used for debugging and logging purposes. 
def test_account_repr():
    account = Account(name="John Doe", currency="€", country="Spain")
    assert repr(account) == f"<Event '{account.account_number}'>"





