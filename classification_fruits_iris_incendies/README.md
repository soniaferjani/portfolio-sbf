# Normalisation de variables et analyse exploratoire : Iris, Fruits et Incendies de forêt en France

## Description courte

**Français.** Notebook d'initiation à la science des données couvrant la normalisation de variables, la corrélation et l'analyse exploratoire de données réelles avec Python.

**English.** Introductory data science notebook covering feature normalization, correlation and exploratory analysis of real data using Python.

## Objectif du projet

**Français.** Comprendre l'effet des principales normalisations sur la dispersion et les distances d'un jeu de données. Maîtriser pandas et matplotlib pour nettoyer, résumer et visualiser des données. Analyser les liens entre localisation, période et surface brûlée sur les feux de forêt de 2023 à 2025.

**English.** Understand the effect of the main normalizations on the dispersion and distances of a dataset. Use pandas and matplotlib to clean, summarize and visualize data. Analyze the links between location, period and burned area for forest fires from 2023 to 2025.

## Dataset

**Français.**
- Iris (Fisher, 1936), chargé via scikit-learn : 150 observations, 4 variables (longueur et largeur des sépales et des pétales en cm), 3 espèces (setosa, versicolor, virginica).
- Fruits (fruits.csv), fourni avec le TP : 20 observations, 2 variables (Weight, Length) et une étiquette binaire (Fruit) distinguant deux types de fruits.
- Incendies 2023 à 2025 (Incendies23-25.csv), données publiques sur les feux de forêt en France : 6 590 lignes et 17 colonnes (année, département, code INSEE, commune, date de première alerte, surfaces par type de terrain en m2, nature du feu, précision de la donnée).

**English.**
- Iris (Fisher, 1936), loaded through scikit-learn: 150 observations, 4 variables (sepal and petal length and width in cm), 3 species (setosa, versicolor, virginica).
- Fruits (fruits.csv), provided with the course: 20 observations, 2 variables (Weight, Length) and a binary label (Fruit) separating two fruit types.
- Fires 2023 to 2025 (Incendies23-25.csv), public data on forest fires in France: 6,590 rows and 17 columns (year, department, INSEE code, municipality, first alert date, areas by land type in m2, fire nature, data accuracy).

## Technologies et outils

**Français.**
- Python 3 et Jupyter Notebook
- NumPy et pandas pour la manipulation de données
- scikit-learn pour le chargement du jeu Iris
- matplotlib pour les graphiques
- geopandas pour les cartes départementales (GeoJSON des départements français)

**English.**
- Python 3 and Jupyter Notebook
- NumPy and pandas for data handling
- scikit-learn for loading the Iris dataset
- matplotlib for plotting
- geopandas for departmental maps (GeoJSON of French departments)

## Approche et modèles

**Français.**
- Preprocessing sur les fruits : implémentation de quatre normalisations (MinMax, centrage par l'étendue, standardisation z-score, projection sur la boule unité) en excluant la colonne de classe, puis comparaison des nuages de points.
- Preprocessing sur les incendies : remplacement des surfaces manquantes par 0, suppression des lignes dont la précision est signalée comme partielle ou non valide, retrait des feux de moins de 20 m2.
- Modèles : aucun modèle prédictif entraîné. L'approche est descriptive et statistique.
- Métriques : moyenne, minimum, maximum, écart type, coefficient de corrélation, agrégations par département, mois et nature du feu.

**English.**
- Preprocessing on fruits: implementation of four normalizations (MinMax, range centering, z-score standardization, unit ball projection) excluding the class column, followed by a scatter plot comparison.
- Preprocessing on fires: missing areas set to 0, rows flagged as partial or invalid data removed, fires under 20 m2 dropped.
- Models: no predictive model trained. The approach is descriptive and statistical.
- Metrics: mean, minimum, maximum, standard deviation, correlation coefficient, aggregations by department, month and fire nature.

## Résultats

**Français.**
- Iris : les pétales (longueur et largeur) séparent le mieux les trois espèces. Moyennes des variables : 5,84 / 3,06 / 3,76 / 1,20 cm.
- Fruits : les normalisations modifient l'échelle des axes sans changer la forme du nuage, sauf la projection sur la boule unité qui altère les distances relatives.
- Incendies : 6 590 feux déclarés, 5 066 après nettoyage. L'Aude (11) cumule la plus grande surface brûlée (environ 143 millions de m2). Août concentre la plus grande surface totale (environ 144 millions de m2). La corrélation entre le mois et la surface parcourue est quasi nulle (0,008).

**English.**
- Iris: petal measurements (length and width) separate the three species best. Variable means: 5.84 / 3.06 / 3.76 / 1.20 cm.
- Fruits: normalizations change the axis scale without altering the cloud shape, except the unit ball projection which distorts relative distances.
- Fires: 6,590 reported fires, 5,066 after cleaning. Aude (11) has the largest burned area (about 143 million m2). August holds the largest total area (about 144 million m2). The correlation between month and burned area is almost null (0.008).

## Structure du repository

**Français.**
- fruits_iris_incendies.ipynb : notebook principal (découverte de scikit-learn, normalisations, analyse des incendies)
- fruits.csv : jeu de données des fruits
- Incendies23-25.csv : jeu de données des feux de forêt
- README.md : présentation du projet

**English.**
- fruits_iris_incendies.ipynb: main notebook (scikit-learn introduction, normalizations, fire analysis)
- fruits.csv: fruits dataset
- Incendies23-25.csv: forest fires dataset
- README.md: project overview
