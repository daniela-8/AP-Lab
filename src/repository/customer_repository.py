class CustomerRepository:
    def __init__(self):
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def remove_customer(self, customer_id):
        for customer in self.customers:
            if customer.customer_id == customer_id:
                self.customers.remove(customer)
                return
        raise ValueError("Customer not found")

    def get_customers(self):
        return self.customers

    def update_customer(self, new_customer):
        for idx, customer in enumerate(self.customers):
            if customer.customer_id == new_customer.customer_id:
                self.customers[idx] = new_customer
                return
        raise ValueError("Customer not found")

    def __str__(self):
        return '\n'.join(str(customer) for customer in self.customers)
