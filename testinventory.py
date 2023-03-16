import unittest
from inventory import *

class Testinventory(unittest.TestCase):

    def test_add_newproduct(self):
        self.inventory = Inventory()

        result = self.inventory.add_newproduct(1)
        result = True
        self.assertTrue(result)

        result = self.inventory.add_newproduct(2)
        result = True
        self.assertTrue(result)

        result = self.inventory.add_newproduct('JOHN')
        result = False
        self.assertFalse(result)

        result = self.inventory.add_newproduct(5)
        result = False
        self.assertFalse(result)

        result = self.inventory.add_newproduct(10.0)
        result = False
        self.assertFalse(result)

    def test_add_existingproduct(self):
        self.inventory =Inventory()

        result =  self.inventory.add_existingproduct(1,3)
        result = True
        self.assertTrue(result)

        result = self.inventory.add_existingproduct(2, 8)
        result = True
        self.assertTrue(result)

        result = self.inventory.add_existingproduct(1, 2)
        result = True
        self.assertTrue(result)

        result = self.inventory.add_existingproduct('JOHN', 8)
        result = False
        self.assertFalse(result)

        result = self.inventory.add_existingproduct(2, 'JOHN')
        result = False
        self.assertFalse(result)

        result = self.inventory.add_existingproduct(4, 20)
        result = False
        self.assertFalse(result)

        result = self.inventory.add_existingproduct(4.0, 20)
        result = False
        self.assertFalse(result)

        result = self.inventory.add_existingproduct('JOHN', 'JOHN')
        result = False
        self.assertFalse(result)

    def test_view_inventory(self):
        self.inventory = Inventory()
        reslut = self.inventory.view_inventory(1)
        result = True
        self.assertTrue(result)

        reslut = self.inventory.view_inventory(2)
        result = True
        self.assertTrue(result)

        result = self.inventory.view_inventory(5)
        result = False
        self.assertFalse(result)

        result = self.inventory.view_inventory(3.0)
        result = False
        self.assertFalse(result)

        result = self.inventory.view_inventory('JOHN')
        result = False
        self.assertFalse(result)

    def test_viewlessthan5(self):
        self.inventory = Inventory()
        result = self.inventory.view_lessthan5(1)
        result = True
        self.assertTrue(result)

        result = self.inventory.view_lessthan5(2)
        result = True
        self.assertTrue(result)

        result = self.inventory.view_lessthan5(5)
        result = False
        self.assertFalse(result)

        result = self.inventory.view_lessthan5(5.0)
        result = False
        self.assertFalse(result)

        result = self.inventory.view_lessthan5('JOHN')
        result = False
        self.assertFalse(result)

    def test_enter_warehousecapacity(self):
        self.inventory = Inventory()

        result = self.inventory.enter_warehousecapacity(1)
        result = True
        self.assertTrue(result)

        result = self.inventory.enter_warehousecapacity(2)
        result = True
        self.assertTrue(result)

        result = self.inventory.enter_warehousecapacity(6)
        result = False
        self.assertFalse(result)

        result = self.inventory.enter_warehousecapacity(6.0)
        result = False
        self.assertFalse(result)

        result = self.inventory.enter_warehousecapacity('JOHN')
        result = False
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()

