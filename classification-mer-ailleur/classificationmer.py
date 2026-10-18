import os
import random
from PIL import Image
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import numpy as np
from skimage.feature import hog
import joblib

path_mer      = r"C:\Users\ferja\Desktop\IAA\Init\Init\Mer"
path_ailleurs = r"C:\Users\ferja\Desktop\IAA\Init\Init\Ailleurs"
path_test     = r"C:\Users\ferja\Desktop\IAA\Data CC2\Data CC2"

extensions = ('.jpg', '.jpeg', '.png')


def explore_directory(path, label):
    files = os.listdir(path)
    images = [f for f in files if f.lower().endswith(extensions)]
    print(f"  Nombre d images : {len(images)}")
    formats = {}
    tailles = {}
    erreurs = []
    for name in images:
        full_path = os.path.join(path, name)
        try:
            img = Image.open(full_path)
            fmt = img.format if img.format else name.split('.')[-1].upper()
            formats[fmt] = formats.get(fmt, 0) + 1
            tailles[img.size] = tailles.get(img.size, 0) + 1
        except Exception as e:
            erreurs.append((name, str(e)))
    print(f"  Formats : {formats}")
    print(f"  Tailles differentes : {len(tailles)}")
    if erreurs:
        print(f"  Images corrompues : {erreurs}")
    return images

images_mer      = explore_directory(path_mer,      "mer")
images_ailleurs = explore_directory(path_ailleurs, "ailleurs")


def resizeImage(i, h, l):
    return i.resize((l, h))

def computeHisto(i):
    h = i.histogram()
    total = sum(h)
    return [v / total for v in h]

def computePixelBW(i):
    pixels = list(i.convert("L").getdata())
    return [p / 255.0 for p in pixels]

def computeHOG(i):
    features = hog(np.array(i.convert("L")), orientations=9,
                   pixels_per_cell=(8, 8), cells_per_block=(2, 2), block_norm="L2-Hys")
    return list(features)

def computeHOGplusHisto(i):
    return computeHOG(i) + computeHisto(i)


# Mapping descripteur -> fonction de calcul
COMPUTE_MAP = {
    "histo"    : computeHisto,
    "bw"       : computePixelBW,
    "hog"      : computeHOG,
    "hog_histo": computeHOGplusHisto,
}

# Cle du dictionnaire S correspondant a chaque descripteur
CLE_MAP = {
    "histo"    : "X_histo",
    "bw"       : "X_pixelbw",
    "hog"      : "X_hog",
    "hog_histo": "X_hog_histo",
}

DESCRIPTEUR_LABELS = {
    "histo"    : "Histogramme RGB",
    "bw"       : "Pixels BW",
    "hog"      : "HOG",
    "hog_histo": "HOG+Histo",
}


def buildSampleFromPath(path1, path2, l=64, h=64):
    S = []
    for path, label in [(path1, +1), (path2, -1)]:
        for name in os.listdir(path):
            if name.lower().endswith(extensions):
                full_path = os.path.join(path, name)
                img = Image.open(full_path).convert("RGB")
                img_r = resizeImage(img, h, l)
                S.append({
                    "name_path"        : full_path,
                    "resized_image"    : img_r,
                    "X_histo"          : computeHisto(img_r),
                    "X_pixelbw"        : computePixelBW(img_r),
                    "X_hog"            : computeHOG(img_r),
                    "X_hog_histo"      : computeHOGplusHisto(img_r),
                    "y_true_class"     : label,
                    "y_predicted_class": None
                })
    random.shuffle(S)
    return S

S = buildSampleFromPath(path_mer, path_ailleurs, l=64, h=64)
print(f"Taille echantillon : {len(S)}")
print(f"Longueur histogramme : {len(S[0]['X_histo'])}")
print(f"Longueur HOG : {len(S[0]['X_hog'])}")
print(f"Longueur HOG+Histo : {len(S[0]['X_hog_histo'])}")


ALGO_MAP = {
    "NaiveBayes"        : GaussianNB,
    "SVM"               : SVC,
    "LogisticRegression": LogisticRegression,
    "DecisionTree"      : DecisionTreeClassifier,
}

algo_naivebayes   = {"name": "NaiveBayes",         "hyper_param": {}}
algo_svm          = {"name": "SVM",                "hyper_param": {"kernel": "rbf", "C":1.6}}
algo_logistic     = {"name": "LogisticRegression", "hyper_param": {"max_iter": 1000}}
algo_decisiontree = {"name": "DecisionTree",       "hyper_param": {"max_depth": 10}}



#Fit fonction des des descripteurs et de l'algo 

def fitFromDescripteur(S, algo=algo_naivebayes, descripteur="histo", n_pca=None):
    cle = CLE_MAP[descripteur]
    X = [ex[cle] for ex in S]
    y = [ex["y_true_class"] for ex in S]
    clf = ALGO_MAP[algo["name"]](**algo["hyper_param"])
    if n_pca:
        model = Pipeline([
            ("scaler", StandardScaler()),
            ("pca",    PCA(n_components=n_pca)),
            ("clf",    clf)
        ])
    else:
        model = clf
    model.fit(X, y)
    return model

def predictOneImage(image_dict, model, descripteur="histo"):
    cle = CLE_MAP[descripteur]
    pred = model.predict([image_dict[cle]])[0]
    image_dict["y_predicted_class"] = pred
    return pred

def predictFromDescripteur(S, model, descripteur="histo"):
    return [predictOneImage(ex, model, descripteur) for ex in S]

def erreur_empirique(S):
    erreurs = sum(1 for ex in S if ex["y_predicted_class"] != ex["y_true_class"])
    return erreurs / len(S)

def cross_validation(S, algo=algo_naivebayes, k=5, descripteur="histo", verbose=False, n_pca=None):
    n = len(S)
    fold_size = n // k
    erreurs_folds = []
    for i in range(k):
        start   = i * fold_size
        end     = start + fold_size if i < k - 1 else n
        S_test  = S[start:end]
        S_train = S[:start] + S[end:]
        for ex in S_test:
            ex["y_predicted_class"] = None
        model_fold = fitFromDescripteur(S_train, algo, descripteur, n_pca)
        predictFromDescripteur(S_test, model_fold, descripteur)
        err_fold = erreur_empirique(S_test)
        erreurs_folds.append(err_fold)
        if verbose:
            print(f"  Fold {i+1}/{k} : {err_fold:.4f}")
    return sum(erreurs_folds) / k


# Test initial NaiveBayes sur histogramme
model       = fitFromDescripteur(S, algo_naivebayes, "histo")
predictions = predictFromDescripteur(S, model, "histo")
print(f"Premieres 10 predictions    : {predictions[:10]}")
print(f"Premieres 10 classes reelles: {[ex['y_true_class'] for ex in S[:10]]}")

err = erreur_empirique(S)
print(f"Erreur empirique (train) : {err:.4f}")

# CV NaiveBayes sur chaque descripteur
for desc in ["histo", "bw", "hog", "hog_histo"]:
    ecv = cross_validation(S, algo=algo_naivebayes, descripteur=desc)
    print(f"CV NaiveBayes {DESCRIPTEUR_LABELS[desc]} : {ecv:.4f}")

# CV NaiveBayes HOG+Histo avec PCA
ecv_pca = cross_validation(S, algo=algo_naivebayes, descripteur="hog_histo", n_pca=50)
print(f"CV NaiveBayes HOG+Histo + PCA(50) : {ecv_pca:.4f}")


# Comparaison des 5 algos x 4 descripteurs
"""
print(f"\n{'Algo':<20} {'Histo RGB':^18} {'Pixels BW':^18} {'HOG':^18} {'HOG+Histo':^18}")
print("-" * 92)

for algo in [algo_naivebayes, algo_svm, algo_logistic, algo_decisiontree]:
    resultats_desc = []
    for desc in ["histo", "bw", "hog", "hog_histo"]:
        m = fitFromDescripteur(S, algo, desc)
        predictFromDescripteur(S, m, desc)
        ee  = erreur_empirique(S)
        ecv = cross_validation(S, algo=algo, descripteur=desc)
        resultats_desc.append((ee, ecv))
    nom = algo['name']
    print(f"{nom:<20}", end="")
    for ee, ecv in resultats_desc:
        print(f" EE={ee:.3f} ECV={ecv:.3f}  ", end="")
    print()
"""

# Grid search SVM : kernel x C
"""
valeurs_C      = list(np.arange(0.1, 2.1, 0.1))
valeurs_kernel = ["rbf", "linear", "poly"]

meilleure_err   = float("inf")
meilleur_kernel = None
meilleur_C      = None
resultats_grid  = []

print("\nRecherche du meilleur kernel et C pour SVM :")
for kernel in valeurs_kernel:
    print(f"\n  kernel={kernel}")
    for C in valeurs_C:
        algo_test = {"name": "SVM", "hyper_param": {"kernel": kernel, "C": C}}
        err = cross_validation(S, algo=algo_test, descripteur="histo")
        resultats_grid.append((kernel, C, err))
        print(f"    C={C:.1f} -> {err:.4f}")
        if err < meilleure_err:
            meilleure_err   = err
            meilleur_kernel = kernel
            meilleur_C      = C

print("\nMeilleur C par kernel :")
for kernel in valeurs_kernel:
    errs = [(C, err) for (k, C, err) in resultats_grid if k == kernel]
    best_C, best_err = min(errs, key=lambda x: x[1])
    print(f"  {kernel} -> C={best_C:.2f}, erreur={best_err:.4f}")

print(f"\nMeilleur kernel : {meilleur_kernel}")
print(f"Meilleur C      : {meilleur_C:.2f}")
print(f"Erreur CV min   : {meilleure_err:.4f}")

algo_svm["hyper_param"]["kernel"] = meilleur_kernel
algo_svm["hyper_param"]["C"]      = meilleur_C

col_w = 12
print("\n" + "=" * 52)
print(f"{'Tableau SVM grid search':^52}")
print("=" * 52)
print(f"{'C':<10}" + "".join(f"{k:^{col_w}}" for k in valeurs_kernel))
print("-" * 52)
for idx_C, C in enumerate(valeurs_C):
    ligne = f"{C:<10.1f}"
    for idx_k, kernel in enumerate(valeurs_kernel):
        err_val = resultats_grid[idx_k * len(valeurs_C) + idx_C][2]
        cell = f"*{err_val:.4f}*" if (kernel == meilleur_kernel and C == meilleur_C) else f"{err_val:.4f}"
        ligne += f"{cell:^{col_w}}"
    print(ligne)
print("=" * 52)
"""

# Selection de la meilleure combinaison algo + descripteur
"""
meilleure_ecv_globale = float("inf")
meilleur_algo         = None
meilleur_descripteur  = None

for algo_test in [algo_naivebayes, {"name": "SVM", "hyper_param": {"kernel": meilleur_kernel, "C": meilleur_C}}, algo_logistic, algo_decisiontree]:
    for desc in ["histo", "bw", "hog", "hog_histo"]:
        ecv = cross_validation(S, algo=algo_test, descripteur=desc)
        if ecv < meilleure_ecv_globale:
            meilleure_ecv_globale = ecv
            meilleur_algo         = algo_test
            meilleur_descripteur  = desc

print(f"\nMeilleure combinaison : {meilleur_algo['name']} + {DESCRIPTEUR_LABELS[meilleur_descripteur]}")
print(f"ECV : {meilleure_ecv_globale:.4f}")
"""

def sauvegarder_modele(model, chemin="modele_final.pkl"):
    joblib.dump(model, chemin)
    print(f"Modele sauvegarde : {chemin}")

def charger_modele(chemin="modele_final.pkl"):
    model = joblib.load(chemin)
    print(f"Modele charge : {chemin}")
    return model

def predire_nouvelles_images(path_test, model, descripteur, l=64, h=64):
    compute_fn = COMPUTE_MAP[descripteur]
    resultats = []
    for name in os.listdir(path_test):
        if name.lower().endswith(extensions):
            full_path = os.path.join(path_test, name)
            img = Image.open(full_path).convert("RGB")
            img_r = resizeImage(img, h, l)
            pred = model.predict([compute_fn(img_r)])[0]
            resultats.append((name, pred))
    return resultats

def generer_fichier_equipe(resultats, algo, err_empirique, err_cv,
                            nom_equipe="Virgule",
                            auteurs="Sonia, Hedi, Yasmine"):
    nom_fichier = f"{nom_equipe}.txt"
    hyper = algo["hyper_param"]
    hyper_str = ", ".join(f"{k}={v}" for k, v in hyper.items()) if hyper else "aucun hyperparametre"
    with open(nom_fichier, "w", encoding="utf-8") as f:
        f.write(f"# {auteurs} (Equipe {nom_equipe})\n")
        f.write(f"# {algo['name']}\n")
        f.write(f"# {hyper_str}\n")
        f.write(f"# Descripteur : Histogramme \n")
        for nom_image, pred in resultats:
            f.write(f"{nom_image} {'+1' if pred == 1 else '-1'}\n")
        f.write(f"# EE = {err_empirique:.2f}\n")
        f.write(f"# ER = {err_cv:.2f}\n")
    print(f"Fichier genere : {nom_fichier}")
    return nom_fichier


print("\nApprentissage du modele final sur tout S :")
model_final = fitFromDescripteur(S, algo_svm, "histo")
predictFromDescripteur(S, model_final, "histo")
err_emp = erreur_empirique(S)
print(f"EE : {err_emp:.4f}")

err_reelle = cross_validation(S, algo_svm, 5, "histo")
print(f"ER : {err_reelle:.4f}")

sauvegarder_modele(model_final, "modele_final.pkl")

print("\nPrediction sur nouvelles images :")
resultats = predire_nouvelles_images(path_test, model_final, "histo")
generer_fichier_equipe(resultats, algo_svm, err_emp, err_reelle)

