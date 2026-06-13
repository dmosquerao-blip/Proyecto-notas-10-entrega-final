import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from scipy.stats import (
    f_oneway,
    shapiro,
    levene,
    kruskal
)

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score

import umap

# =====================================================
# CARGA DE DATOS
# =====================================================

df = pd.read_excel("Notas 10.xlsx")

# Elimina espacios al inicio y final
df.columns = df.columns.str.strip()

print("\nDimensiones:")
print(df.shape)

print("\nColumnas:")
print(df.columns.tolist())

# =====================================================
# VARIABLES
# =====================================================

materias = [
    "LENG",
    "TRIG",
    "BIOLO",
    "FISI",
    "QUIM",
    "FILO",
    "CPOL",
    "INGL",
    "EFIS",
    "REL",
    "EYV",
    "INFO"
]

tecnicas = [
    "Electricidad",
    "Electronica",
    "Electromecanica",
    "Diseño corte y confeccion",
    "Soldadura",
    "Ebanisteria",
    "Diseño arquitectonico",
    "Mecanica"
]

# =====================================================
# VALIDACIÓN
# =====================================================

faltantes = [
    c for c in materias + tecnicas
    if c not in df.columns
]

if len(faltantes) > 0:
    raise ValueError(
        f"Columnas faltantes:\n{faltantes}"
    )

# =====================================================
# LIMPIEZA
# =====================================================

df[materias] = df[materias].apply(
    pd.to_numeric,
    errors="coerce"
)

df[materias] = df[materias].fillna(
    df[materias].mean()
)

# =====================================================
# PROMEDIO GENERAL
# =====================================================

df["Promedio_General"] = (
    df[materias]
    .mean(axis=1)
)

# =====================================================
# ELIMINACIÓN DE OUTLIERS (IQR)
# =====================================================

Q1 = df["Promedio_General"].quantile(0.25)
Q3 = df["Promedio_General"].quantile(0.75)

IQR = Q3 - Q1

limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

print("\nLímite inferior:", round(limite_inferior,3))
print("Límite superior:", round(limite_superior,3))

n_original = len(df)

df = df[
    (df["Promedio_General"] >= limite_inferior) &
    (df["Promedio_General"] <= limite_superior)
].copy()

print(
    "\nRegistros eliminados:",
    n_original - len(df)
)

print(
    "Registros restantes:",
    len(df)
)

# =====================================================
# TÉCNICA DEL ESTUDIANTE
# =====================================================

df["Tecnica"] = (
    df[tecnicas]
    .eq(1)
    .idxmax(axis=1)
)

# =====================================================
# DESCRIPTIVOS
# =====================================================

print("\nESTADÍSTICAS DESCRIPTIVAS")

estadisticas = (
    df.groupby("Tecnica")
    ["Promedio_General"]
    .agg(
        [
            "count",
            "mean",
            "median",
            "std",
            "min",
            "max"
        ]
    )
    .round(3)
)

print(estadisticas)

# =====================================================
# BOXPLOT
# =====================================================

plt.figure(figsize=(12,6))

sns.boxplot(
    data=df,
    x="Tecnica",
    y="Promedio_General"
)

plt.xticks(rotation=45)
plt.title("Promedio General por Técnica")
plt.tight_layout()

plt.show()

# =====================================================
# ANOVA
# =====================================================

grupos = [
    df[df["Tecnica"] == t]
    ["Promedio_General"]
    for t in df["Tecnica"].unique()
]

F, p = f_oneway(*grupos)

print("\nANOVA")
print("F =", round(F,4))
print("p =", round(p,6))

# =====================================================
# SHAPIRO
# =====================================================

print("\nSHAPIRO")

for tecnica in df["Tecnica"].unique():

    grupo = (
        df[df["Tecnica"] == tecnica]
        ["Promedio_General"]
    )

    if len(grupo) >= 3:

        stat, pval = shapiro(grupo)

        print(
            tecnica,
            "p =",
            round(pval,4)
        )

# =====================================================
# LEVENE
# =====================================================

stat, p = levene(*grupos)

print("\nLEVENE")
print("p =", round(p,6))

# =====================================================
# KRUSKAL
# =====================================================

H, p = kruskal(*grupos)

print("\nKRUSKAL-WALLIS")
print("H =", round(H,4))
print("p =", round(p,6))

# =====================================================
# TAMAÑO DEL EFECTO
# =====================================================

n = len(df)
k = df["Tecnica"].nunique()

eta2_H = (H - k + 1) / (n - k)

print("\nTamaño del efecto")
print("η²H =", round(eta2_H,4))

if eta2_H < 0.01:
    print("Efecto muy pequeño")
elif eta2_H < 0.06:
    print("Efecto pequeño")
elif eta2_H < 0.14:
    print("Efecto moderado")
else:
    print("Efecto grande")

# =====================================================
# REGRESIÓN
# =====================================================

X_reg = df[
    [
        "Electricidad",
        "Electronica",
        "Electromecanica",
        "Diseño corte y confeccion",
        "Soldadura",
        "Ebanisteria",
        "Diseño arquitectonico"
    ]
]

y_reg = df["Promedio_General"]

modelo_reg = LinearRegression()

modelo_reg.fit(
    X_reg,
    y_reg
)

coeficientes = pd.DataFrame(
    {
        "Variable": X_reg.columns,
        "Coeficiente": modelo_reg.coef_
    }
)

print("\nCOEFICIENTES")

print(
    coeficientes.round(4)
)

print("\nIntercepto:")
print(
    round(
        modelo_reg.intercept_,
        4
    )
)

print("\nR²:")
print(
    round(
        modelo_reg.score(
            X_reg,
            y_reg
        ),
        4
    )
)

# =====================================================
# CLUSTERING
# =====================================================

X_cluster = df[materias]

scaler = StandardScaler()

X_scaled = scaler.fit_transform(
    X_cluster
)

# =====================================================
# PCA
# =====================================================

pca_modelo = PCA(
    n_components=0.90
)

X_pca = pca_modelo.fit_transform(
    X_scaled
)

print(
    "\nComponentes PCA:",
    X_pca.shape[1]
)

print(
    "Varianza explicada:",
    round(
        pca_modelo.explained_variance_ratio_.sum()*100,
        2
    ),
    "%"
)

# =====================================================
# SILHOUETTE
# =====================================================

print("\nEVALUACIÓN DE K")

for k_test in range(2,11):

    modelo = KMeans(
        n_clusters=k_test,
        random_state=42,
        n_init=20
    )

    etiquetas = modelo.fit_predict(
        X_pca
    )

    sil = silhouette_score(
        X_pca,
        etiquetas
    )

    print(
        f"K={k_test} -> {sil:.4f}"
    )

# =====================================================
# CODO
# =====================================================

inercias = []

for k_test in range(1,11):

    modelo = KMeans(
        n_clusters=k_test,
        random_state=42,
        n_init=20
    )

    modelo.fit(X_pca)

    inercias.append(
        modelo.inertia_
    )

plt.figure(figsize=(8,5))

plt.plot(
    range(1,11),
    inercias,
    marker="o"
)

plt.title("Método del Codo")
plt.xlabel("K")
plt.ylabel("Inercia")

plt.show()

# =====================================================
# MODELO FINAL
# =====================================================

modelo_cluster = KMeans(
    n_clusters=2,
    random_state=42,
    n_init=50
)

df["Cluster"] = modelo_cluster.fit_predict(
    X_pca
)

# =====================================================
# VALIDACIÓN
# =====================================================

silhouette = silhouette_score(
    X_pca,
    df["Cluster"]
)

print("\nSilhouette Final:")
print(round(silhouette,4))

print("\nTamaño de clusters")

print(
    df["Cluster"]
    .value_counts()
    .sort_index()
)

# =====================================================
# VALIDACIÓN
# =====================================================

silhouette = silhouette_score(
    X_pca,
    df["Cluster"]
)

print("\nSilhouette Final:")
print(round(silhouette,4))

print("\nTamaño de clusters")

print(
    df["Cluster"]
    .value_counts()
    .sort_index()
)

# =====================================================
# CENTROIDES
# =====================================================

centroides = pd.DataFrame(
    scaler.inverse_transform(
        pca_modelo.inverse_transform(
            modelo_cluster.cluster_centers_
        )
    ),
    columns=materias
)

print("\nCENTROIDES")

print(
    centroides.round(2)
)

# =====================================================
# TÉCNICA VS CLUSTER
# =====================================================

print("\nTABLA TÉCNICA VS CLUSTER")

print(
    pd.crosstab(
        df["Tecnica"],
        df["Cluster"]
    )
)

# =====================================================
# BOXPLOT CLUSTER
# =====================================================

plt.figure(figsize=(8,5))

sns.boxplot(
    data=df,
    x="Cluster",
    y="Promedio_General"
)

plt.title(
    "Promedio General por Cluster"
)

plt.show()

# =====================================================
# PCA VISUAL
# =====================================================

pca_vis = PCA(
    n_components=2
)

X_vis = pca_vis.fit_transform(
    X_scaled
)

df["PCA1"] = X_vis[:,0]
df["PCA2"] = X_vis[:,1]

plt.figure(figsize=(8,6))

sns.scatterplot(
    data=df,
    x="PCA1",
    y="PCA2",
    hue="Cluster",
    palette="Set1"
)

plt.title(
    "Clusters mediante PCA"
)

plt.show()

# =====================================================
# UMAP
# =====================================================

reductor = umap.UMAP(
    n_components=2,
    random_state=42
)

X_umap = reductor.fit_transform(
    X_scaled
)

df["UMAP1"] = X_umap[:,0]
df["UMAP2"] = X_umap[:,1]

plt.figure(figsize=(8,6))

sns.scatterplot(
    data=df,
    x="UMAP1",
    y="UMAP2",
    hue="Cluster",
    palette="Set1"
)

plt.title(
    "Clusters mediante UMAP"
)

plt.show()

print(
    "\nANÁLISIS FINALIZADO CORRECTAMENTE"
)