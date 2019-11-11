import random


class Product:

    def __init__(self, name, price=10, weight=20, flammability=0.5, identifier=random.randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier


    def stealability(self):
        """
        Calculates the price divided by the weight, and then returns a message
        """
        if self.price / self.weight < 0.5:
            return f'Not so stealable...'
        elif self.price / self.weight < 1:
            return f'Kinda stealable.'
        elif self.price / self.weight > 1:
            return f'Very stealable!'

    def explode(self):
        """
        calculates the flammability times the weight, and then returns a message

        """
        if self.flammability * self.weight < 10:
            return f"...fizzle."
        elif self.flammability * self.weight < 50:
            return f"...boom!"
        elif self.flammability * self.weight >= 50:
            return f"...BABOOM!!"


class BoxingGlove(Product):
    """BoxingGlove is a class of product."""
    def __init__(self,  weight):
        super().__init__(weight)
        self.weight = 10

    def explode(self):
        """BoxingGlove can't explode.  """
        return f"...it's a glove."

    def punch(self):
        """BoxingGlove used to provide punches.  """
        if self.weight < 5:
            return f"That tickles."
        if 15 > self.weight >= 5:
            return f"Hey that hurt!"
        if self.weight < 5:
            return f"OUCH!"