import unittest
from population import City_country

class test_population(unittest.TestCase):
    """ Thist test both cases of population and without population"""

    def test_city_name(self):

        city_name = City_country("accra","ghana")
        self.assertEqual("Accra, Ghana", city_name)

    def test_city_population(self):
        city_name_population = City_country("accra","ghana",23000000)
        self.assertEqual("Accra, Ghana: 23000000", city_name_population)

unittest.main()
