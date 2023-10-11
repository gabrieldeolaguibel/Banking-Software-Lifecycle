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

# This test will check the functionality of updating the balance of an existing account.
def test_update_account_balance(session):
    # Create a new account
    account = Account(name='John Doe', balance=1000.0, country='US')
    session.add(account)
    session.commit()

    # Update the balance
    account.balance = 1500.0
    session.commit()

    assert account.balance == 1500.0

# This test will check the functionality of adding a country to an existing account.
def test_add_country_to_account(session):
    # Create a new account without a country
    account = Account(name='John Doe', balance=1000.0)
    session.add(account)
    session.commit()

    # Add a country to the account
    account.country = 'US'
    session.commit()

    assert account.country == 'US'



