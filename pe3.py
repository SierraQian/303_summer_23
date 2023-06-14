# Pair Exercise 3
# encode, decode, class

import string
# Encode
def encode(input_text, shift):
    list_alphabet = [chr(ord('a') + i) for i in range(26)]

    result_alphabet = []
    input_text = input_text.lower()
    for alphabet in input_text:
        if alphabet not in list_alphabet:
            shift_alphabet = alphabet
            result_alphabet.append(shift_alphabet)
        else:

            shift_alphabet = list_alphabet[(list_alphabet.index(alphabet) + shift) % 26]
            result_alphabet.append(shift_alphabet)

    result_alphabet = ''.join(result_alphabet)

    return (list_alphabet, result_alphabet)

# print(encode("a", 3)) #should return (["a", "b", ... "z"], "d")
# print(encode("abc", 4)) #should return (["a", "b", ... "z"], "efg")
# print(encode("xyz", 3)) #should return (["a", "b", ... "z"], "abc")
# print(encode("j!K,2?", 3)) #should return (["a", "b", ... "z"], "m!n,2?")

# Decode
def decode(input_text, shift):
    list_alphabet = [chr(ord('a') + i) for i in range(26)]

    result_alphabet = []
    input_text = input_text.lower()
    for alphabet in input_text:
        if alphabet not in list_alphabet:
            shift_alphabet = alphabet
            result_alphabet.append(shift_alphabet)
        else:

            shift_alphabet = list_alphabet[(list_alphabet.index(alphabet) - shift + 26) % 26]
            result_alphabet.append(shift_alphabet)

    result_alphabet = ''.join(result_alphabet)

    return result_alphabet

# print(decode("d", 3)) #should return "a"
# print(decode("efg", 4)) #should return "abc"
# print(decode("abc", 3)) #should return "xyz"
# print(decode("m!n,2?", 3)) #should return "j!K,2?"

# Class

import datetime

# Creation date in the future, raise an exception
class BankAccountExceptions(Exception):
    pass
class BankAccount():
    def __init__(self, name = 'Clocks', ID = '123', creation_date = datetime.date.today(), balance = 0):
        if not isinstance(creation_date, datetime.date):
            raise BankAccountExceptions("Creation date should be the type of datetime.date.")
        self.name = name
        self.ID = ID
        # change creation_date format
        self.creation_date = creation_date
        self.balance = balance
        # self date validation when get arguments
        self.creation_date_validation()

    def creation_date_validation(self):
        current_date = datetime.date.today()
        if self.creation_date > current_date:
            raise BankAccountExceptions("Creation date cannot be a future date.")

    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount
        # else:
        #     self.balance = self.balance
        #     raise BankAccountExceptions("Deposit amount should be positive.")
        return self.balance

    def withdraw(self, amount):
        if amount >= 0:
            self.balance -= amount
        return self.balance

    def view_balance(self):
        return self.balance

class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        one_day = datetime.timedelta(days=1)
        if datetime.date.today() + one_day * 30 * 6 >= self.current_date and self.balance - amount >= 0 and amount >= 0:
            self.balance -= amount
        # else:
        #     self.balance = self.balance
        #     raise BankAccountExceptions("Withdrawals not allowed. "
        #                     "Please make sure you create account 6 month before "
        #                     "or you have sufficient mount in your account.")
        return self.balance

class CheckingAccount(BankAccount):
    def withdraw(self, amount):
        if self.balance - amount >= 0 and amount >= 0:
            self.balance -= amount
        else:
            self.balance -= amount + 30
            # raise BankAccountExceptions("Insufficient balance. Overdraft fee charged.")
        return self.balance