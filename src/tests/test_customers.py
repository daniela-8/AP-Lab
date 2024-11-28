import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
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
        customer = Customer(1, "John Doe", 123456789)
        customer.set_id(2)
        customer.set_name("Jane Doe")
        customer.set_CNP(987654321)
        self.assertEqual(customer.get_id(), 2)
        self.assertEqual(customer.get_name(), "Jane Doe")
        self.assertEqual(customer.get_CNP(), 987654321)

    def test_customer_get_customer(self):
        customer = Customer(1, "John Doe", 123456789)
        self.assertEqual(customer.get_customer(), (1, "John Doe", 123456789))

class TestCustomerRepository(unittest.TestCase):

    def setUp(self):
        self.repository = CustomerRepository()

    def test_add_customer(self):
        customer = Customer(1, "John Doe", 123456789)
        self.repository.add_customer(customer)
        self.assertIn(customer.get_customer(), self.repository.get_customers())

    def test_remove_customer(self):
        customer = Customer(1, "John Doe", 123456789)
        self.repository.add_customer(customer)
        self.repository.remove_customer(1)
        self.assertNotIn(customer.get_customer(), self.repository.get_customers())

    def test_update_customer(self):
        customer = Customer(1, "John Doe", 123456789)
        self.repository.add_customer(customer)
        updated_customer = Customer(1, "Jane Doe", 987654321)
        self.repository.update_customer(updated_customer)
        customers = self.repository.get_customers()
        self.assertIn(updated_customer.get_customer(), customers)

class TestCustomerService(unittest.TestCase):

    def setUp(self):
        self.repository = CustomerRepository()
        self.service = CustomerService(self.repository)

    def test_add_customer_success(self):
        self.service.add_customer(1, "John Doe", 123456789)
        customers = self.service.get_customers()
        self.assertIn((1, "John Doe", 123456789), customers)

    def test_add_customer_duplicate_id(self):
        self.service.add_customer(1, "John Doe", 123456789)
        with self.assertRaises(ValueError):
            self.service.add_customer(1, "Jane Doe", 987654321)

    def test_delete_customer_success(self):
        self.service.add_customer(1, "John Doe", 123456789)
        self.service.delete_customer(1)
        customers = self.service.get_customers()
        self.assertNotIn((1, "John Doe", 123456789), customers)

    def test_delete_customer_not_found(self):
        with self.assertRaises(ValueError):
            self.service.delete_customer(99)

    def test_update_customer_success(self):
        self.service.add_customer(1, "John Doe", 123456789)
        self.service.update_customer(1, "Jane Doe", 987654321)
        customers = self.service.get_customers()
        self.assertIn((1, "Jane Doe", 987654321), customers)

    def test_update_customer_not_found(self):
        with self.assertRaises(ValueError):
            self.service.update_customer(99, "Jane Doe", 987654321)

    def test_search_customers_by_name(self):
        self.service.add_customer(1, "John Doe", 123456789)
        self.service.add_customer(2, "Jane Smith", 987654321)
        matched_customers = self.service.search_customers_by_name("Jane")
        self.assertEqual(len(matched_customers), 1)
        self.assertEqual(matched_customers[0][1], "Jane Smith")

    def test_sort_customers_by_CNP(self):
        self.service.add_customer(1, "John Doe", 987654321)
        self.service.add_customer(2, "Jane Smith", 123456789)
        sorted_customers = self.service.sort_customers_by_CNP()
        self.assertEqual(sorted_customers[0][2], 123456789)
        self.assertEqual(sorted_customers[1][2], 987654321)
        
    def test_customer_comparison(self):
        customer1 = Customer(1, "Alice", 1234)
        customer2 = Customer(2, "Bob", 5678)
        self.assertTrue(customer1 < customer2)
        self.assertFalse(customer1 > customer2)
        customer3 = Customer(3, "Charlie", 1234)
        self.assertFalse(customer1 < customer3)
        self.assertFalse(customer1 > customer3)

if __name__ == "__main__":
    unittest.main()
