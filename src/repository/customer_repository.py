
class CustomerRepository:
    def __init__(self):
        self.customers= []

    def add_customer(self, customer):
        self.customers.append(customer)

    def remove_customer(self, customer):
        self.customers.remove(customer)

    def get_customers(self):
        return self.customers
