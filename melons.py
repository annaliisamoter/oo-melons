"""Classes for melon orders."""

import random
import datetime


class TooManyMelonsError(ValueError):
    """Catches orders greater than 100 and flags them"""


class AbstractMelonOrder(object):
    """General Melon order class"""


    def __init__(self, species, qty):
        """Initialize melon order attributes"""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.time_of_order = datetime.datetime.now()
        if self.qty > 100:
            raise TooManyMelonsError('Too many melons!')

    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_base_price()
        if self.species == "christmas melon":
            base_price = base_price * 1.5

        total = ((1 + self.tax) * self.qty * base_price)

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    def get_base_price(self):
        """Implements random "Splurge Pricing" base price"""

        base_price = random.randint(5, 9)
        week_day = datetime.datetime.weekday(self.time_of_order)
        hour = self.time_of_order.hour

        if week_day in range(0, 5) and hour in range(8, 11):
            base_price = base_price + 4

        return base_price


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = 'Domestic'
    tax = 0.08

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super(DomesticMelonOrder, self).__init__(species, qty)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = 'International'
    tax = 0.17

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super(InternationalMelonOrder, self).__init__(species, qty)

        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def get_total(self):
        total = super(InternationalMelonOrder, self).get_total()
        if self.qty < 10:
            total = total + 3
        return total


class GovernmentMelonOrder(AbstractMelonOrder):
    """Melon order from the government."""

    order_type = 'Government'
    tax = 0.00

    def __init__(self, species, qty):
        """Initializes melon order attributes"""
        super(GovernmentMelonOrder, self).__init__(species, qty)

        self.passed_inspection = False

    def mark_inspection(self, passed):
        """Marks order as having passed inspection"""
        if passed is True:
            self.passed_inspection = True


