from coordinates_providers import CSVCoordinateProvider, APICoordinateProvider, FixedCoordinateProvider
from haversine import haversine_distance

def main():
    print("Seleccione la fuente de coordenadas:")
    print("1. CSV")
    print("2. API")
    print("3. Fijo")
    choice = input("Ingrese su elección (1/2/3): ")

    if choice == '1':
        csv_path = 'worldcities.csv'  # Ruta al archivo CSV
        provider = CSVCoordinateProvider(csv_path)
    elif choice == '2':
        provider = APICoordinateProvider()
    elif choice == '3':
        provider = FixedCoordinateProvider()
    else:
        print("Elección no válida")
        return

    city1 = input("Introduce el nombre de la primera ciudad: ")
    country1 = input("Introduce el nombre del país de la primera ciudad: ")
    city2 = input("Introduce el nombre de la segunda ciudad: ")
    country2 = input("Introduce el nombre del país de la segunda ciudad: ")

    try:
        coord1 = provider.get_coordinates(city1, country1)
        coord2 = provider.get_coordinates(city2, country2)
        distance = haversine_distance(coord1, coord2)
        print(f"La distancia entre {city1}, {country1} y {city2}, {country2} es de {distance:.2f} km.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
