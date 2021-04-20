import pytest
from wallet import Wallet 
from exception import InsufficientAmount

@pytest.fixture
def empty_wallet():
  return Wallet()

@pytest.fixture
def wallet():
  return Wallet(90)

def test_default_initial_amount(empty_wallet):
  assert empty_wallet.balance == 0

def test_setting_initial(wallet):
  assert wallet.balance == 90

def test_add_cash(wallet):
  wallet.add_cash(10)
  assert wallet.balance == 100

def test_spend_cash(wallet):
  wallet.spend_cash(10)
  assert wallet.balance == 80

def test_spend_cash_raises_exception_on_insufficient_amount(wallet):
  with pytest.raises(InsufficientAmount):
    wallet.spend_cash(100)