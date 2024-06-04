import pandas as pd
from .coordinate_provider import CoordinateProvider  # Importación relativa

class CSVCoordinateProvider(CoordinateProvider):
    def __init__(self, csv_path):
        self.data = pd.read_csv(csv_path)

    def get_coordinates(self, city, country):
        result = self.data[(self.data['city'].str.lower() == city.lower()) & 
                           (self.data['country'].str.lower() == country.lower())]
        if not result.empty:
            return result.iloc[0]['lat'], result.iloc[0]['lng']
        else:
            raise ValueError("Ciudad o país no encontrados en el CSV")
