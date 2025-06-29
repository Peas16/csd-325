# Paul Fralix, 06/28/2025, Assignment 7.2

# test_cities.py

import unittest
from city_functions import city_country

class TestCityCountry(unittest.TestCase):
    """Tests for city_functions.py"""

    def test_city_country(self):
        """Test city_country function with city and country"""
        result = city_country('Santiago', 'Chile')
        self.assertEqual(result, 'Santiago, Chile')

   if __name__ == '__main__':
    unittest.main()
