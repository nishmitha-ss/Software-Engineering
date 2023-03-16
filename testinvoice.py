import unittest
from invoice import *

class Testinvoice(unittest.TestCase):
    def test_create_invoice(self):
        self.invoice = Invoice()
        result = self.invoice.create_invoice('JOHN',  6)
        result = True
        self.assertTrue(result)

        result = self.invoice.create_invoice('JOHN',  8)
        result = True
        self.assertTrue(result)

        result = self.invoice.create_invoice('EMILY',  1)
        result = True
        self.assertTrue(result)

        result = self.invoice.create_invoice(1,1)
        result = False
        self.assertFalse(result)

        result = self.invoice.create_invoice(1,'JOHN')
        result = False
        self.assertFalse(result)

        result = self.invoice.create_invoice('JOHN','JOHN')
        result = False
        self.assertFalse(result)

        result = self.invoice.create_invoice('JOHN', 1.0)
        result = False
        self.assertFalse(result)

        result = self.invoice.create_invoice('JOHN', '2')
        result = False
        self.assertFalse(result)

        result = self.invoice.create_invoice('JOHN', 100)
        result = False
        self.assertFalse(result)


    def test_update_invoice(self):
        self.invoice = Invoice()

        result = self.invoice.update_invoice(1)
        result = True
        self.assertTrue(result)

        result = self.invoice.update_invoice(2)
        result = True
        self.assertTrue(result)

        result = self.invoice.update_invoice('JOHN')
        result = False
        self.assertFalse(result)

        result = self.invoice.update_invoice(100)
        result = False
        self.assertFalse(result)

        result = self.invoice.update_invoice(100.89)
        result = False
        self.assertFalse(result)

    def test_open_invoice(self):
        self.invoice = Invoice()
        reslut = self.invoice.open_invoice()
        result = True
        self.assertTrue(result)

    def test_close_invoice(self):
        self.invoice = Invoice()
        reslut = self.invoice.close_invoice()
        result = True
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()