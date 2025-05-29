import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# 1. Charger et nettoyer les données
df = pd.read_excel("donnees_projet_emargement.xlsx")
df['retard'] = df['retard'].fillna(0)
df['justificatif'] = df['justificatif'].fillna(0)
df['note_cc'] = df['note_cc'].fillna(df['note_cc'].mean())
df['note_exam'] = df['note_exam'].fillna(df['note_exam'].mean())

# 2. Créer le DataFrame stats
stats = df.groupby('id_etudiant').agg({
    'present': 'mean',  # taux de présence
    'retard': 'mean',
    'justificatif': lambda x: ((df.loc[x.index, 'present'] == 0) & (x == 0)).sum(),
    'note_cc': 'mean',
    'note_exam': 'mean',
    'distance_domicile': 'mean',
    'connecte_wifi': 'mean',
    'nb_notifications': 'mean'
}).reset_index()
stats.rename(columns={
    'present': 'taux_presence',
    'retard': 'retard_moyen',
    'justificatif': 'nb_absences_injustifiees',
    'note_cc': 'moyenne_cc',
    'note_exam': 'moyenne_exam',
    'distance_domicile': 'distance_moyenne',
    'connecte_wifi': 'connexion_moyenne',
    'nb_notifications': 'notif_moyenne'
}, inplace=True)

# 3. Préparation des features pour le clustering
features = [
    'taux_presence', 'moyenne_cc', 'moyenne_exam',
    'retard_moyen', 'nb_absences_injustifiees', 'distance_moyenne'
]
X_clust = stats[features]

# 4. Normalisation
scaler = StandardScaler()
X_clust_scaled = scaler.fit_transform(X_clust)

# 5. Clustering KMeans
k = 3
kmeans = KMeans(n_clusters=k, random_state=42)
stats['groupe'] = kmeans.fit_predict(X_clust_scaled)

# 6. Visualisation (optionnelle)
plt.figure(figsize=(8,6))
plt.scatter(stats['taux_presence'], stats['moyenne_exam'], c=stats['groupe'], cmap='Set1')
plt.xlabel('Taux de présence')
plt.ylabel('Moyenne examen')
plt.title('Clustering des étudiants (présence vs. réussite)')
plt.colorbar(label='Groupe')
plt.show()

# 7. Statistiques par groupe
print(stats.groupby('groupe')[features].mean())


# Calcul des moyennes par groupe
group_means = stats.groupby('groupe')[features].mean()

# Transpose pour avoir les features sur l’axe Y
group_means.T.plot(kind='barh', figsize=(10, 6))
plt.title("Profil moyen de chaque groupe d'étudiants")
plt.xlabel("Valeur moyenne")
plt.ylabel("Indicateur")
plt.legend(title='Groupe')
plt.tight_layout()
plt.show()

