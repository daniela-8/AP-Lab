# domain/customer.py

class Customer:
    def __init__(self, customer_id, name, CNP):
        self._customer_id = customer_id
        self._name = name
        self._CNP = CNP

    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, value):
        if not isinstance(value, int):
            raise ValueError("Customer ID must be an integer.")
        self._customer_id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty.")
        self._name = value

    @property
    def CNP(self):
        return self._CNP

    @CNP.setter
    def CNP(self, value):
        if not isinstance(value, int):
            raise ValueError("CNP must be an integer.")
        self._CNP = value

    def __str__(self):
        return f"Id: {self.customer_id}, Name: {self.name}, CNP: {self.CNP}"
