# Projet : Analyse Prédictive d'Émargement et Réussite Étudiante. 

Auteur : Ryadh38Année : 2024-2025. 

## Objectif du projet:  

Ce projet a pour but de :

1- Analyser les données d'émargement (présence/absence, retards, absences justifiées/injustifiées). 


2- Prédire le risque de décrochage scolaire. 


3- Identifier les facteurs d'absentéisme. 


4- Optimiser les groupes d'étudiants grâce à du clustering. 


5- Créer un dashboard interactif sous Streamlit pour visualiser et explorer ces résultats. 


## Structure du projet:

.
├── CLUSTERING/
│   └── Scripts et analyses pour segmenter les étudiants en groupes. 


├── Corelation/
│   └── Étude des corrélations entre présence et réussite académique. 


├── Dashbord/
│   └── Code du dashboard interactif Streamlit. 


├── Prédiction du décrochage/
│   └── Modèles pour prédire les risques de décrochage scolaire. 


├── Prévision d’absentéisme/
│   └── Modèles pour anticiper les absences à venir. 


├── l’analyse de la corrélation présenceréussite/
│   └── Scripts détaillés d’analyse des liens entre assiduité et performances. 


├── README.md
└── donnees_projet_emargement.xlsx (données source). 


## Contenu du dépôt:



/Dashbord/ → Contient le fichier dashboard.py (application Streamlit). 


stats.csv → Données agrégées par étudiant. 


coeffs_decrochage.csv → Résultats régression logistique (décrochage). 


importances_rf.csv → Importances Random Forest (absentéisme). 



## Lancer le projet localement



### Cloner le dépôt :

git clone https://github.com/Ryadh38/projet-emargement.git. 

### Installer les dépendances :

pip install -r requirements.txt. 

### Lancer le dashboard Streamlit :

cd Dashbord. 
streamlit run dashbord.py. 

## Captures du dashboard:


### Acceuil:


<img width="956" alt="Acceuil" src="https://github.com/user-attachments/assets/9e188851-7a76-4b43-a8d9-0a37483179c1" />. 


### Page Décrochage scolaire:


<img width="956" alt="Décrochage scolaire" src="https://github.com/user-attachments/assets/333f26fd-229f-4ff6-8b60-91f1a12a36e6" />.


### Page Absentéisme:


<img width="956" alt="Absentéisme" src="https://github.com/user-attachments/assets/b68f7586-e1ee-4020-bb70-f7be794a3c39" />. 


### Corrélation Présence vs Réussite:

![graphe présence-réussite](https://github.com/user-attachments/assets/0f25fa88-58d2-4d37-a704-724c1f56491f). 



<img width="957" alt="Corrélation présence-réussite" src="https://github.com/user-attachments/assets/fa716ef9-fa51-4808-8bbe-a447b12a4557" />.

 

### Clustering & Profils:



<img width="959" alt="Clustering1" src="https://github.com/user-attachments/assets/8bb8746b-7ba7-4e3a-b0ec-2c08bd53d053" />. 



<img width="959" alt="Clustering2" src="https://github.com/user-attachments/assets/4d329cc6-91bf-409a-918a-812e93cb1dbd" />. 


![Clustering-radarChartDesGroupes](https://github.com/user-attachments/assets/836b2dd7-5e9b-469a-b999-c46aa7f66d1a)
<img width="959" alt="interpretation-RadarChart" src="https://github.com/user-attachments/assets/5cbbfb50-f5fa-4b47-a118-954e6802befb" />. 



## Explications des sections:

### Décrochage scolaire:

Méthode : Régression logistique. 

But : Prédire les étudiants à risque selon le taux de présence, notes, retards, etc. 

Visualisation : Importance des variables → quelles variables augmentent ou diminuent le risque.

### Absentéisme:

Méthode : Random Forest

But : Identifier les principaux facteurs qui expliquent les absences.

Visualisation : Graphique d’importance des features.

### Corrélation présence/réussite:

But : Visualiser la relation entre la présence moyenne et les résultats académiques.

Visualisation : Scatter plot coloré par groupe.

### Clustering:

Méthode : KMeans (clustering non supervisé). 

But : Grouper les étudiants selon leurs profils.

Visualisation : Barres, radar charts, tableaux comparatifs par groupe.



## Le projet a été structuré en sprints :


### Sprint 1:

Nettoyage & préparation des données.

✅ Terminé

### Sprint 2:

Modèles prédictifs (décrochage, absentéisme).

✅ Terminé

### Sprint 3:

Clustering et analyse des groupes.

✅ Terminé

### Sprint 4

Développement du dashboard Streamlit.

✅ Terminé

### Sprint 5

Documentation & finalisation GitHub.

## Description des modules:

1-Prédiction du décrochage	Utilisation de régression logistique pour identifier les étudiants à risque selon leur assiduité et leurs résultats.

2-Prévision d’absentéisme	Modèles Random Forest pour anticiper les absences et comprendre les facteurs principaux.

3-Corrélation présence/réussite	Étude de la relation entre présence en cours et performances académiques (notes aux examens).

4- Clustering	Regroupement des étudiants selon leurs profils d’assiduité, de performance et de comportement pour identifier des segments homogènes.

## Liens utiles

Repo GitHub : https://github.com/Ryadh38/projet-emargement.

Streamlit : https://streamlit.io/.


## Outils utilisés par partie:

### Prédiction du décrochage scolaire
Outil principal :

Régression logistique (via scikit-learn)

Autres :

pandas → pour gérer les données

matplotlib → pour visualiser les coefficients

### Prévision d’absentéisme
Outil principal :

Random Forest Classifier (scikit-learn)

Autres :

pandas → pour les données

matplotlib → pour tracer l’importance des variables

### Corrélation présence / réussite

 Outil principal :

Analyse visuelle par scatter plot (matplotlib)

Autres :

pandas → pour calculer les moyennes

Optionnellement numpy → pour calculer des corrélations numériques

 ### Clustering (optimisation des groupes)
Outil principal :

KMeans Clustering (scikit-learn)

Autres :

StandardScaler (scikit-learn) → pour normaliser les données

matplotlib → pour barplots, radar charts

pandas → pour grouper et résumer les stats

### Dashboard interactif/

Outil principal :

Streamlit → pour construire le tableau de bord web interactif

## Résumé général des librairies Python utilisées :

pandas

numpy

scikit-learn

matplotlib

streamlit




Auteur :Belkhamsa Ryadh
