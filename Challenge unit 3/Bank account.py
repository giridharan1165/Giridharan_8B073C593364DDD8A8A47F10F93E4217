class BankAccount:

  def __init__(self, account_number, account_holder_name, initial_balance=0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = initial_balance

  def deposit(self, amount):
    self.__account_balance += amount

  def withdraw(self, amount):
    if amount <= self.__account_balance:
      self.__account_balance -= amount
    else:
      print("Insufficient funds")

  def display_balance(self):
    return self.__account_balance


my_account = BankAccount("123456789", "John Doe", 1000)
print("Initial balance:", my_account.display_balance())

my_account.deposit(500)
print("Balance after deposit:", my_account.display_balance())

my_account.withdraw(200)
print("Balance after withdrawal:", my_account.display_balance())
