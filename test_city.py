import unittest
from city_function import City_country

class test_city_case(unittest.TestCase):

    def test_city_name(self):
        # i have to use assertions

        city_name = City_country("accra", "ghana")
        self.assertEqual("Accra, Ghana", city_name)

unittest.main()
