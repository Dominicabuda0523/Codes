# Write code below 💖

class BankAccount:
  def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
    self.first_name = first_name
    self.last_name = last_name
    self.account_id = account_id
    self.account_type = account_type
    self.pin = pin
    self.balance = balance

  def deposit(self, amount):
    self.balance += amount
    return self.balance

  def withdraw(self, amount):
    self.balance -= amount
    return self.balance

  def display_balance(self):
    print(f'Your current balance is ${self.balance}.')

student1 = BankAccount('Dominic', 'Abuda', 230509, 'Student', 269540, 0)

student1.deposit(96)
student1.withdraw(25)
student1.display_balance()