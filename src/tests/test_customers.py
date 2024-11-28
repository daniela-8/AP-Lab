import unittest
from termios import IXANY

from domain.customer import Customer
from repository.customer_repository import CustomerRepository
from operations.operations import CustomerService


class TestCustomer(unittest.TestCase):

    def test_customer_initialization(self):
        customer = Customer(1, "John Doe", 123456789)
        self.assertEqual(customer.get_id(), 1)
        self.assertEqual(customer.get_name(), "John Doe")
        self.assertEqual(customer.get_CNP(), 123456789)

    def test_customer_setters(self):
        customer = Customer(1, "Floricica Rodi", 123456789)
        customer.set_id(2)
        customer.set_name("Jane Doe")
        customer.set_CNP(987654321)
        self.assertEqual(customer.get_id(), 2)
        self.assertEqual(customer.get_name(), "Jane Doe")
        self.assertEqual(customer.get_CNP(), 987654321)

    def test_customer_str(self):
        customer = Customer(1, "Floricica Rodi", 123456789)
        self.assertEqual(str(customer), "Id: 1, Name: Floricica Rodi, CNP: 123456789")


class TestCustomerRepository(unittest.TestCase):

    def setUp(self):
        self.repository = CustomerRepository()

    def test_add_customer(self):
        customer = Customer(1, "Floricica Rodi", 123456789)
        self.repository.add_customer(customer)
        self.assertIn(customer, self.repository.get_customers())

    def test_remove_customer(self):
        customer = Customer(1, "Floricica Rodi", 123456789)
        self.repository.add_customer(customer)
        self.repository.remove_customer(customer)
        self.assertNotIn(customer, self.repository.get_customers())

    def test_update_customer(self):
        customer = Customer(1, "Floricica Rodi", 123456789)
        self.repository.add_customer(customer)
        updated_customer = Customer(1, "Jane Doe", 987654321)
        self.repository.update_customer(updated_customer)
        customers = self.repository.get_customers()
        self.assertEqual(customers[0].get_name(), "Jane Doe")
        self.assertEqual(customers[0].get_CNP(), 987654321)


class TestCustomerService(unittest.TestCase):

    def setUp(self):
        self.repository = CustomerRepository()
        self.service = CustomerService(self.repository)

    def test_add_customer_success(self):
        self.service.add_customer(1, "Floricica Rodi", 123456789)
        customers = self.service.print_customers()
        self.assertIn("Id: 1, Name: Floricica Rodi, CNP: 123456789", customers)

    def test_add_customer_duplicate_id(self):
        self.service.add_customer(1, "Floricica Rodi", 123456789)
        with self.assertRaises(ValueError):
            self.service.add_customer(1, "Jane Doe", 987654321)

    def test_delete_customer_success(self):
        self.service.add_customer(1, "Floricica Rodi", 123456789)
        self.service.delete_customer(1)
        customers = self.service.print_customers()
        self.assertNotIn("Id: 1, Name: Floricica Rodi, CNP: 123456789", customers)

    def test_delete_customer_not_found(self):
        with self.assertRaises(ValueError):
            self.service.delete_customer(99)

    def test_update_customer_success(self):
        self.service.add_customer(1, "Floricica Rodi", 123456789)
        self.service.update_customer(1, "Varu Sandel", 987654321)
        customers = self.service.print_customers()
        self.assertIn("Id: 1, Name: Varu Sandel, CNP: 987654321", customers)

    def test_update_customer_not_found(self):
        with self.assertRaises(ValueError):
            self.service.update_customer(99, "Varu Sandel", 987654321)


if __name__ == "__main__":
    unittest.main()
