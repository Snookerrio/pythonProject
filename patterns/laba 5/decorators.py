from credit_card import CreditCard
from bank_info import BankCustomer

class GoldenCreditCard:
    def __init__(self, credit_card: CreditCard):
        self._credit_card = credit_card

    def give_details(self):
        details = self._credit_card.give_details()
        details["type"] = "Golden"
        details["benefits"] = "Exclusive benefits for Golden cardholders"
        return details


class VIPCustomer:
    def __init__(self, customer: BankCustomer):
        self._customer = customer

    def give_details(self):
        details = self._customer.give_details()
        details["type"] = "VIP"
        details["benefits"] = "Priority customer support and additional rewards"
        return details