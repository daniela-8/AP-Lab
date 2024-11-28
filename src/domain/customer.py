class Customer:
    def __init__(self, customer_id, name, CNP):
        self.customer = (customer_id, name, CNP)
    
    def get_id(self):
        return self.customer[0]
    
    def get_name(self):
        return self.customer[1]
    
    def get_CNP(self):
        return self.customer[2]
    
    def set_id(self, new_id):
        self.customer = (new_id, self.customer[1], self.customer[2])
    
    def set_name(self, new_name):
        self.customer = (self.customer[0], new_name, self.customer[2])
    
    def set_CNP(self, new_CNP):
        self.customer = (self.customer[0], self.customer[1], new_CNP)
    
    def get_customer(self):
        return self.customer
    
    def __len__(self):
        return len(self.get_name())
    
    def __str__(self):
        return f"Id: {self.customer[0]}, Name: {self.customer[1]}, CNP: {self.customer[2]}"
