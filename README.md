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

🖼 Captures du dashboard:
🔹 Acceuil:
<img width="956" alt="Acceuil" src="https://github.com/user-attachments/assets/9e188851-7a76-4b43-a8d9-0a37483179c1" />


🔹 Page Décrochage scolaire
<img width="956" alt="Décrochage scolaire" src="https://github.com/user-attachments/assets/333f26fd-229f-4ff6-8b60-91f1a12a36e6" />


🔹 Page Absentéisme


<img width="956" alt="Absentéisme" src="https://github.com/user-attachments/assets/b68f7586-e1ee-4020-bb70-f7be794a3c39" />

🔹 Corrélation Présence vs Réussite

![graphe présence-réussite](https://github.com/user-attachments/assets/0f25fa88-58d2-4d37-a704-724c1f56491f)

<img width="957" alt="Corrélation présence-réussite" src="https://github.com/user-attachments/assets/fa716ef9-fa51-4808-8bbe-a447b12a4557" />

🔹 Clustering & Profils
<img width="959" alt="Clustering1" src="https://github.com/user-attachments/assets/8bb8746b-7ba7-4e3a-b0ec-2c08bd53d053" />
<img width="959" alt="Clustering2" src="https://github.com/user-attachments/assets/4d329cc6-91bf-409a-918a-812e93cb1dbd" />


![Clustering-radarChartDesGroupes](https://github.com/user-attachments/assets/836b2dd7-5e9b-469a-b999-c46aa7f66d1a)
<img width="959" alt="interpretation-RadarChart" src="https://github.com/user-attachments/assets/5cbbfb50-f5fa-4b47-a118-954e6802befb" />

📊 Explications des sections:

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


🔗 Liens utiles

Repo GitHub : https://github.com/Ryadh38/projet-emargement

Streamlit : https://streamlit.io/


Auteur :Belkhamsa Ryadh
