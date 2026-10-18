# Alim'confiance : recherche et cartographie des contrôles sanitaires

## Description courte

**Français.** Notebook d'exploration de la base Alim'confiance permettant de rechercher des établissements alimentaires par ville, niveau d'hygiène ou activité et de les afficher sur une carte interactive.

**English.** Notebook exploring the Alim'confiance database to search food establishments by city, hygiene level or activity and display them on an interactive map.

## Objectif du projet

**Français.** Rendre exploitables les résultats officiels des contrôles sanitaires en les nettoyant et en les structurant. Fournir un outil de recherche multicritère et une visualisation géographique par niveau d'hygiène. Proposer une interface à filtres interactifs sans connaissance préalable de la base.

**English.** Make the official health inspection results usable by cleaning and structuring them. Provide a multi-criteria search tool and a geographic visualization by hygiene level. Offer an interface with interactive filters requiring no prior knowledge of the database.

## Dataset

**Français.** Base Alim'confiance de la Direction générale de l'alimentation (DGAL), récupérée directement depuis le portail OpenDataSoft (export CSV, deux adresses d'export essayées tour à tour, avec repli possible sur un fichier local). Elle contient plus de 76 000 établissements avec leur dernier résultat de contrôle. Principales variables : nom de l'établissement, activité, synthèse de l'évaluation sanitaire (quatre niveaux), commune, adresse, date d'inspection et coordonnées GPS.

**English.** Alim'confiance database from the French Directorate General for Food (DGAL), retrieved directly from the OpenDataSoft portal (CSV export, two export addresses tried in turn, with a fallback to a local file). It contains more than 76,000 establishments with their latest inspection result. Main variables: establishment name, activity, sanitary evaluation summary (four levels), municipality, address, inspection date and GPS coordinates.

## Technologies et outils

**Français.**
- Python 3 et Jupyter Notebook
- pandas et NumPy pour le nettoyage et la recherche
- requests pour la récupération des données en ligne
- GeoPandas et Shapely pour la géométrie des points
- Folium pour les cartes interactives
- ipywidgets pour les filtres interactifs

**English.**
- Python 3 and Jupyter Notebook
- pandas and NumPy for cleaning and search
- requests for online data retrieval
- GeoPandas and Shapely for point geometry
- Folium for interactive maps
- ipywidgets for interactive filters

## Approche et modèles

**Français.**
- Preprocessing : détection automatique des colonnes utiles malgré les variations de nom entre versions de l'export, séparation de la colonne GPS en latitude et longitude, suppression des lignes sans coordonnées.
- Modèles : aucun modèle d'apprentissage automatique. L'approche est descriptive et repose sur le filtrage de données.
- Analyse : fonction de recherche combinant ville, niveau et activité, conversion en GeoDataFrame (EPSG:4326), marqueurs colorés selon les quatre niveaux officiels (vert, bleu, orange, rouge).
- Métriques : aucune métrique de performance. Le suivi porte sur les effectifs par niveau d'hygiène et le nombre d'établissements retournés par recherche.

**English.**
- Preprocessing: automatic detection of useful columns despite name variations between export versions, splitting of the GPS column into latitude and longitude, removal of rows without coordinates.
- Models: no machine learning model. The approach is descriptive and relies on data filtering.
- Analysis: search function combining city, level and activity, conversion to a GeoDataFrame (EPSG:4326), markers colored by the four official levels (green, blue, orange, red).
- Metrics: no performance metric. Monitoring covers counts per hygiene level and the number of establishments returned by each search.

## Résultats

**Français.**
- Chargement automatisé de la base complète sans téléchargement manuel, avec gestion des interruptions de service du portail.
- Recherche multicritère fonctionnelle (exemple documenté : établissements de niveau satisfaisant à Rennes) avec tableau lisible des résultats.
- Carte Folium centrée automatiquement sur les résultats, avec fenêtre d'information par établissement (nom, activité, niveau, adresse) et repli sur le centre de la France si la recherche est vide.
- Interface interactive à menus déroulants et bouton de recherche affichant les 20 premiers résultats et la carte associée.

**English.**
- Automated loading of the full database without manual download, with handling of portal service interruptions.
- Working multi-criteria search (documented example: satisfactory level establishments in Rennes) with a readable results table.
- Folium map automatically centered on the results, with an information popup per establishment (name, activity, level, address) and a fallback to the center of France when the search is empty.
- Interactive interface with dropdown menus and a search button displaying the first 20 results and the matching map.

## Structure du repository

**Français.**
- alimconfiance.ipynb : notebook principal (import, nettoyage, recherche, cartographie, filtres interactifs)
- README.md : présentation du projet

**English.**
- alimconfiance.ipynb: main notebook (import, cleaning, search, mapping, interactive filters)
- README.md: project overview
