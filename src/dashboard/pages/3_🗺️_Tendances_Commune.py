"""
Page 3 - Tendances par commune
Carte interactive GPS et classements
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

st.set_page_config(page_title="Tendances par commune", page_icon="🗺️", layout=config.LAYOUT)

st.title("🗺️ Tendances par commune")
st.markdown("### Carte interactive et classements")
st.markdown("---")

# ============================================================================
# CHARGEMENT DONNÉES
# ============================================================================

with st.spinner("Chargement des données..."):
    df_communes = data_loader.load_communes_avec_gps()

if df_communes is None:
    st.error("❌ Impossible de charger les données")
    st.stop()

# ============================================================================
# FILTRES
# ============================================================================

st.markdown("## 🔍 Filtres")

col1, col2, col3 = st.columns(3)

with col1:
    profils_disponibles = ['Tous'] + sorted(df_communes['profil'].dropna().unique().tolist())
    filtre_profil = st.selectbox("Profil", profils_disponibles)

with col2:
    categories_disponibles = ['Tous'] + sorted(df_communes['categorie_priorite'].dropna().unique().tolist())
    filtre_categorie = st.selectbox("Catégorie priorité", categories_disponibles)

with col3:
    indicateur = st.selectbox("Indicateur carte", ["Taux mortalité", "Score fragilité"])

# Appliquer filtres
df_filtre = df_communes.copy()

if filtre_profil != 'Tous':
    df_filtre = df_filtre[df_filtre['profil'] == filtre_profil]

if filtre_categorie != 'Tous':
    df_filtre = df_filtre[df_filtre['categorie_priorite'] == filtre_categorie]

# Filtrer communes avec GPS
df_filtre = df_filtre[df_filtre['latitude'].notna() & df_filtre['longitude'].notna()]

st.markdown(f"**{len(df_filtre)} communes** affichées (sur {len(df_communes)} total)")

st.markdown("---")

# ============================================================================
# KPI GLOBAUX
# ============================================================================

st.markdown("## 📊 Indicateurs globaux")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Communes", len(df_filtre))

with col2:
    taux_moyen = df_filtre['taux_mortalite'].mean()
    st.metric("Taux mortalité moyen", f"{taux_moyen:.1f}%")

with col3:
    score_moyen = df_filtre['score_fragilite'].mean() if 'score_fragilite' in df_filtre.columns else 0
    st.metric("Score fragilité moyen", f"{score_moyen:.1f}")

with col4:
    nb_prioritaires = len(df_filtre[df_filtre['categorie_priorite'].isin(['Priorité A', 'Priorité B'])])
    st.metric("Communes prioritaires", nb_prioritaires)

st.markdown("---")

# ============================================================================
# CARTE INTERACTIVE GPS
# ============================================================================

st.markdown(f"## 🗺️ Carte interactive — {indicateur}")

# Préparer données pour carte
if indicateur == "Taux mortalité":
    colonne_valeur = 'taux_mortalite'
    titre_couleur = 'Taux (%)'
else:
    colonne_valeur = 'score_fragilite'
    titre_couleur = 'Score'

# Carte scatter mapbox
fig = px.scatter_mapbox(
    df_filtre,
    lat='latitude',
    lon='longitude',
    color=colonne_valeur,
    size='nb_actifs',
    hover_name='nom_commune',
    hover_data={
        'latitude': False,
        'longitude': False,
        'taux_mortalite': ':.1f',
        'score_fragilite': ':.1f',
        'nb_actifs': True,
        'profil': True,
        'categorie_priorite': True
    },
    color_continuous_scale=['green', 'orange', 'red'],
    labels={colonne_valeur: titre_couleur},
    zoom=8,
    height=600
)

fig.update_layout(
    mapbox_style="open-street-map",
    margin={"r":0,"t":0,"l":0,"b":0}
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ============================================================================
# CLASSEMENTS
# ============================================================================

st.markdown("## 📊 Classements")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🟢 Top 10 communes dynamiques")
    st.markdown("*Taux mortalité le plus faible*")

    top_dynamiques = df_filtre.nsmallest(10, 'taux_mortalite')[
        ['nom_commune', 'taux_mortalite', 'nb_actifs', 'profil', 'categorie_priorite']
    ].copy()

    top_dynamiques.columns = ['Commune', 'Taux (%)', 'Nb actifs', 'Profil', 'Catégorie']
    top_dynamiques['Taux (%)'] = top_dynamiques['Taux (%)'].round(1)

    st.dataframe(top_dynamiques, use_container_width=True, hide_index=True)

with col2:
    st.markdown("### 🔴 Top 10 communes fragiles")
    st.markdown("*Taux mortalité le plus élevé*")

    top_fragiles = df_filtre.nlargest(10, 'taux_mortalite')[
        ['nom_commune', 'taux_mortalite', 'nb_actifs', 'profil', 'categorie_priorite']
    ].copy()

    top_fragiles.columns = ['Commune', 'Taux (%)', 'Nb actifs', 'Profil', 'Catégorie']
    top_fragiles['Taux (%)'] = top_fragiles['Taux (%)'].round(1)

    st.dataframe(top_fragiles, use_container_width=True, hide_index=True)

st.markdown("---")

# ============================================================================
# RÉPARTITION PAR PROFIL
# ============================================================================

st.markdown("## 📊 Répartition par profil")

col1, col2 = st.columns([1, 2])

with col1:
    repartition = df_filtre['profil'].value_counts()

    st.markdown("**Nombre par profil** :")
    for profil, count in repartition.items():
        pct = (count / len(df_filtre)) * 100
        st.markdown(f"- {profil}: **{count}** ({pct:.1f}%)")

with col2:
    fig_pie = px.pie(
        values=repartition.values,
        names=repartition.index,
        title="Répartition des communes",
        color=repartition.index,
        color_discrete_map={
            'Dynamique': config.COLOR_DYNAMIQUE,
            'Précaire': config.COLOR_PRECAIRE,
            'Métropole': config.COLOR_METROPOLE,
            'Désertifié': config.COLOR_DESERTIFIE
        }
    )
    fig_pie.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig_pie, use_container_width=True)

st.markdown("---")
st.markdown(config.FOOTER_TEXT)
