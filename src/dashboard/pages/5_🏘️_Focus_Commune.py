"""
Page 5 - Focus Commune
Analyse détaillée d'une commune
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent / "utils"))
import config
import data_loader

st.set_page_config(page_title="Focus Commune", page_icon="🏘️", layout=config.LAYOUT)

st.title("🏘️ Focus Commune")
st.markdown("### Analyse détaillée par commune")
st.markdown("---")

# ============================================================================
# CHARGEMENT DONNÉES
# ============================================================================

with st.spinner("Chargement des données..."):
    df_communes = data_loader.load_communes_avec_gps()
    df_commerces_manquants = data_loader.load_commerces_manquants()
    df_etablissements = data_loader.load_etablissements()

if df_communes is None or df_etablissements is None:
    st.error("❌ Impossible de charger les données")
    st.stop()

# ============================================================================
# SÉLECTION COMMUNE
# ============================================================================

st.markdown("## 🔍 Sélection de la commune")

# Liste communes triée
communes_liste = sorted(df_communes['nom_commune'].unique().tolist())

commune_selectionnee = st.selectbox(
    "Choisir une commune",
    communes_liste,
    index=0
)

# Récupérer données commune
commune_data = df_communes[df_communes['nom_commune'] == commune_selectionnee].iloc[0]

st.markdown("---")

# ============================================================================
# FICHE IDENTITÉ COMMUNE
# ============================================================================

st.markdown(f"## 📊 {commune_selectionnee}")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("Établissements actifs", int(commune_data['nb_actifs']))

with col2:
    st.metric("Taux mortalité", f"{commune_data['taux_mortalite']:.1f}%")

with col3:
    st.metric("Score fragilité", f"{commune_data['score_fragilite']:.1f}")

with col4:
    st.metric("Profil", commune_data['profil'])

with col5:
    st.metric("Catégorie", commune_data['categorie_priorite'])

st.markdown("---")

# ============================================================================
# COMPARAISON DÉPARTEMENT
# ============================================================================

st.markdown("## 📊 Comparaison avec le département")

# Calculer moyennes département
taux_dept = df_communes['taux_mortalite'].mean()
score_dept = df_communes['score_fragilite'].mean()
actifs_dept = df_communes['nb_actifs'].mean()

comparaison = pd.DataFrame({
    'Indicateur': ['Établissements actifs', 'Taux mortalité (%)', 'Score fragilité'],
    'Commune': [
        int(commune_data['nb_actifs']),
        round(commune_data['taux_mortalite'], 1),
        round(commune_data['score_fragilite'], 1)
    ],
    'Moyenne département': [
        int(actifs_dept),
        round(taux_dept, 1),
        round(score_dept, 1)
    ]
})

comparaison['Écart'] = comparaison['Commune'] - comparaison['Moyenne département']
comparaison['Écart'] = comparaison['Écart'].round(1)

st.dataframe(comparaison, use_container_width=True, hide_index=True)

st.markdown("---")

# ============================================================================
# TOP 5 SECTEURS NAF COMMUNE
# ============================================================================

st.markdown("## 📊 Top 5 secteurs d'activité")

# Filtrer établissements de la commune
etab_commune = df_etablissements[
    df_etablissements['nom_commune'] == commune_selectionnee
].copy()

if len(etab_commune) > 0:
    # Compter par NAF classe
    secteurs = etab_commune['naf_libelle'].value_counts().head(5)

    fig = px.bar(
        x=secteurs.values,
        y=secteurs.index,
        orientation='h',
        labels={'x': 'Nombre établissements', 'y': 'Secteur'},
        color=secteurs.values,
        color_continuous_scale='Viridis'
    )

    fig.update_layout(height=300, showlegend=False)
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("Aucun établissement trouvé pour cette commune")

st.markdown("---")

# ============================================================================
# ÉVOLUTION TEMPORELLE COMMUNE
# ============================================================================

st.markdown("## 📈 Évolution 2015-2024")

# Calculer évolution pour la commune
evolution_commune = []

for annee in range(2015, 2025):
    nb_creations = len(etab_commune[etab_commune['annee_creation'] == annee])
    nb_fermetures = len(etab_commune[etab_commune['annee_fermeture'] == annee])

    evolution_commune.append({
        'annee': annee,
        'creations': nb_creations,
        'fermetures': nb_fermetures,
        'solde': nb_creations - nb_fermetures
    })

df_evolution = pd.DataFrame(evolution_commune)

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=df_evolution['annee'],
    y=df_evolution['creations'],
    mode='lines+markers',
    name='Créations',
    line=dict(color=config.COLOR_SUCCESS, width=2)
))

fig.add_trace(go.Scatter(
    x=df_evolution['annee'],
    y=df_evolution['fermetures'],
    mode='lines+markers',
    name='Fermetures',
    line=dict(color=config.COLOR_DANGER, width=2)
))

fig.update_layout(
    height=400,
    xaxis_title="Année",
    yaxis_title="Nombre",
    hovermode='x unified'
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ============================================================================
# COMMERCES MANQUANTS
# ============================================================================

if commune_data['categorie_priorite'] in ['Priorité A', 'Priorité B']:
    st.markdown("## 🏪 Commerces essentiels manquants")

    if df_commerces_manquants is not None:
        commerces_commune = df_commerces_manquants[
            df_commerces_manquants['nom_commune'] == commune_selectionnee
        ]

        if len(commerces_commune) > 0:
            manquants = commerces_commune.iloc[0]

            cols = st.columns(5)
            commerces = ['boulangerie', 'epicerie', 'pharmacie', 'boucherie', 'poste']

            for idx, commerce in enumerate(commerces):
                with cols[idx]:
                    if commerce in manquants and manquants[commerce] == 0:
                        st.error(f"❌ {commerce.capitalize()}")
                    else:
                        st.success(f"✅ {commerce.capitalize()}")
        else:
            st.info("Aucune donnée sur commerces manquants")

    st.markdown("---")

# ============================================================================
# COMMUNES SIMILAIRES
# ============================================================================

st.markdown("## 🔍 Communes similaires")

# Filtrer même profil et score proche
communes_similaires = df_communes[
    (df_communes['profil'] == commune_data['profil']) &
    (df_communes['score_fragilite'].between(
        commune_data['score_fragilite'] - 5,
        commune_data['score_fragilite'] + 5
    )) &
    (df_communes['nom_commune'] != commune_selectionnee)
].nsmallest(5, 'score_fragilite')[['nom_commune', 'taux_mortalite', 'score_fragilite', 'nb_actifs']]

communes_similaires.columns = ['Commune', 'Taux (%)', 'Score', 'Nb actifs']

st.dataframe(communes_similaires, use_container_width=True, hide_index=True)

st.markdown("---")
st.markdown(config.FOOTER_TEXT)
