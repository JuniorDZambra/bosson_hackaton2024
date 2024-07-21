# Visualización interactiva para análisis de desempeño en aprendizaje escolar en Colombia
### Equipo Bosson: Leonardo Manrique, Lester Peña, Junior Zambrano, Luis Camacho.
## Introducción
En este repositorio se muestra la metodología utilizada para crear una visualización interactiva de los datos obtenidos por los examénes diagnósticos **Saber 11°** [1] y **Saber Pro** [2] realizados por el gobierno Colombiano entre los años 2010 y 2022.

Esta visualización facilita el análisis del desempeño del aprendizaje en el sistema educativo del pais en la eduación media y universitaria respectivamente.

Los exámenes **Saber 11°** y **Saber Pro** son exámenes estandarizados que se realizan en Colombia para evaluar el desempeño académico de los estudiantes en distintas áreas de estudio:

- El examen **Saber 11°** esta compuesto por 5 pruebas correspondientes a las distintas áreas de estudio de la eduación media a evaluar que son: Lectura Crítica, Matemáticas, Sociales y Ciudadanas, Ciencias naturales e Inglés; cada prueba se evalúa en base a 100 puntos de modo que el exámen cuenta con un puntaje global de 500 puntos.

- Por otro lado, el exámen **Saber Pro** esta dirigdo a estudiantes universitarios. Este exámen cuenta con 5 modulos de evaluación de temas genéricos: Lectura crítica, Razonamiento Cuantitativo, Competencias Ciudadanas, Comunicación Escrita e Inglés, y cuenta con un grupo de modulos específicos adicionales que dependen del área de estudio del estudiante. Cada modulo se evalua en base a 300 puntos y el puntaje global del exámen es el promedio de estos.

Los datos recopilados mostrados en la visualización son de carácter demógrafico, acádemico y socio-ecnómico.

## Metodología
Para realizar la visualización interactiva se armó un *dashboard* utilizando las librerias *dash* en Python. Mediante este *dashboard* se interactua con los datos en la red mediante un llamado al acceso API. Luego, se realiza un codigo para generar el reporte de los datos y desarrollar las acciones interactivas que relacionan los datos mediante gráficos los cuales pueden ser modificados seleccionando la dimension, filtros, entre otros parámetros. Para el apartado viusual se utilizó HTML y CSS para realizar una portada en la cual se puede elegir entre los distintos exámenes. Además, allí se muestra el titulo y el logo del proyecto.

## Instalación y uso de la aplicación
### Linux
1. Clonar el repositorio:
```bash
git clone https://github.com/JuniorDZambra/bosson_hackaton2024.git
```
2. Instalar las dependencias:
```bash
python -m pip install -r requirements.txt
```
3. Ejecutar el archivo `app.py`:
```bash
python3 app.py
```
4. Abrir el navegador y acceder a la dirección `http://127.0.0.1:8050/`.
5. Mientras la aplicación se esté ejecutando, se puede interactuar con los datos mediante los filtros y gráficos interactivos.
6. Para cerrar la aplicación, presionar `Ctrl + C` en la terminal.

## Referencias
[1] [https://www.datos.gov.co/Educaci-n/Resultados-nicos-Saber-11/kgxf-xxbe/about_data](https://www.datos.gov.co/Educaci-n/Resultados-nicos-Saber-11/kgxf-xxbe/about_data)

[2] [https://www.datos.gov.co/Educaci-n/Resultados-nicos-Saber-Pro/u37r-hjmu/data_preview](https://www.datos.gov.co/Educaci-n/Resultados-nicos-Saber-Pro/u37r-hjmu/data_preview)