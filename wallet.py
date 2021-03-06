from exception import InsufficientAmount

class Wallet():
  def __init__(self, initial_amount = 0):
    self.balance = initial_amount

  def add_cash(self, amount):
    self.balance += amount
  
  def spend_cash(self, amount):
    if self.balance < amount:
      raise InsufficientAmount('Not enough cash to spend {}'.format(amount))
    self.balance -= amount