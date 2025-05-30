import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Configuration de la page
st.set_page_config(
    page_title="Dashboard Projet d'Émargement",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar navigation
st.sidebar.title("Navigation")
section = st.sidebar.radio("Aller à :", [
    "Accueil",
    "Décrochage scolaire",
    "Absentéisme",
    "Corrélation présence/réussite",
    "Clustering"
])

# Chargement des données
@st.cache_data
def load_data():
    stats = pd.read_csv("stats.csv")
    coeffs = pd.read_csv("coeffs_decrochage.csv", index_col=0).iloc[:, 0]
    importances = pd.read_csv("importances_rf.csv", index_col=0).iloc[:, 0]
    return stats, coeffs, importances

stats, coeffs, importances = load_data()
features = ['taux_presence', 'moyenne_cc', 'moyenne_exam', 'retard_moyen', 'nb_absences_injustifiees', 'distance_moyenne', 'connexion_moyenne', 'notif_moyenne']

# Accueil
if section == "Accueil":
    st.title("📊 Projet d'analyse prédictive d'émargement")
    st.markdown("""
    Bienvenue sur le tableau de bord interactif.
    
    **Objectifs :**
    - Prédire le décrochage scolaire
    - Analyser l'absentéisme
    - Comprendre les corrélations présence/réussite
    - Optimiser les groupes d'étudiants
    """)

# Décrochage scolaire
elif section == "Décrochage scolaire":
    st.header("1️⃣ Décrochage scolaire (Régression logistique)")
    st.bar_chart(coeffs.sort_values())
    with st.expander("📝 Interprétation"):
        st.write("""
        **Analyse :**
        - Plus une variable a un coefficient élevé (barre longue), plus elle influence fortement la probabilité de décrochage.
        - Les variables positives indiquent un effet positif sur le risque de décrochage (quand elles augmentent, le risque aussi).
        - Inversement, les variables négatives protègent contre le décrochage.
        - Exemple : Si le taux de présence a un coefficient négatif, cela signifie que plus un étudiant est présent, moins il risque de décrocher.
        """)

# Absentéisme
elif section == "Absentéisme":
    st.header("2️⃣ Prédiction de l'absentéisme (Random Forest)")
    st.bar_chart(importances.sort_values())
    with st.expander("📝 Interprétation"):
        st.write("""
        **Analyse :**
        - Les variables les plus importantes sont celles qui expliquent le mieux l’absentéisme.
        - Exemple : Si la distance au domicile est très importante, cela signifie qu’elle joue un rôle clé dans l’absence des étudiants.
        - Permet de cibler les actions de prévention sur les facteurs identifiés comme les plus influents.
        """)

# Corrélation présence/réussite
elif section == "Corrélation présence/réussite":
    st.header("3️⃣ Corrélation entre taux de présence et réussite académique")
    fig, ax = plt.subplots()
    scatter = ax.scatter(stats['taux_presence'], stats['moyenne_exam'], c=stats.get('groupe', 0), cmap='Set1', alpha=0.7)
    ax.set_xlabel("Taux de présence")
    ax.set_ylabel("Moyenne examen")
    ax.set_title("Présence vs. Moyenne d'examen")
    st.pyplot(fig)
    with st.expander("📝 Interprétation"):
        st.write("""
        **Analyse de la corrélation :**
        - Si les points montent vers la droite, il y a une corrélation positive : plus un étudiant est présent, meilleure est sa note.
        - Les points groupés en bas à gauche indiquent des étudiants à risque (faible présence, faibles notes).
        - Les couleurs par groupe permettent de voir si certains profils sont plus à risque que d’autres.
        """)

# Clustering
elif section == "Clustering":
    st.header("4️⃣ Clustering des étudiants")
    if 'groupe' in stats.columns:
        st.subheader("Répartition par groupe")
        st.bar_chart(stats['groupe'].value_counts())

        group_means = stats.groupby('groupe')[features].mean()
        st.subheader("Profil moyen (valeurs brutes)")
        st.dataframe(group_means)

        group_fmt = group_means.copy()
        group_fmt['taux_presence'] = (group_fmt['taux_presence'] * 100).round(1).astype(str) + '%'
        for col in features[1:]:
            group_fmt[col] = group_fmt[col].round(1)

        st.subheader("Profil moyen (formaté)")
        st.dataframe(group_fmt)

        st.subheader("Radar Chart comparatif")
        labels = group_means.columns.tolist()
        angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
        angles += angles[:1]
        fig_radar, ax_radar = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
        for grp, row in group_means.iterrows():
            vals = row.tolist() + [row.tolist()[0]]
            ax_radar.plot(angles, vals, label=f"Groupe {grp}")
            ax_radar.fill(angles, vals, alpha=0.15)
        ax_radar.set_thetagrids(np.degrees(angles[:-1]), labels)
        ax_radar.set_title("Radar Chart des groupes")
        ax_radar.legend()
        st.pyplot(fig_radar)

        with st.expander("📝 Analyse globale des groupes"):
            st.write("""
            **Résumé :**
            - Groupe faible risque : forte présence, bonnes notes, peu d’absences/retards.
            - Groupe intermédiaire : moyenne présence/notes, quelques absences.
            - Groupe haut risque : faible présence, notes basses, beaucoup d’absences.
            - Ces profils aident à adapter les dispositifs d’accompagnement.
            """)
    else:
        st.info("La colonne 'groupe' est manquante. Exécute le script de clustering au préalable.")

# Footer
st.markdown("---")
st.markdown("*Projet réalisé par Ryadh38 – 2024-2025*")
