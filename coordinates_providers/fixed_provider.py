from .coordinate_provider import CoordinateProvider  # Importación relativa

class FixedCoordinateProvider(CoordinateProvider):
    def __init__(self):
        # Define las coordenadas fijas para algunas ciudades
        self.fixed_coordinates = {
            'Lima, Peru': (-12.0464, -77.0428),
            'Bogota, Colombia': (4.7110, -74.0721),
            'Buenos Aires, Argentina': (-34.6037, -58.3816)
            # Puedes agregar más ciudades y sus coordenadas aquí si lo deseas
        }

    def get_coordinates(self, city, country):
        # Comprueba si las coordenadas para la ciudad dada están disponibles
         city_country = f"{city}, {country}"
    # Comprueba si las coordenadas para la ciudad dada están disponibles
         if city_country in self.fixed_coordinates:
             return self.fixed_coordinates[city_country]
         
         else:
            raise ValueError("Coordenadas para la ciudad no encontradas en el proveedor fijo")