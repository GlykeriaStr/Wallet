class Wallet():
  def __init__(self, initial_amount = 0):
    self.balance = initial_amount

  def add_cash(self, amount):
    self.balance += amount