import pytest
from wallet import Wallet

def test_default_initial_amount():
  wallet = Wallet()
  assert wallet.balance == 0

def test_setting_initial():
  wallet = Wallet(10)
  assert wallet.balance == 10

def test_add_cash():
  wallet = Wallet(90)
  wallet.add_cash(10)
  assert wallet.balance == 100

def test_spend_cash():
  wallet = Wallet(100)
  wallet.spend_cash(10)
  assert wallet.balance == 90