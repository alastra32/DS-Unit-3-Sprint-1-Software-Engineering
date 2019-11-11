#!/usr/bin/env python

import unittest

from acme_report import generate_products


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products and reports are the tops!"""

    def test_default_num_products(self):
        """Test  checks that it really does receive a list of length 30"""
        prod = generate_products()
        self.assertEqual(len(prod), 30)

    def test_legal_names(self):
        """ checks that the generated names for a default batch of products are all valid possible names to generate"""
        prod = generate_products()
        ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
        NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']
        for product in prod:
            self.assertIn(product.name.split(" ")[0], ADJECTIVES)
            self.assertIn(product.name.split(" ")[1], NOUNS)


if __name__ == '__main__':
    unittest.main()
