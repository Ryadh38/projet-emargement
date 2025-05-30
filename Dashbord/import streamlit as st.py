import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.sidebar.title("Navigation")
section = st.sidebar.radio("Choisissez une section", [
    "Accueil", 
    "Décrochage scolaire", 
    "Absentéisme", 
    "Corrélations", 
    "Clustering"
])
if section == "Accueil":
    st.title("Bienvenue sur le Dashboard")
    st.write("Objectif du projet : ...")

elif section == "Décrochage scolaire":
    

st.set_page_config(
    page_title="Dashboard Projet d'Émargement",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Titre principal
st.title("📊 Dashboard : Analyse prédictive de l'émargement et réussite étudiante")

# --------------------------
# 1. Chargement des données
# --------------------------
@st.cache_data
def load_data():
    stats = pd.read_csv("stats.csv")
    coeffs_df = pd.read_csv("coeffs_decrochage.csv", index_col=0)
    coeffs = coeffs_df.iloc[:, 0]
    importances_df = pd.read_csv("importances_rf.csv", index_col=0)
    importances = importances_df.iloc[:, 0]
    return stats, coeffs, importances

stats, coeffs, importances = load_data()

# Liste des colonnes à utiliser pour le clustering
features = [
    'taux_presence', 'moyenne_cc', 'moyenne_exam',
    'retard_moyen', 'nb_absences_injustifiees', 'distance_moyenne',
    'connexion_moyenne', 'notif_moyenne'
]

# --------------------------------------------
# 2. Partie 1 : Prédiction du décrochage scolaire
# --------------------------------------------
st.header("1️⃣ Prédiction du décrochage scolaire (Régression logistique)")
st.write(
    "Ce module utilise la régression logistique pour estimer le risque de décrochage "
    "(étudiant considéré comme ‘décrocheur’ si présence < 60 % ou note < 10)."
)
st.subheader("Importance des variables")
st.bar_chart(coeffs.sort_values(), height=300)

with st.expander("📝 Interprétation"):
    st.write("""
    **Analyse :**
    - Plus une variable a un coefficient élevé (barre longue), plus elle influence fortement la probabilité de décrochage.
    - Les variables positives augmentent le risque de décrochage.
    - Les variables négatives protègent contre le décrochage.
    - Exemple : un taux de présence négatif signifie que plus l’étudiant est présent, moins il décroche.
    """)

# ------------------------------------------------
# 3. Partie 2 : Prédiction de l'absentéisme (RF)
# ------------------------------------------------
st.header("2️⃣ Prédiction de l'absentéisme (Random Forest)")
st.write(
    "Le modèle Random Forest permet d'identifier les facteurs contribuant le plus "
    "à l'absentéisme séance par séance."
)
st.subheader("Importance des variables")
st.bar_chart(importances.sort_values(), height=300)

with st.expander("📝 Interprétation"):
    st.write("""
    **Analyse :**
    - Les variables les plus importantes expliquent le mieux l’absentéisme.
    - Exemple : Si la distance au domicile est importante, elle joue un rôle clé.
    - Cela permet de cibler les actions de prévention sur les bons leviers.
    """)

# ------------------------------------------------------
# 4. Partie 3 : Corrélation présence / réussite
# ------------------------------------------------------
st.header("3️⃣ Corrélation entre taux de présence et réussite académique")
st.write(
    "Scatter plot : chaque point = un étudiant, couleur = groupe (si clustering effectué)."
)
fig_corr, ax_corr = plt.subplots(figsize=(6, 4))
ax_corr.scatter(
    stats['taux_presence'],
    stats['moyenne_exam'],
    c=stats.get('groupe', 0),
    cmap='Set1',
    alpha=0.7
)
ax_corr.set_xlabel("Taux de présence")
ax_corr.set_ylabel("Moyenne examen")
ax_corr.set_title("Présence vs. Moyenne d'examen")
st.pyplot(fig_corr)

with st.expander("📝 Interprétation"):
    st.write("""
    **Analyse :**
    - Si les points montent vers la droite, il y a une corrélation positive : plus de présence, meilleures notes.
    - Les points en bas à gauche indiquent des étudiants à risque.
    - Les couleurs permettent d’identifier les profils par groupe.
    """)

# --------------------------------------------------------
# 5. Partie 4 : Clustering et optimisation des groupes
# --------------------------------------------------------
st.header("4️ Clustering et optimisation des groupes d'étudiants")

if 'groupe' in stats.columns:
    st.subheader("Répartition des étudiants par groupe")
    st.bar_chart(stats['groupe'].value_counts().sort_index(), height=250)

    group_means = stats.groupby('groupe')[features].mean()
    st.subheader("Profil moyen par groupe (valeurs brutes)")
    st.dataframe(group_means)

    # Formatage pour lisibilité
    group_means_fmt = group_means.copy()
    group_means_fmt['taux_presence'] = (
        (group_means_fmt['taux_presence'] * 100).round(1).astype(str) + '%'
    )
    for col in features[1:]:
        group_means_fmt[col] = group_means_fmt[col].round(1)

    st.subheader("Profil moyen par groupe (valeurs formatées)")
    st.dataframe(group_means_fmt)

    st.subheader("Interprétation des profils")
    cols = st.columns(2)
    for i, (grp, row) in enumerate(group_means_fmt.iterrows()):
        with cols[i % 2]:
            st.markdown(f"**Groupe {grp}**")
            st.markdown(f"- Taux de présence : {row['taux_presence']}")
            st.markdown(f"- Moyenne CC : {row['moyenne_cc']} /20")
            st.markdown(f"- Moyenne examen : {row['moyenne_exam']} /20")
            st.markdown(f"- Retard moyen : {row['retard_moyen']} min")
            st.markdown(f"- Absences injustifiées : {row['nb_absences_injustifiees']}")
            st.markdown(f"- Distance domicile : {row['distance_moyenne']} km")
            st.markdown(f"- Connexions Wi-Fi : {row['connexion_moyenne']}")
            st.markdown(f"- Notifications reçues : {row['notif_moyenne']}")
            st.markdown("---")

    with st.expander("📝 Analyse globale des groupes"):
        st.write("""
        **Résumé :**
        - Groupe faible risque : forte présence, bonnes notes, peu d’absences/retards.
        - Groupe intermédiaire : moyenne présence/notes, quelques absences.
        - Groupe haut risque : faible présence, notes basses, beaucoup d’absences.
        - Ces profils aident à adapter les dispositifs d’accompagnement.
        """)

    st.subheader("Comparaison des groupes (barres horizontales)")
    fig_barh, ax_barh = plt.subplots(figsize=(10, 5))
    group_means.T.plot(kind='barh', ax=ax_barh)
    ax_barh.set_xlabel("Valeur moyenne")
    ax_barh.set_ylabel("Indicateur")
    ax_barh.set_title("Profil moyen de chaque groupe")
    st.pyplot(fig_barh)

    st.subheader("Comparaison des groupes (Radar Chart)")
    labels = group_means.columns.tolist()
    num_vars = len(labels)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angles += angles[:1]  # pour fermer la boucle

    fig_radar, ax_radar = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    for grp, row in group_means.iterrows():
        vals = row.tolist()
        vals += vals[:1]  # fermer la boucle
        ax_radar.plot(angles, vals, label=f"Groupe {grp}")
        ax_radar.fill(angles, vals, alpha=0.15)
    ax_radar.set_thetagrids(np.degrees(angles[:-1]), labels)  # sans le dernier angle répété
    ax_radar.set_title("Radar Chart des profils de groupe")
    ax_radar.legend(loc='upper right')
    st.pyplot(fig_radar)

else:
    st.info("La colonne 'groupe' n'existe pas dans `stats`. Exécute d'abord ton script de clustering.")

# Footer
st.markdown("---")
st.markdown("*Projet d'analyse prédictive d'émargement – Ryadh38 – 2024-2025*")