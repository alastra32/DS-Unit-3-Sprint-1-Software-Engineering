#!/usr/bin/env python

import unittest

from acme import Product


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""

    def setUp(self):
        """setup for default values"""
        self.prod = Product('Test Product')

    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_stealability(self):
        """Test default stealability works as expected."""
        self.assertEqual(self.prod.stealability, f"Kinda stealable.")

    def test_explode(self):
        """Test default explode works as expected."""
        self.assertEqual(self.prod.explode(), f"...boom!")


if __name__ == '__main__':
    unittest.main()
