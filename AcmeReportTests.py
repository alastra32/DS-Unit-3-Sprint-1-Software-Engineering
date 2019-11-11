#!/usr/bin/env python

import unittest
from acme_report import generate_products, inventory_report
from acme_report import generate_products, ADJECTIVES, NOUNS


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
        list_adjectives = []
        list_nouns = []
        for product in prod:
            list_adjectives.append(product.name.split(" ", expand=True)[0])
            list_nouns.append(product.name.split(" ", expand=True)[1])
        self.assertIn(list_adjectives,ADJECTIVES)
        self.assertIn(list_nouns,NOUNS))


if __name__ == '__main__':
    unittest.main()
