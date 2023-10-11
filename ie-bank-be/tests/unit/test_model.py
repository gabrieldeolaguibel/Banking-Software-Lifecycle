from iebank_api.models import Account
from app import db
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

# This test will check if an existing account's details can be updated correctly.
def test_update_account():
    # Create a dummy account
    account = Account(name="Test Account", currency="USD", country="USA")
    db.session.add(account)
    db.session.commit()

    # Update the account details
    account.name = "Updated Test Account"
    db.session.commit()

    # Fetch the updated account from the database
    updated_account = Account.query.get(account.id)

    # Assert that the account details were updated correctly
    assert updated_account.name == "Updated Test Account"

# This test will check if an account can be deleted correctly.
def test_delete_account():
    # Create a dummy account
    account = Account(name="Test Account", currency="USD", country="USA")
    db.session.add(account)
    db.session.commit()

    # Delete the account
    db.session.delete(account)
    db.session.commit()

    # Try to fetch the deleted account from the database
    deleted_account = Account.query.get(account.id)

    # Assert that the account was deleted
    assert deleted_account is None

