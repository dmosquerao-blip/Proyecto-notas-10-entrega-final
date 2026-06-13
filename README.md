# Análisis del Rendimiento Académico según la Especialidad Técnica
## Descripción del proyecto

Este proyecto tiene como objetivo analizar si existen diferencias significativas en el rendimiento académico de los estudiantes de grado décimo según la especialidad técnica cursada.

La base de datos contiene las calificaciones de 197 estudiantes en diferentes asignaturas académicas, así como la especialidad técnica a la que pertenece cada estudiante.

# Objetivo general

Determinar si la especialidad técnica cursada por los estudiantes influye significativamente en su rendimiento académico promedio.

#Objetivos específicos
1.Calcular el promedio académico general de cada estudiante.
2.Realizar un análisis descriptivo de las calificaciones.
3.Comparar los promedios académicos entre las diferentes especialidades técnicas.
4.Aplicar pruebas estadísticas para evaluar diferencias significativas entre grupos.
5.Construir modelos de estimación para analizar la relación entre la especialidad técnica y el rendimiento académico.
5.Aplicar regresión lineal para modelar la relación entre variables académicas y el promedio general.
7.Implementar técnicas de clusterización para identificar grupos de estudiantes con patrones de rendimiento similares.

# Base de datos

La información se encuentra en el archivo:

Notas 10.xlsx

La base contiene:

1. Identificador del estudiante.
2. Nombre del estudiante.
3. Calificaciones de las asignaturas.
4. Especialidad técnica codificada mediante variables binarias (One-Hot Encoding).
5. Especialidades técnicas analizadas
Electricidad
Electrónica
Electromecánica
Diseño corte y confección
Soldadura
Ebanistería
Diseño arquitectónico
Mecánica
Metodología

# Ejecucion  
1. Carga y exploración de datos
Lectura del archivo Excel mediante Pandas.
Verificación de tipos de datos.
Identificación de variables académicas y técnicas.
2. Construcción de variables
Cálculo del promedio académico general para cada estudiante.
Identificación de la especialidad técnica correspondiente.
3. Análisis descriptivo
Estadísticas descriptivas.
Distribuciones por técnica.
Visualización mediante diagramas de caja (boxplots).
4. Análisis inferencial
Prueba ANOVA.
Verificación de supuestos estadísticos.
Comparación de grupos mediante pruebas no paramétricas (Kruskal-Wallis).
5. Modelos predictivos
Aplicación de regresión lineal para analizar la relación entre variables académicas y el promedio general.
Evaluación del modelo mediante métricas como R² y error cuadrático medio (MSE).
6. Análisis de clusterización
Aplicación de algoritmos de clustering (como K-Means) para agrupar estudiantes según su rendimiento académico.
Visualización de los grupos obtenidos.
Interpretación de los clusters en función del desempeño y la especialidad técnica.
Herramientas utilizadas
Python 3.14.5
Pandas
NumPy
SciPy
Matplotlib
Seaborn
Scikit-Learn

# Estructura del proyecto

Trabajo final fundamentos ciencias de datos/
│
├── Main.py
├── Notas 10.xlsx
├── README.md
├── Proyecto_Notas_10.ipynb
├── DATABASE.md
├── WORKFLOWS.md
├── requisitos.txt
├── .gitignore
├── .env.example
└── Trabajo final fcd.code-workspace

# Requerimientos 

Instalar dependencias:
pip install -r requirements.txt

Ejecutar el proyecto:
python Main.py

# Tipo de proyecto

Este trabajo corresponde a un análisis de datos con enfoque híbrido que integra inferencia estadística, modelos predictivos mediante regresión lineal y técnicas de clusterización para la segmentación de estudiantes según su rendimiento académico.