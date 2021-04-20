import pytest
from wallet import Wallet

def test_default_initial_amount():
  wallet = Wallet()
  assert wallet.balance == 0

def test_setting_initial():
  wallet = Wallet(10)
  assert wallet.balance == 10