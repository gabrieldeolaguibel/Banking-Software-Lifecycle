import pytest
from iebank_api.models import Account
from iebank_api import db, app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


@pytest.fixture(scope='function')
def session():
    db.create_all()
    yield db.session
    db.session.remove()
    db.drop_all()

@pytest.fixture
def testing_client(scope='module'):
    db.create_all()
    account = Account('Test Account', '€', 'CountryName')
    db.session.add(account)
    db.session.commit()

    with app.test_client() as testing_client:
        yield testing_client

    db.drop_all()