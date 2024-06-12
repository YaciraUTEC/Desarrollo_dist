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
        print("Elección inválida")
        return

    if choice == '2':
        city1 = input("Introduce el nombre de la primera ciudad (por ejemplo, Lima): ")
        city2 = input("Introduce el nombre de la segunda ciudad (por ejemplo, Bogota): ")
        city3 = input("Introduce el nombre de la tercera ciudad (por ejemplo, Buenos Aires): ")
    else:
        city1_country1 = input("Introduce el nombre de la primera ciudad y su país separados por una coma (por ejemplo, Lima, Peru): ")
        city2_country2 = input("Introduce el nombre de la segunda ciudad y su país separados por una coma (por ejemplo, Bogota, Colombia): ")
        city3_country3 = input("Introduce el nombre de la tercera ciudad y su país separados por una coma (por ejemplo, Buenos Aires, Argentina): ")

        city1, country1 = map(str.strip, city1_country1.split(','))
        city2, country2 = map(str.strip, city2_country2.split(','))
        city3, country3 = map(str.strip, city3_country3.split(','))

    try:
        if choice == '2':
            coord1 = provider.get_coordinates(city1)
            coord2 = provider.get_coordinates(city2)
            coord3 = provider.get_coordinates(city3)
        else:
            coord1 = provider.get_coordinates(city1, country1)
            coord2 = provider.get_coordinates(city2, country2)
            coord3 = provider.get_coordinates(city3, country3)
        
        distance1_2 = haversine_distance(coord1, coord2)
        distance1_3 = haversine_distance(coord1, coord3)
        distance2_3 = haversine_distance(coord2, coord3)

        print(f"La distancia entre {city1} y {city2} es de {distance1_2:.2f} km.")
        print(f"La distancia entre {city1} y {city3} es de {distance1_3:.2f} km.")
        print(f"La distancia entre {city2} y {city3} es de {distance2_3:.2f} km.")

        min_distance = min(distance1_2, distance1_3, distance2_3)
        if min_distance == distance1_2:
            closest_cities = (city1, city2)
        elif min_distance == distance1_3:
            closest_cities = (city1, city3)
        else:
            closest_cities = (city2, city3)

        print(f"Las dos ciudades más cercanas entre ellas son {closest_cities[0]} y {closest_cities[1]} con una distancia de {min_distance:.2f} km.")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
