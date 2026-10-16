# Classification par k plus proches voisins sur le jeu Digits

## Description courte

**Français.** Notebook de travaux pratiques sur la classification de chiffres manuscrits par les k plus proches voisins, avec étude des hyperparamètres et de l'estimation de l'erreur réelle.

**English.** Practical notebook on handwritten digit classification with k nearest neighbors, including a study of hyperparameters and real error estimation.

## Objectif du projet

**Français.** Apprendre, évaluer et régler un classifieur k plus proches voisins avec scikit-learn. Comparer l'erreur d'apprentissage à l'erreur réelle estimée par hold-out et validation croisée. Analyser les confusions entre classes.

**English.** Train, evaluate and tune a k nearest neighbors classifier with scikit-learn. Compare training error with real error estimated by hold-out and cross validation. Analyze confusions between classes.

## Dataset

**Français.** Jeu de données Digits, chargé via scikit-learn : 1 797 images de chiffres manuscrits en niveaux de gris (8 x 8 pixels), soit 64 variables numériques par exemple (intensité des pixels), et 10 classes (chiffres de 0 à 9).

**English.** Digits dataset, loaded through scikit-learn: 1,797 grayscale handwritten digit images (8 x 8 pixels), giving 64 numerical features per sample (pixel intensity), and 10 classes (digits 0 to 9).

## Technologies et outils

**Français.**
- Python 3 et Jupyter Notebook
- NumPy pour la manipulation de matrices
- scikit-learn (KNeighborsClassifier, train_test_split, cross_val_score, confusion_matrix)
- matplotlib pour les visualisations

**English.**
- Python 3 and Jupyter Notebook
- NumPy for matrix handling
- scikit-learn (KNeighborsClassifier, train_test_split, cross_val_score, confusion_matrix)
- matplotlib for visualizations

## Approche et modèles

**Français.**
- Preprocessing : affichage des images, mise en forme des données en vecteurs de 64 valeurs, découpages apprentissage et test (75/25, 50/50, 70/30, 80/20).
- Modèle : k plus proches voisins, avec variation de k (1 à 35) et de la distance de Minkowski (p = 1, 2 et 5).
- Évaluation : erreur d'apprentissage, hold-out simple, hold-out répété 10 fois, validation croisée à 10 plis, matrice de confusion 10 x 10.
- Métriques : taux d'erreur, exactitude et F1-mesure macro (validation croisée à 5 plis).

**English.**
- Preprocessing: image display, data shaped as 64 value vectors, train and test splits (75/25, 50/50, 70/30, 80/20).
- Model: k nearest neighbors, varying k (1 to 35) and the Minkowski distance (p = 1, 2 and 5).
- Evaluation: training error, single hold-out, hold-out repeated 10 times, 10-fold cross validation, 10 x 10 confusion matrix.
- Metrics: error rate, accuracy and macro F1 score (5-fold cross validation).

## Résultats

**Français.**
- L'erreur d'apprentissage est nulle pour k = 1 (chaque exemple est son propre voisin) puis augmente avec k, de 0,9 % pour k = 2 à environ 3,1 % pour k = 35.
- Erreur réelle pour k = 3 : environ 3,0 % en moyenne sur 10 hold-out (70/30) et 2,3 % en validation croisée à 10 plis.
- F1-mesure macro en validation croisée à 5 plis : environ 0,967 (erreur de 3,3 %).
- Matrice de confusion (k = 12, test de 20 %) : classes presque toutes parfaitement reconnues, avec quelques confusions du 8 vers le 1 (3 cas) et du 9 vers les 3, 4 et 5.
- Test sur images tournées de 180 degrés : le classifieur échoue fortement, avec notamment des 6 reconnus comme des 9 (165 sur 181).

**English.**
- Training error is zero for k = 1 (each sample is its own neighbor) then grows with k, from 0.9% for k = 2 to about 3.1% for k = 35.
- Real error for k = 3: about 3.0% on average over 10 hold-outs (70/30) and 2.3% in 10-fold cross validation.
- Macro F1 score in 5-fold cross validation: about 0.967 (3.3% error).
- Confusion matrix (k = 12, 20% test set): nearly all classes perfectly recognized, with a few confusions of 8 as 1 (3 cases) and of 9 as 3, 4 and 5.
- Test on images rotated by 180 degrees: the classifier fails strongly, with 6s recognized as 9s in particular (165 out of 181).

## Structure du repository

**Français.**
- classification-knn-mindset.ipynb : notebook principal (k plus proches voisins sur Digits, hyperparamètres, évaluation, matrice de confusion)
- README.md : présentation du projet

**English.**
- classification-knn-mindset.ipynb: main notebook (k nearest neighbors on Digits, hyperparameters, evaluation, confusion matrix)
- README.md: project overview
