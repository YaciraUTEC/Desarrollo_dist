# Actividad: Calcular Distancia entre Ciudades

### Descripción
Este proyecto implementa un programa que recibe como entrada los nombres de dos ciudades y sus respectivos países, y devuelve la distancia entre ellas.

### Implementar un Servicio
Este servicio debe devolver la latitud y longitud de las ciudades utilizando tres formas diferentes y hacer un switch utilizando interfaces.

### Formas de Implementación

1. **Lectura desde un archivo CSV** (`worldcities.csv`).
2. **Uso de una API**: `https://nominatim.openstreetmap.org/search?q=lima,peru&format=json`.
3. **Valores fijos** (opcional).

### Método de Cálculo de Distancia

El archivo `haversine.py` contiene la implementación del método para calcular la distancia entre dos puntos en la superficie de la Tierra dados sus latitudes y longitudes. Este método se basa en la fórmula de Haversine, que es una ecuación importante en la navegación y la geodesia para encontrar la distancia entre dos puntos en una esfera, dada su longitud y latitud

-----------------------------------------------------------
### Cambios solicitados en otro git  
1. Implementar, en un nuevo Branch (checkout —b) un cambio en el código del repositorio de su compañero con un nuevo **endpoint/opción** de interfaz que reciba tres nombres de ciudad e indique cuales dos se encuentran más cerca (menor distancia en km).
Ejemplo: Lima, Bogota, Buenos Aires, ***Deberia retomar Lima***.
2. Realizar eI Request.
### Link al repositorio de Github de la dupla de la que son colaboradores  
[Commit elaborado](https://www.ejemplo.com)
### Integrantes
- Yacira Nicol Campoverde
- Sebastian Rojas Berrios


