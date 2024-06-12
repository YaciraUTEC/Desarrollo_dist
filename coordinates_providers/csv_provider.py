import pandas as pd
from .coordinate_provider import CoordinateProvider  # Importación relativa

class CSVCoordinateProvider(CoordinateProvider):
    def __init__(self, csv_path):
        self.data = pd.read_csv(csv_path, usecols=[0, 2, 3])  # Solo necesitamos las columnas de nombre de ciudad, latitud y longitud

    def get_coordinates(self, city, country):
        # Busca la ciudad en los datos
        city_data = self.data[self.data['city'].str.lower() == city.lower()]
        if not city_data.empty:
        # Toma solo el primer registro de la ciudad encontrada
          city_data = city_data.iloc[0]
        # Devuelve las coordenadas de la ciudad
        return float(city_data['lat']), float(city_data['lng'])
