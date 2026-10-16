# Régression linéaire par moindres carrés : prix de vente et Eucalyptus

## Description courte

**Français.** Notebook de travaux pratiques sur la régression linéaire par moindres carrés avec scikit-learn, complété par une implémentation à partir de la formule analytique.

**English.** Practical notebook on least squares linear regression with scikit-learn, complemented by an implementation based on the analytical formula.

## Objectif du projet

**Français.** Comprendre le fonctionnement d'un régresseur linéaire (pente, intercept, coefficient de détermination) et estimer ses performances par hold-out et validation croisée. Améliorer le modèle par transformation des variables explicatives. Reprogrammer la solution des moindres carrés et la comparer à scikit-learn.

**English.** Understand how a linear regressor works (slope, intercept, coefficient of determination) and estimate its performance with hold-out and cross validation. Improve the model through feature transformations. Reimplement the least squares solution and compare it with scikit-learn.

## Dataset

**Français.**
- Données jouet : 8 observations associant un prix de vente (x) au nombre de produits vendus (y), saisies directement dans le notebook.
- Eucalyptus (eucalyptus.txt), fourni avec le TP : 1 429 observations, 2 variables numériques : la hauteur de l'arbre (h, cible) et sa circonférence (c, variable explicative).

**English.**
- Toy data: 8 observations linking a selling price (x) to the number of products sold (y), entered directly in the notebook.
- Eucalyptus (eucalyptus.txt), provided with the course: 1,429 observations, 2 numerical variables: tree height (h, target) and circumference (c, explanatory variable).

## Technologies et outils

**Français.**
- Python 3 et Jupyter Notebook
- NumPy pour le calcul matriciel
- scikit-learn (LinearRegression, train_test_split, KFold, cross_val_score, métriques)
- matplotlib pour les visualisations 2D et 3D

**English.**
- Python 3 and Jupyter Notebook
- NumPy for matrix computation
- scikit-learn (LinearRegression, train_test_split, KFold, cross_val_score, metrics)
- matplotlib for 2D and 3D visualizations

## Approche et modèles

**Français.**
- Preprocessing : mise en forme des variables en matrices (n, d), ajout de transformations de la circonférence (logarithme, racine carrée, inverse, puissances 2 et 3).
- Modèles : régression linéaire simple avec et sans intercept, régression multivariée sur variables transformées (douze combinaisons comparées), implémentation maison w = (X^T X)^(-1) X^T y.
- Évaluation : 10 répétitions de hold-out (80 % apprentissage, 20 % test) et validation croisée à 10 plis.
- Métriques : coefficient de détermination R2 et erreur quadratique moyenne (MSE).

**English.**
- Preprocessing: reshaping variables into (n, d) matrices, adding transformations of the circumference (logarithm, square root, inverse, powers 2 and 3).
- Models: simple linear regression with and without intercept, multivariate regression on transformed features (twelve combinations compared), custom implementation w = (X^T X)^(-1) X^T y.
- Evaluation: 10 repeated hold-outs (80% training, 20% test) and 10-fold cross validation.
- Metrics: coefficient of determination R2 and mean squared error (MSE).

## Résultats

**Français.**
- Données jouet : R2 de 0,88 avec intercept (MSE 121,8) contre un R2 de -5,39 sans intercept, ce qui montre le rôle indispensable du terme constant.
- Eucalyptus, modèle linéaire sur c : R2 moyen de 0,755 (hold-out) et 0,765 (validation croisée), MSE moyenne proche de 1,45.
- Eucalyptus, avec c et log c : R2 moyen de 0,789 et MSE moyenne de 1,29 en validation croisée. Meilleure combinaison testée (c, c^2, racine de c, log c) : R2 de 0,792.
- L'implémentation maison reproduit les coefficients et les scores de scikit-learn.

**English.**
- Toy data: R2 of 0.88 with intercept (MSE 121.8) versus an R2 of -5.39 without intercept, showing the essential role of the constant term.
- Eucalyptus, linear model on c: mean R2 of 0.755 (hold-out) and 0.765 (cross validation), mean MSE close to 1.45.
- Eucalyptus, with c and log c: mean R2 of 0.789 and mean MSE of 1.29 in cross validation. Best combination tested (c, c^2, square root of c, log c): R2 of 0.792.
- The custom implementation reproduces the scikit-learn coefficients and scores.

## Structure du repository

**Français.**
- tp_regression.ipynb : notebook principal (régression simple, Eucalyptus, implémentation maison)
- eucalyptus.txt : jeu de données Eucalyptus
- README.md : présentation du projet

**English.**
- tp_regression.ipynb: main notebook (simple regression, Eucalyptus, custom implementation)
- eucalyptus.txt: Eucalyptus dataset
- README.md: project overview
