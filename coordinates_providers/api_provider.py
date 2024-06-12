import requests
from .coordinate_provider import CoordinateProvider  # Importación relativa

class APICoordinateProvider(CoordinateProvider):
    def get_coordinates(self, city):
        url = f"https://nominatim.openstreetmap.org/search?q={city}&format=json"
        response = requests.get(url)
      
        
        if response.status_code == 200:
            data = response.json()
            if data:
                return float(data[0]['lat']), float(data[0]['lon'])
            else:
                raise ValueError("La respuesta de la API está vacía")
        else:
            raise ValueError(f"Error al hacer la solicitud a la API: {response.status_code}")
