import pandas as pd
import joblib
#Charger et nettoyer les données
df = pd.read_excel("donnees_projet_emargement.xlsx")
print(df.head())
# Supprimer les lignes où 'present' n'est pas renseigné
df = df.dropna(subset=['present'])
#Charger et nettoyer les données

df['retard'].fillna(0, inplace=True)
df['justificatif'].fillna(0, inplace=True)
df['note_cc'].fillna(df['note_cc'].mean(), inplace=True)
df['note_exam'].fillna(df['note_exam'].mean(), inplace=True)
# 3 Analyser et créer des “features” par étudiant:
# On regroupe les données par étudiant pour calculer ses moyennes/taux
stats = df.groupby('id_etudiant').agg({
    'present': 'mean',
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

print(stats.head())
#  4 Définir la cible à prédire (“label”):
# Si présence < 60% ou moyenne_exam < 10 => décrocheur (1), sinon (0)
stats['deccrochage'] = ((stats['taux_presence'] < 0.6) | (stats['moyenne_exam'] < 10)).astype(int)
# 5 Séparer les données en train/test:
from sklearn.model_selection import train_test_split

X = stats[['taux_presence', 'retard_moyen', 'nb_absences_injustifiees', 'moyenne_cc', 'moyenne_exam', 'distance_moyenne', 'connexion_moyenne', 'notif_moyenne']]
y = stats['deccrochage']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)
# 6  Choisir et entraîner un modèle IA:
from sklearn.linear_model import LogisticRegression

clf = LogisticRegression()
clf.fit(X_train, y_train)

#7️ Évaluer les performances:
from sklearn.metrics import classification_report

y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred))

#8️  Interpréter et sauvegarder le modèle:
joblib.dump(clf, 'modele_deccrochage.pkl')
coeffs = pd.Series(clf.coef_[0], index=X.columns)
print(coeffs.sort_values())

import pandas as pd
import matplotlib.pyplot as plt

# Supposons que tu as déjà calculé tes coefficients
coeffs = pd.Series(clf.coef_[0], index=X.columns)
coeffs.sort_values().plot(kind='barh', figsize=(8,5))
plt.title("Influence des variables sur le décrochage scolaire")
plt.xlabel("Poids (coefficient)")
plt.tight_layout()
plt.show()
