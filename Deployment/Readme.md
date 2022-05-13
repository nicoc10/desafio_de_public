# Deployment

El ETL puede ser desplegado con Docker. La imagen contiene un cluster Spark y comparte volúmenes de datos para leer los archivos .csv
Para ejecutar el ETL:
```
docker-compose up
```
### Variables
Variables de sistema:
- INPUT_RESULT: Ubicación de `result.csv`
- INPUT_CONSOLES: Ubicación de `consoles.csv`
- OUTPUT_FOLDER: Ubicación del resultado
### Volúmenes
Además de los datos de entrada, la carpeta `data` contendrá los resultados luego de ejecutar el ETL


