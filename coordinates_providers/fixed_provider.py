from .coordinate_provider import CoordinateProvider  # Importación relativa

class FixedCoordinateProvider(CoordinateProvider):
    def get_coordinates(self, city, country):
        return -12.0600, -77.0428  # Ejemplo: coordenadas fijas de Lima, Perú
