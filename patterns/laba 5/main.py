from credit_card import CreditCard
from bank_info import BankInfo, BankCustomer, PersonalInfo
from decorators import GoldenCreditCard, VIPCustomer

# Створення об'єктів CreditCard та BankInfo
credit_card = CreditCard("John Doe", "1234567890", 5000.0, 30, "123")
bank_info = BankInfo("Sample Bank", "John Doe", ["1234567890"])

# Створення особистої інформації та BankCustomer
personal_info = PersonalInfo(name="John Doe", age=30, address="123 Main St")
customer = BankCustomer(personal_info, bank_info)

# Адаптер для CreditCard з декоратором GoldenCreditCard
golden_card = GoldenCreditCard(credit_card)
print("Golden Credit Card Details:", golden_card.give_details())

# Декоратор VIP для BankCustomer
vip_customer = VIPCustomer(customer)
print("VIP Customer Details:", vip_customer.give_details())