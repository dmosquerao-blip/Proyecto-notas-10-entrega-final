## Análisis Estadístico y de Ciencia de Datos

El proyecto incluye diferentes etapas de análisis con el objetivo de estudiar la relación entre el rendimiento académico de los estudiantes y la especialidad técnica cursada.

### Estadística Descriptiva

Se calculan medidas descriptivas sobre las calificaciones de los estudiantes, incluyendo:

- Número de estudiantes por técnica.
- Promedio general por estudiante.
- Media, mediana y desviación estándar por técnica.
- Valores mínimos y máximos por grupo.
- Diagramas de caja (Boxplots) para visualizar la distribución de los promedios académicos y detectar posibles valores atípicos.

### Análisis Inferencial

Se aplican pruebas estadísticas para determinar si existen diferencias significativas entre las especialidades técnicas:

- Prueba de normalidad de Shapiro-Wilk.
- Prueba de homogeneidad de varianzas de Levene.
- ANOVA de un factor.
- Prueba no paramétrica de Kruskal-Wallis.
- Cálculo del tamaño del efecto mediante η²H.

Los resultados obtenidos permiten evaluar si la especialidad técnica está asociada con diferencias significativas en el rendimiento académico general de los estudiantes.

### Regresión Lineal

Se implementa un modelo de regresión lineal utilizando las especialidades técnicas codificadas mediante One-Hot Encoding.

#### Objetivos

- Evaluar la capacidad explicativa de la técnica sobre el rendimiento académico.
- Estimar el efecto de cada especialidad técnica sobre el promedio general.
- Calcular el coeficiente de determinación (R²).
- Identificar qué especialidades presentan asociaciones positivas o negativas con el desempeño académico.

### Reducción de Dimensionalidad mediante PCA

Antes de realizar la clusterización, las variables académicas son estandarizadas mediante `StandardScaler` para eliminar diferencias de escala entre materias.

Posteriormente se aplica el método de Análisis de Componentes Principales (PCA) con los siguientes objetivos:

- Reducir la dimensionalidad del conjunto de datos.
- Eliminar redundancia entre variables altamente correlacionadas.
- Mantener la mayor proporción posible de la variabilidad original.
- Mejorar la eficiencia computacional de los algoritmos de agrupamiento.

En el análisis realizado, PCA redujo las 12 variables académicas originales a 9 componentes principales, conservando aproximadamente el 93.12% de la varianza total del conjunto de datos.

### Clusterización

Se aplica el algoritmo K-Means utilizando las calificaciones académicas como variables de entrada.

#### Objetivos

- Identificar grupos de estudiantes con patrones de rendimiento similares.
- Analizar la distribución de las especialidades técnicas dentro de cada grupo.
- Comparar el rendimiento promedio entre clusters.
- Detectar posibles perfiles académicos diferenciados.

### Selección del Número de Clusters

Para determinar el número adecuado de grupos se emplean dos criterios complementarios:

#### Método del Codo (Elbow Method)

Se calcula la inercia para distintos valores de K y se construye la curva correspondiente con el fin de identificar el punto donde la reducción de la variabilidad interna deja de ser significativa.

#### Coeficiente Silhouette

Se calcula el índice Silhouette para diferentes valores de K.

Este indicador permite evaluar:

- La cohesión interna de cada cluster.
- La separación entre grupos.
- La calidad global de la partición obtenida.

En los resultados obtenidos, el mayor valor de Silhouette fue aproximadamente 0.2373 para K=3, lo que indica una estructura de agrupamiento débil pero identificable dentro de los datos académicos.

### Validación e Interpretación de Clusters

Una vez obtenidos los clusters se realizan los siguientes análisis:

- Número de estudiantes por cluster.
- Comparación de promedios académicos entre grupos.
- Análisis de centroides.
- Tabla de contingencia entre especialidad técnica y cluster.
- Interpretación de perfiles académicos asociados a cada grupo.

Los resultados mostraron que la mayoría de los estudiantes se distribuyen entre dos grandes perfiles académicos de rendimiento medio y alto, mientras que un tercer grupo estuvo asociado a un caso atípico identificado durante el análisis.

### Visualización de Clusters mediante PCA

Con fines exploratorios y de interpretación visual, los estudiantes son proyectados sobre los dos primeros componentes principales obtenidos mediante PCA.

Esta representación permite:

- Observar la separación entre clusters.
- Identificar zonas de solapamiento.
- Detectar posibles observaciones atípicas.
- Analizar la estructura global del conjunto de datos.

### Visualización de Clusters mediante UMAP

Adicionalmente se utiliza UMAP (Uniform Manifold Approximation and Projection), una técnica no lineal de reducción de dimensionalidad que preserva mejor las relaciones locales entre observaciones.

Los objetivos de esta visualización son:

- Explorar posibles estructuras complejas en los datos.
- Evaluar la consistencia de los clusters obtenidos por K-Means.
- Identificar agrupamientos que podrían no ser visibles mediante PCA.
- Complementar la interpretación visual del modelo de clusterización.

### Hallazgos Principales

Los análisis estadísticos indicaron que no existen diferencias significativas en el rendimiento académico general entre las distintas especialidades técnicas. Tanto ANOVA como Kruskal-Wallis produjeron valores de significancia superiores a 0.05, mientras que el tamaño del efecto obtenido fue pequeño (η²H = 0.0272), sugiriendo una influencia reducida de la técnica sobre el desempeño académico.

Por otro lado, la clusterización permitió identificar grupos de estudiantes con diferentes niveles de rendimiento académico, aunque con una separación moderada entre ellos, reflejada en los valores del coeficiente Silhouette. La distribución de las especialidades dentro de los clusters mostró una mezcla considerable de estudiantes de todas las técnicas, lo que sugiere que la modalidad técnica cursada no constituye el principal factor explicativo de las diferencias de desempeño observadas.