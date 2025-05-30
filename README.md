📊 Projet : Analyse Prédictive d'Émargement et Réussite Étudiante

Auteur : Ryadh38Année : 2024-2025

🌟 Objectif du projet

Ce projet a pour but de :
1- Analyser les données d'émargement (présence/absence, retards, absences justifiées/injustifiées)
2- Prédire le risque de décrochage scolaire
3- Identifier les facteurs d'absentéisme
4- Optimiser les groupes d'étudiants grâce à du clustering
5- Créer un dashboard interactif sous Streamlit pour visualiser et explorer ces résultats

📂 Contenu du dépôt:

/Dashbord/ → Contient le fichier dashboard.py (application Streamlit)

stats.csv → Données agrégées par étudiant

coeffs_decrochage.csv → Résultats régression logistique (décrochage)

importances_rf.csv → Importances Random Forest (absentéisme)

🚀 Comment exécuter le dashboard ?

Prérequis :

Python 3.10 ou supérieur

Installer les packages nécessaires :

pip install streamlit pandas matplotlib numpy

Lancer l’application :

cd Dashbord
streamlit run dashboard.py

Une URL locale s’affichera (par ex. http://localhost:8501) → ouvrir dans le navigateur.

🖼 Captures du dashboard

🔹 Page Décrochage scolaire



🔹 Page Absentéisme



🔹 Corrélation Présence vs Réussite



🔹 Clustering & Profils



(⚠ Assure-toi d’ajouter tes propres captures dans un dossier /captures/ avant de pousser sur GitHub)

📊 Explications des sections

1️⃣ Décrochage scolaire

Méthode : Régression logistique

But : Prédire les étudiants à risque selon le taux de présence, notes, retards, etc.

Visualisation : Importance des variables → quelles variables augmentent ou diminuent le risque.

2️⃣ Absentéisme

Méthode : Random Forest

But : Identifier les principaux facteurs qui expliquent les absences.

Visualisation : Graphique d’importance des features.

3️⃣ Corrélation présence/réussite

But : Visualiser la relation entre la présence moyenne et les résultats académiques.

Visualisation : Scatter plot coloré par groupe.

4️⃣ Clustering

Méthode : KMeans (clustering non supervisé)

But : Grouper les étudiants selon leurs profils.

Visualisation : Barres, radar charts, tableaux comparatifs par groupe.

🛠 Méthodologie agile

Le projet a été structuré en sprints :

Sprint

Objectif

Avancement

Sprint 1

Nettoyage & préparation des données

✅ Terminé

Sprint 2

Modèles prédictifs (décrochage, absentéisme)

✅ Terminé

Sprint 3

Clustering et analyse des groupes

✅ Terminé

Sprint 4

Développement du dashboard Streamlit

✅ Terminé

Sprint 5

Documentation & finalisation GitHub

🔄 En cours

🔗 Liens utiles

Repo GitHub : https://github.com/Ryadh38/projet-emargement

Streamlit : https://streamlit.io/


Auteur :Belkhamsa Ryadh
