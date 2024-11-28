class CustomerRepository:
    def __init__(self):
        self.customers = set()  
    
    def add_customer(self, customer):
        self.customers.add(customer.get_customer())
    
    def remove_customer(self, customer_id):
        to_remove = None
        for customer in self.customers:
            if customer[0] == customer_id:
                to_remove = customer
                break
        if to_remove:
            self.customers.remove(to_remove)
        else:
            raise ValueError("Customer not found")
    
    def get_customers(self):
        return self.customers
    
    def update_customer(self, new_customer):
        old_customer = None
        for customer in self.customers:
            if customer[0] == new_customer.get_id():
                old_customer = customer
                break
        if old_customer:
            self.customers.remove(old_customer)
            self.customers.add(new_customer.get_customer())
        else:
            raise ValueError("Customer not found")
