import random
import unittest

from acme import Product

class TestAnimal(unittest.TestCase):
    def setUp(self):
        self.name='A Cool Toy'
        self.prod = Product(name)


if __name__ == '__main__':
    unittest.main()
