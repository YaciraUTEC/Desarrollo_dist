import requests
from .coordinate_provider import CoordinateProvider  # Importación relativa

class APICoordinateProvider(CoordinateProvider):
    def get_coordinates(self, city, country):
        url = f"https://nominatim.openstreetmap.org/search?q={city},{country}&format=json"
        response = requests.get(url)
        data = response.json()
        
        if data:
            return float(data[0]['lat']), float(data[0]['lon'])
        else:
            raise ValueError("Ciudad o país no encontrados usando la API")
