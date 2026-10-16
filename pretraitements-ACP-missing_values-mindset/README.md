# Prétraitement de données : ACP et imputation des valeurs manquantes sur le jeu Digits

## Description courte

**Français.** Notebook de travaux pratiques sur le prétraitement de données : réduction de dimension par ACP et comparaison de méthodes de complétion des valeurs manquantes sur des chiffres manuscrits.

**English.** Practical notebook on data preprocessing: dimensionality reduction with PCA and comparison of missing value imputation methods on handwritten digits.

## Objectif du projet

**Français.** Comprendre ce que fait l'ACP sur des données de grande dimension et en interpréter les projections 2D et 3D. Comparer plusieurs stratégies d'imputation de valeurs manquantes. Quantifier leur qualité par un écart quadratique par rapport aux vraies valeurs.

**English.** Understand what PCA does on high dimensional data and interpret its 2D and 3D projections. Compare several missing value imputation strategies. Measure their quality through a squared error against the true values.

## Dataset

**Français.** Jeu de données Digits, chargé via scikit-learn : 1 797 images de chiffres manuscrits (classes de 0 à 9), chacune de taille 8 x 8 pixels, soit 64 variables numériques par exemple (intensité des pixels). Pour la partie imputation, entre 1 000 et 2 000 valeurs sont supprimées aléatoirement (1 363 lors de l'exécution présentée, soit environ 1,2 % des valeurs).

**English.** Digits dataset, loaded through scikit-learn: 1,797 handwritten digit images (classes 0 to 9), each 8 x 8 pixels, giving 64 numerical features per sample (pixel intensity). For the imputation part, between 1,000 and 2,000 values are randomly removed (1,363 in the presented run, about 1.2% of the values).

## Technologies et outils

**Français.**
- Python 3 et Jupyter Notebook
- NumPy pour la manipulation de matrices
- scikit-learn (PCA, SimpleImputer, KNNImputer, load_digits)
- matplotlib pour les visualisations 2D et 3D

**English.**
- Python 3 and Jupyter Notebook
- NumPy for matrix handling
- scikit-learn (PCA, SimpleImputer, KNNImputer, load_digits)
- matplotlib for 2D and 3D visualizations

## Approche et modèles

**Français.**
- Preprocessing : affichage des images, comptage des valeurs manquantes (globalement et par colonne) via des fonctions dédiées.
- ACP : projection des 64 variables sur 2 puis 3 composantes principales, avec visualisation par classe.
- Imputation : trois méthodes comparées, la valeur la plus fréquente par colonne, la moyenne par colonne, et les k plus proches voisins (k = 5, pondération uniforme).
- Métrique : somme des écarts au carré entre les valeurs imputées et les valeurs réelles (plus elle est faible, meilleure est la méthode).

**English.**
- Preprocessing: image display, counting of missing values (overall and per column) with dedicated functions.
- PCA: projection of the 64 features onto 2 then 3 principal components, with visualization by class.
- Imputation: three methods compared, the most frequent value per column, the column mean, and k nearest neighbors (k = 5, uniform weights).
- Metric: sum of squared differences between imputed and true values (the lower, the better the method).

## Résultats

**Français.**
- Les projections ACP en 2D et 3D permettent de visualiser la structure des classes de chiffres, avec des recouvrements entre certaines classes qui limitent la séparation par simples frontières.
- Classement des méthodes d'imputation par écart quadratique : k plus proches voisins (6 378), moyenne par colonne (25 369), valeur la plus fréquente (57 017).
- Les k plus proches voisins réduisent l'erreur d'un facteur environ 4 par rapport à la moyenne et environ 9 par rapport à la valeur la plus fréquente.

**English.**
- The 2D and 3D PCA projections reveal the class structure of the digits, with overlaps between some classes that limit separation by simple boundaries.
- Imputation methods ranked by squared error: k nearest neighbors (6,378), column mean (25,369), most frequent value (57,017).
- k nearest neighbors cut the error by a factor of about 4 compared with the mean and about 9 compared with the most frequent value.

## Structure du repository

**Français.**
- TP2_prep.ipynb : notebook principal (ACP sur Digits, imputation des valeurs manquantes)
- README.md : présentation du projet

**English.**
- TP2_prep.ipynb: main notebook (PCA on Digits, missing value imputation)
- README.md: project overview
