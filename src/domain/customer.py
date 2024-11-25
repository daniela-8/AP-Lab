
class Customer:
    def __init__(self, id, name, CNP):
        self.id = id
        self.name = name
        self.CNP = CNP

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_CNP(self):
        return self.CNP

    def set_CNP(self, CNP):
        self.CNP = CNP

    def set_name(self, name):
        self.name = name

    def set_id(self, id):
        self.id = id

    def __str__(self):
        return f"Id: {self.id}, Name: {self.name}, CNP: {self.CNP}"


