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
[Commit elaborado](https://github.com/YaciraUTEC/Desarrollo_dist/tree/new-feature-branch2)

### ¡ALERTA!

**Importante**: En este caso hemos colocado el link del branch elaborado en nuestro propio git, porque no encontramos una dupla para poder colaborar 🥹
----------------------------------------------------------------------
# Actividad 2: Pruebas Unitarias

* *Caso de Éxito:* Asegura que la aplicación puede calcular la distancia entre dos ciudades válidas.
* *Caso Extremo 1 (Ciudad No Existente):* Asegura que la aplicación maneje correctamente la situación cuando se proporciona una ciudad que no existe en el archivo CSV.
* *Caso Extremo 2 (Misma Ciudad dos Veces):* Asegura que la aplicación maneje correctamente la situación cuando se proporciona la misma ciudad dos veces, devolviendo una distancia de 0 km.

### Pasos
1. Añadimos una carpeta llamada `tests`, dentro de ella se encontrarán 2 archivos: `init.py` y `test_providers`
2. Implementamos los 3 casos, para eso utilizaremos `unittest`
3. Ejecutamos las pruebas unitarias `python -m unittest discover -s tests`

### Casos de prueba (Forma Manuel)
Tomamos en cuenta el formato Precondition, Test Steps, Test Data, Expected Result
### Casos de Prueba Manuales

| Test Case ID | Title                                    | Preconditions                                                               | Test Steps                                                                 | Test Data                                              | Expected Result                               |
|--------------|------------------------------------------|----------------------------------------------------------------------------|---------------------------------------------------------------------------|-------------------------------------------------------|-----------------------------------------------|
| TC_001       | Distancia entre dos ciudades existentes  | Archivo `worldcities.csv` válido, conexión a internet disponible             | 1. Ejecutar el programa.<br>2. Seleccionar la fuente de datos.<br>3. Ingresar "Lima, Peru".<br>4. Ingresar "Cairo, Egypt".<br>5. Solicitar distancia. | Ciudad1: Lima<br>País1: Peru<br>Ciudad2: Cairo<br>País2: Egypt | La distancia entre Lima y Cairo se muestra correctamente (aprox. 12345 km). |
| TC_002       | Ciudad no existente                      | Archivo `worldcities.csv` válido, conexión a internet disponible             | 1. Ejecutar el programa.<br>2. Seleccionar la fuente de datos.<br>3. Ingresar "NonExistentCity, Peru".<br>4. Ingresar "Cairo, Egypt".<br>5. Solicitar distancia. | Ciudad1: NonExistentCity<br>País1: Peru<br>Ciudad2: Cairo<br>País2: Egypt | El programa lanza un error indicando que la ciudad "NonExistentCity" no se encuentra. |
| TC_003       | Misma ciudad dos veces                  | Archivo `worldcities.csv` válido, conexión a internet disponible             | 1. Ejecutar el programa.<br>2. Seleccionar la fuente de datos.<br>3. Ingresar "Lima, Peru" dos veces.<br>5. Solicitar distancia. | Ciudad1: Lima<br>País1: Peru<br>Ciudad2: Lima<br>País2: Peru | El programa muestra una distancia de 0 km. |


### Integrantes
- Yacira Nicol Campoverde
- Sebastian Rojas Berrios
