#!/usr/bin/env python
import random
from statistics import mean

from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    products = []
    product_names = []
    for name in range(0, num_products):
        product_names.append(f'{random.choice(ADJECTIVES)} {random.choice(NOUNS)}')
    for product in product_names:
        x = Product(product)
        x.price = random.randint(5, 100)
        x.weight = random.randint(5, 100)
        x.flammability = random.uniform(0.0, 2.5)
        products.append(x)
    return products


def inventory_report(products):
    list_products = []
    list_prices = []
    list_weights = []
    list_flammability = []
    for product in products:
        list_products.append(product.name)
        list_product = set(list_products)
        list_prices.append(product.price)
        list_weights.append(product.weight)
        list_flammability.append(product.flammability)
    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print(f'Unique product names:', len(list_product))
    print(f'Average price:', mean(list_prices))
    print(f'Average weight:', mean(list_weights))
    print(f'Average flammability', mean(list_flammability))


test_list_product = generate_products()
inventory_report(test_list_product)
