class Bill:
    def __init__(self, limiting_amount):
        self.limiting_amount = limiting_amount  # bill limit
        self.current_debt = 0  # initial debt

    # Check if limit is exceeded
    def check(self, amount):
        return (self.current_debt + amount) <= self.limiting_amount

    # Add amount to debt
    def add(self, amount):
        if self.check(amount):
            self.current_debt += amount
        else:
            print(f"Limit exceeded! Unable to add {amount} to the bill.")

    # Pay the debt
    def pay(self, amount):
        self.current_debt -= amount
        if self.current_debt < 0:
            self.current_debt = 0

    # Change bill limit
    def change_limit(self, new_limit):
        self.limiting_amount = new_limit

    # Getter methods for current debt and limit
    def get_current_debt(self):
        return self.current_debt

    def get_limiting_amount(self):
        return self.limiting_amount



class Operator:
    def __init__(self, ID, talking_charge, message_cost, network_charge, discount_rate):
        self.ID = ID
        self.talking_charge = talking_charge
        self.message_cost = message_cost
        self.network_charge = network_charge
        self.discount_rate = discount_rate

    # Calculate talking cost
    def calculate_talking_cost(self, minute, customer):
        cost = minute * self.talking_charge
        # Apply discount for customers younger than 18 or older than 65
        if customer.age < 18 or customer.age > 65:
            cost *= (1 - self.discount_rate / 100)
        return cost

    # Calculate message cost
    def calculate_message_cost(self, quantity, customer, other):
        cost = quantity * self.message_cost
        # Apply discount if both customers use the same operator
        if customer.operator.ID == other.operator.ID:
            cost *= (1 - self.discount_rate / 100)
        return cost

    # Calculate internet cost
    def calculate_network_cost(self, amount):
        return amount * self.network_charge



class Customer:
    def __init__(self, ID, name, age, operator, bill, limiting_amount):
        self.ID = ID
        self.name = name
        self.age = age
        self.operator = operator
        self.bill = bill
        self.limiting_amount = limiting_amount

    # Talk method
    def talk(self, minute, other):
        cost = self.operator.calculate_talking_cost(minute, self)
        if self.bill.check(cost):
            self.bill.add(cost)
            print(f"{self.name} talked to {other.name} for {minute} minutes. Cost: {cost}.")
        else:
            print(f"Not enough balance for a {minute}-minute call.")

    # Message method
    def message(self, quantity, other):
        cost = self.operator.calculate_message_cost(quantity, self, other)
        if self.bill.check(cost):
            self.bill.add(cost)
            print(f"{self.name} sent {quantity} messages to {other.name}. Cost: {cost}.")
        else:
            print(f"Not enough balance to send {quantity} messages.")

    # Internet connection method
    def connection(self, amount):
        cost = self.operator.calculate_network_cost(amount)
        if self.bill.check(cost):
            self.bill.add(cost)
            print(f"{self.name} used {amount} MB of internet. Cost: {cost}.")
        else:
            print(f"Not enough balance to use {amount} MB of internet.")

    # Getters and setters for age, operator, and bill
    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_operator(self):
        return self.operator

    def set_operator(self, operator):
        self.operator = operator

    def get_bill(self):
        return self.bill

    def set_bill(self, bill):
        self.bill = bill



def main():
    # Create operators
    operator1 = Operator(0, 0.5, 0.2, 0.1, 10)
    operator2 = Operator(1, 0.6, 0.3, 0.15, 15)

    # Create customers
    bill1 = Bill(100)
    customer1 = Customer(0, "Ivan", 20, operator1, bill1, 100)

    bill2 = Bill(200)
    customer2 = Customer(1, "Anna", 70, operator2, bill2, 200)

    # Customers interact
    customer1.talk(10, customer2)
    customer1.message(5, customer2)
    customer1.connection(50)

    # Pay bills
    customer1.bill.pay(50)
    print(f"Current debt of {customer1.name}: {customer1.bill.get_current_debt()}")

if __name__ == "__main__":
    main()

