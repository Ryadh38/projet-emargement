import pandas as pd
import matplotlib.pyplot as plt

#1️ Préparer les données:
df = pd.read_excel("donnees_projet_emargement.xlsx")

# Nettoyage classique
df['retard'] = df['retard'].fillna(0)
df['justificatif'] = df['justificatif'].fillna(0)
df['note_cc'] = df['note_cc'].fillna(df['note_cc'].mean())
df['note_exam'] = df['note_exam'].fillna(df['note_exam'].mean())
#2️ Variable cible “sera-t-il absent ?”:
df['absent'] = 1 - df['present']   # 1 = absent, 0 = présent
# 3️⃣ Features (variables explicatives):
# Pour simplifier : on prend des features directes (mais on peut ajouter l’historique !)
features = [
    'retard', 'justificatif', 'note_cc', 'note_exam',
    'distance_domicile', 'connecte_wifi', 'nb_notifications'
]
X = df[features]
y = df['absent']
#4️⃣ Séparer train/test:
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)
#5️⃣ Choisir et entraîner un modèle:
from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier(n_estimators=100)
clf.fit(X_train, y_train)
#6️⃣ Évaluer la performance: 
from sklearn.metrics import classification_report

y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred))
#7️⃣ Analyser les résultats:
import pandas as pd
import matplotlib.pyplot as plt

importances = pd.Series(clf.feature_importances_, index=features)
importances.sort_values().plot(kind='barh')
plt.title("Importance des variables pour la prédiction de l'absentéisme")
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

importances = pd.Series(clf.feature_importances_, index=X.columns)
importances.sort_values().plot(kind='barh', figsize=(8,5))
plt.title("Importance des variables pour la prédiction de l'absentéisme")
plt.xlabel("Importance")
plt.tight_layout()
plt.show()

