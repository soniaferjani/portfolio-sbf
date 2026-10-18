# Étude de la pollution des stations de la RATP

## Description courte

**Français.** Notebook d'analyse de la qualité de l'air dans les stations du réseau francilien, avec calcul d'un niveau de pollution moyen par ligne de transport.

**English.** Notebook analyzing air quality in Île-de-France transit stations, computing an average pollution level per transport line.

## Objectif du projet

**Français.** Classer les lignes du réseau selon le niveau de pollution aux particules de leurs stations. Mesurer l'effet de l'exclusion des stations aériennes sur ce classement. Examiner le lien entre le nombre de stations d'une ligne et sa pollution moyenne.

**English.** Rank network lines by the particle pollution level of their stations. Measure the effect of excluding overground stations on this ranking. Examine the link between the number of stations on a line and its average pollution.

## Dataset

**Français.** Jeu de données d'Île-de-France Mobilités sur la qualité de l'air dans les stations, réalisé avec Airparif et publié sur data.gouv.fr : 665 stations et 19 colonnes. Principales variables : identifiant et nom de la station, nom de la ligne, niveau de pollution aux particules (station aérienne, pas de données, faible, moyenne, élevée), incertitude, recommandation de surveillance, coordonnées GPS.

**English.** Île-de-France Mobilités dataset on air quality in stations, produced with Airparif and published on data.gouv.fr: 665 stations and 19 columns. Main variables: station identifier and name, line name, particle pollution level (overground station, no data, low, medium, high), uncertainty, monitoring recommendation, GPS coordinates.

## Technologies et outils

**Français.**
- Python 3 et Jupyter Notebook
- pandas et NumPy pour le nettoyage et les agrégations
- matplotlib pour les nuages de points
- unicodedata pour la normalisation des textes

**English.**
- Python 3 and Jupyter Notebook
- pandas and NumPy for cleaning and aggregations
- matplotlib for scatter plots
- unicodedata for text normalization

## Approche et modèles

**Français.**
- Preprocessing : lecture avec détection automatique du séparateur, conservation des 4 premières et des 3 dernières colonnes, normalisation des textes (minuscules, sans accents), détection automatique des colonnes utiles.
- Encodage : conversion du niveau de pollution en score numérique (station aérienne 0,5, pas de données 0,5, faible 1, moyenne 2, élevée 3).
- Modèles : aucun modèle d'apprentissage automatique. L'approche est descriptive.
- Métriques : pollution moyenne par ligne (somme des scores divisée par le nombre de stations), calculée avec toutes les stations puis hors stations aériennes, classements des 10 lignes les plus et les moins polluées.

**English.**
- Preprocessing: loading with automatic separator detection, keeping the first 4 and last 3 columns, text normalization (lowercase, no accents), automatic detection of useful columns.
- Encoding: conversion of the pollution level into a numerical score (overground station 0.5, no data 0.5, low 1, medium 2, high 3).
- Models: no machine learning model. The approach is descriptive.
- Metrics: average pollution per line (sum of scores divided by the number of stations), computed with all stations then excluding overground stations, rankings of the 10 most and least polluted lines.

## Résultats

**Français.**
- Toutes stations : les lignes de métro 9 (1,97), 5 (1,84) et 10 (1,78) figurent parmi les plus polluées parmi les lignes de taille significative. Les RER E, D, B et C sont les moins polluées (0,62 à 0,70), car elles comptent beaucoup de stations aériennes.
- Stations souterraines uniquement : la ligne 5 monte à 2,00, suivie des lignes 9 (1,97), 2 (1,95) et 6 (1,93). La ligne 4 reste la moins polluée (1,17), devant les lignes 1 (1,36) et 13 (1,40).
- L'exclusion des stations aériennes modifie nettement le classement des RER : le RER A passe de 0,88 à 1,67.
- Limite : dans la version actuelle, les stations « pollution élevée » et « pas de données » ne sont pas reconnues par la table de correspondance et sont écartées des moyennes. Les scores par ligne sont donc probablement sous-estimés.

**English.**
- All stations: metro lines 9 (1.97), 5 (1.84) and 10 (1.78) are among the most polluted lines of significant size. RER E, D, B and C are the least polluted (0.62 to 0.70) because they include many overground stations.
- Underground stations only: line 5 rises to 2.00, followed by lines 9 (1.97), 2 (1.95) and 6 (1.93). Line 4 remains the least polluted (1.17), ahead of lines 1 (1.36) and 13 (1.40).
- Excluding overground stations significantly changes the RER ranking: RER A goes from 0.88 to 1.67.
- Limitation: in the current version, "high pollution" and "no data" stations are not recognized by the mapping table and are dropped from the averages. Line scores are therefore likely underestimated.

## Structure du repository

**Français.**
- etude_pollution_ratp.ipynb : notebook principal (chargement, nettoyage, encodage, moyennes par ligne, visualisations)
- README.md : présentation du projet

**English.**
- etude_pollution_ratp.ipynb: main notebook (loading, cleaning, encoding, per line averages, visualizations)
- README.md: project overview
