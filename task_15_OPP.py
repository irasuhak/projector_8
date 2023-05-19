## Practice

# **Task 1**. 
# Create a class Product with properties name, price, and quantity. 
# Create a child class Book that inherits from Product and adds a property author and a method called read.  

# Конструктор батьківського класу Product
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

# Конструктор класу Product, що успадковує атрибути класу Product швидким методом super() 
# та додає додатковий атрибут і метод
class Book(Product):
    def __init__(self, name, price, quantity, author):
        super().__init__(name, price, quantity)
        self.author = author
    
    def read(self):
        print(f'Reading {self.name} by {self.author}')
        

chosen_product = Product('Phone', 5000, 10)
chosen_book = Book('Python Cookbook', 400, 5, 'David Beazley')

chosen_book.read()
        


# **Task 2**. 
# Create a class Restaurant with properties name, cuisine, and menu. 
# The menu property should be a dictionary with keys being the dish name and values being the price. 
# Create a child class FastFood that inherits from Restaurant and adds a property drive_thru 
# (a boolean indicating whether the restaurant has a drive-thru or not) 
# and a method called order which takes in the dish name and quantity and returns the total cost of the order. 
# The method should also update the menu dictionary to subtract the ordered quantity from the available quantity. 
# If the dish is not available or if the requested quantity is greater than the available quantity, 
# the method should return a message indicating that the order cannot be fulfilled.  

from typing import Dict, Union

class Restaurant:
    def __init__(self, name: str, cuisine: str, menu: Dict[str, Dict[str, Union[float, int]]]):
        self.name = name
        self.cuisine = cuisine
        self.menu = menu

class FastFood(Restaurant):
    def __init__(self, name: str, cuisine: str, menu: Dict[str, Dict[str, Union[float, int]]], drive_thru: bool):
        super().__init__(name, cuisine, menu)
        self.drive_thru = drive_thru
        
    def order(self, dish_name: str, quantity: int) -> Union[float, str]:
        if dish_name in self.menu:
            dish = self.menu[dish_name]
            dish_price = dish['price']
            available_quantity = dish['quantity']
            if quantity > 0:
                if quantity <= available_quantity:
                    total_cost = dish_price * quantity
                    dish['quantity'] -= quantity
                    return total_cost
                else:
                    return 'Requested quantity not available'
        else:
            return 'Dish not available'


menu =  {
    'burger': {'price': 5, 'quantity': 10},
    'pizza': {'price': 10, 'quantity': 20},
    'drink': {'price': 1, 'quantity': 15}
}

mc = FastFood('McDonalds', 'Fast Food', menu, True)

print(mc.order('burger', 5)) # 25
print(mc.order('burger', 15)) # Requested quantity not available
print(mc.order('soup', 5)) # Dish not available



# 3. **(Optional) A Bank**

# A. Using the Account class as a base class, write two derived classes called SavingsAccount and CurrentAccount. 
#    A SavingsAccount object, in addition to the attributes of an Account object, 
#    should have an interest attribute and a method which adds interest to the account. 
#    A CurrentAccount object, in addition to the attributes of an Account object, should have an overdraft limit attribute.

class Account:
    def __init__(self, balance, account_number):
        self._balance = balance
        self._account_number = account_number
    
    @classmethod
    def create_account(cls, account_number):
        return cls(0.0, account_number)
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError('Amount must be positive')

    def withdraw(self, amount):
        if amount > 0:
            self._balance -= amount
        else:
            raise ValueError('Amount must be positive')

    def get_balance(self):
        return self._balance
    
    def get_account_number(self):
        return self._account_number
    
    def __str__(self):
        return f'Account number: {self._account_number}, balance: {self._balance}'


# Створення похідного класу SavingsAccount
class SavingsAccount(Account):
    def __init__(self, balance, account_number, interest): 
        super().__init__(balance, account_number)
        self._interest = interest  # Відсоткова ставка
        
    def add_interest(self):
        interest_ammount = self._balance * self._interest  # Обчислення суми відсотків
        self._balance += interest_ammount  # Додавання відсотків до балансу рахунку
        
    def __str__(self):
        return f'Account number: {self._account_number}, Balance: {self._balance}, Interests: {self._interest}'
    
    
# Створення похідного класу CurrentAccount
class CurrentAccount(Account):
    def __init__(self, balance, account_number, overdraft_limit):
        super().__init__(balance, account_number)
        self._overdraft_limit = overdraft_limit
        
    def get_overdraft_limit(self):
        return self._overdraft_limit
    
    def __str__(self):
        return f'Account number: {self._account_number}, Balance: {self._balance}, Overdraft limit: {self._overdraft_limit}'

 
# B. Now create a Bank class, an object of which contains an array of Account objects. 
#    Accounts in the array could be instances of the Account class, the SavingsAccount class, or the CurrentAccount class. 
#    Create some test accounts (some of each type).

# C. Write an update method in the Bank class. It iterates through each account, 
#    updating it in the following ways: Savings accounts get interest added (via the method you already wrote); 
#    CurrentAccounts get a letter sent if they are in overdraft. (use print to 'send' the letter).

# D. The Bank class requires methods for opening and closing accounts, and for paying a dividend into each account.

class Bank:
    def __init__(self):
        self.accounts = []  # Масив об'єктів рахунків    
    
    def add_account(self, account):
        self.accounts.append(account)  # Додавання рахунку до масиву

    def remove_account(self, account):
        self.accounts.remove(account)  # Видалення рахунку з масиву
        
    def pay_dividend(self, amount):
        total_accounts = len(self.accounts)
        dividend_per_account = amount / total_accounts   # Внесення дивіденду на рахунок
        
        for account in self.accounts:
            account.deposit(dividend_per_account)
            print(f'Dividend of {dividend_per_account} paid into account {account.get_account_number()}.')
        
    def display_accounts(self):
        for account in self.accounts:
            print(account)  # Виведення деталей кожного рахунку
            
    def update_accounts(self):
        for account in self.accounts:
            if isinstance(account, SavingsAccount):
                account.add_interest  # Додавання відсотків до зберігаючих рахунків
            elif isinstance(account, CurrentAccount):
                if account.get_balance() < 0:
                    print(f'Sending letter to account {account.get_account_number()}')  # Відправлення листа про перевищення кредитного ліміту

# Створення тестових рахунків
savings_account = SavingsAccount(1000.0, "SA001", 0.05)  
current_account = CurrentAccount(5000.0, "CA001", 1000.0)  
normal_account = Account(2000.0, "NA001")  
current_account1 = CurrentAccount(-500, "CA001", 1000.0)  
# Створення об'єкта Bank
bank = Bank()

# Додавання рахунків до банку
bank.add_account(savings_account)
bank.add_account(current_account)
bank.add_account(normal_account)
bank.add_account(current_account1)

# Виведення всіх рахунків у банку
bank.display_accounts()

# Оновлення рахунків
bank.update_accounts()
