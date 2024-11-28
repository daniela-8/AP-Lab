
class CustomerRepository:
    def __init__(self):
        self.customers= []

    def add_customer(self, customer):
        self.customers.append(customer)

    def remove_customer(self, customer):
        self.customers.remove(customer)

    def get_customers(self):
        return self.customers

    def update_customer(self, new_customer):
        for customer in self.customers:
            if customer.get_id() == new_customer.get_id():
                customer.set_name(new_customer.get_name())
                customer.set_CNP(new_customer.get_CNP())
