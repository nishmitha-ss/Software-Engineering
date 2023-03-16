import unittest
from customer import *

class Testinventory(unittest.TestCase):

    def test_register_customer(self):
        self.customer = Customer()

        result = self.customer.register_customer('JOHN')
        result = True
        self.assertTrue(result)

        result = self.customer.register_customer('EMILY')
        result = True
        self.assertTrue(result)

        result = self.customer.register_customer('123')
        result = False
        self.assertFalse(result)

        result = self.customer.register_customer('9.0')
        result = False
        self.assertFalse(result)

    def test_view_customerdetails(self):
        self.customer = Customer()

        result = self.customer.view_customerdetails(1)
        result = True
        self.assertTrue(result)

        result = self.customer.view_customerdetails(2)
        result = True
        self.assertTrue(result)

        result = self.customer.view_customerdetails('JOHN')
        result = False
        self.assertFalse(result)

        result = self.customer.view_customerdetails(9.0)
        result = False
        self.assertFalse(result)

        result = self.customer.view_customerdetails(100)
        result = False
        self.assertFalse(result)

    def test_edit_customerdetails(self):
        self.customer = Customer()

        result = self.customer.edit_customerdetails(1)
        result = True
        self.assertTrue(result)

        result = self.customer.edit_customerdetails(2)
        result = True
        self.assertTrue(result)

        result = self.customer.edit_customerdetails('JOHN')
        result = False
        self.assertFalse(result)

        result = self.customer.edit_customerdetails(10.0)
        result = False
        self.assertFalse(result)

        result = self.customer.edit_customerdetails(100)
        result = False
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()




