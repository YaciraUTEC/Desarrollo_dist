import unittest
from coordinates_providers import CSVCoordinateProvider, APICoordinateProvider, FixedCoordinateProvider
from haversine import haversine_distance

class TestCoordinateProviders(unittest.TestCase):
    
    def setUp(self):
        self.csv_path = 'worldcities.csv'
        self.csv_provider = CSVCoordinateProvider(self.csv_path)
        self.api_provider = APICoordinateProvider()
        self.fixed_provider = FixedCoordinateProvider()
        
        self.test_city = "Lima"
        self.test_country = "Peru"
        self.test_city2 = "Cairo"
        self.test_country2 = "Egypt"
        
    # Caso de Éxito
    def test_csv_provider_success(self):
        coord1 = self.csv_provider.get_coordinates(self.test_city, self.test_country)
        coord2 = self.csv_provider.get_coordinates(self.test_city2, self.test_country2)
        distance = haversine_distance(coord1, coord2)
        self.assertIsNotNone(distance)
        self.assertGreater(distance, 0)
        
    # Caso Extremo 1: Ciudad no existente
    def test_csv_provider_city_not_found(self):
        with self.assertRaises(ValueError):
            self.csv_provider.get_coordinates("NonExistentCity", self.test_country)
    
    # Caso Extremo 2: Misma ciudad dos veces
    def test_same_city(self):
        coord = self.csv_provider.get_coordinates(self.test_city, self.test_country)
        distance = haversine_distance(coord, coord)
        self.assertEqual(distance, 0)

if __name__ == '__main__':
    unittest.main()
