import pytest
from wallet import Wallet 
from exception import InsufficientAmount

@pytest.fixture
def empty_wallet():
  '''Returns a Wallet instance with a zero balance'''
  return Wallet()

@pytest.fixture
def wallet():
  '''Returns a Wallet instance with a balance of 20'''
  return Wallet(90)

@pytest.mark.parametrize('earned, spent, expected', [
  (30, 20, 10),
  (50, 30, 20),
])

def test_transactions(empty_wallet, earned, spent, expected):
  empty_wallet.add_cash(earned)
  empty_wallet.spend_cash(spent)
  assert empty_wallet.balance == expected

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