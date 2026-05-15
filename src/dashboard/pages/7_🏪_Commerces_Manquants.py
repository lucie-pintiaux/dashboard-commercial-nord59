"""
Page 7 - Commerces manquants
Identification besoins non couverts
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

st.set_page_config(page_title="Commerces manquants", page_icon="🏪", layout=config.LAYOUT)

st.title("🏪 Commerces manquants")
st.markdown("### Identification des commerces essentiels absents")
st.markdown("---")

# ============================================================================
# CHARGEMENT DONNÉES
# ============================================================================

with st.spinner("Chargement des données..."):
    df_commerces_manquants = data_loader.load_commerces_manquants()
    df_communes = data_loader.load_communes_avec_gps()

if df_commerces_manquants is None or df_communes is None:
    st.error("❌ Impossible de charger les données")
    st.stop()

# ============================================================================
# KPI GLOBAUX
# ============================================================================

st.markdown("## 📊 Vue d'ensemble")

col1, col2, col3, col4 = st.columns(4)

with col1:
    nb_communes = len(df_commerces_manquants)
    st.metric("Communes concernées", nb_communes)

with col2:
    total_manquants = df_commerces_manquants['nb_commerces_manquants'].sum()
    st.metric("Total commerces manquants", int(total_manquants))

with col3:
    prioritaires = df_commerces_manquants[
        df_commerces_manquants['categorie_priorite'].isin(['Priorité A', 'Priorité B'])
    ]
    nb_prioritaires = len(prioritaires)
    st.metric("Communes prioritaires", nb_prioritaires)

with col4:
    moyenne_manquants = df_commerces_manquants['nb_commerces_manquants'].mean()
    st.metric("Moyenne par commune", f"{moyenne_manquants:.1f}")

st.markdown("---")

# ============================================================================
# TOP 10 TYPES COMMERCES LES PLUS MANQUANTS
# ============================================================================

st.markdown("## 📊 Top 10 types de commerces les plus manquants")

# Extraire tous les types de commerces
tous_types = []
for liste in df_commerces_manquants['liste_manquants']:
    if pd.notna(liste):
        types = [t.strip() for t in liste.split(',')]
        tous_types.extend(types)

# Compter occurrences
types_counts = pd.Series(tous_types).value_counts().head(10)

fig = px.bar(
    x=types_counts.values,
    y=types_counts.index,
    orientation='h',
    color=types_counts.values,
    color_continuous_scale='Reds',
    labels={'x': 'Nombre de communes', 'y': 'Type de commerce'},
    text=types_counts.values
)

fig.update_traces(textposition='outside')
fig.update_layout(height=500, showlegend=False)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ============================================================================
# FILTRES
# ============================================================================

st.markdown("## 🔍 Filtres")

col1, col2 = st.columns(2)

with col1:
    categories = ['Tous'] + sorted(df_commerces_manquants['categorie_priorite'].unique().tolist())
    filtre_categorie = st.selectbox("Catégorie priorité", categories)

with col2:
    # Créer liste unique types commerces
    types_uniques = sorted(list(set(tous_types)))
    filtre_type = st.selectbox("Type de commerce", ['Tous'] + types_uniques)

# Appliquer filtres
df_filtre = df_commerces_manquants.copy()

if filtre_categorie != 'Tous':
    df_filtre = df_filtre[df_filtre['categorie_priorite'] == filtre_categorie]

if filtre_type != 'Tous':
    df_filtre = df_filtre[df_filtre['liste_manquants'].str.contains(filtre_type, na=False)]

st.markdown(f"**{len(df_filtre)} communes** affichées")

st.markdown("---")

# ============================================================================
# CARTE COMMUNES AVEC COMMERCES MANQUANTS
# ============================================================================

st.markdown("## 🗺️ Carte des communes avec commerces manquants")

# Joindre avec GPS
df_carte = df_filtre.merge(
    df_communes[['code_commune', 'latitude', 'longitude']], 
    on='code_commune', 
    how='left'
)

df_carte = df_carte[df_carte['latitude'].notna() & df_carte['longitude'].notna()]

if len(df_carte) > 0:
    fig_carte = px.scatter_mapbox(
        df_carte,
        lat='latitude',
        lon='longitude',
        color='nb_commerces_manquants',
        size='nb_commerces_manquants',
        hover_name='nom_commune',
        hover_data={
            'latitude': False,
            'longitude': False,
            'nb_commerces_manquants': True,
            'score_fragilite': ':.1f',
            'categorie_priorite': True,
            'liste_manquants': True
        },
        color_continuous_scale='Reds',
        labels={'nb_commerces_manquants': 'Nb commerces manquants'},
        zoom=8,
        height=600
    )

    fig_carte.update_layout(
        mapbox_style="open-street-map",
        margin={"r":0,"t":0,"l":0,"b":0}
    )

    st.plotly_chart(fig_carte, use_container_width=True)
else:
    st.info("Aucune commune avec coordonnées GPS disponible")

st.markdown("---")

# ============================================================================
# TABLEAU DÉTAILLÉ
# ============================================================================

st.markdown("## 📋 Tableau détaillé par commune")

df_display = df_filtre[[
    'nom_commune', 'epci_nom', 'categorie_priorite', 'score_fragilite', 
    'nb_commerces_manquants', 'liste_manquants'
]].copy()

df_display = df_display.sort_values('nb_commerces_manquants', ascending=False)

df_display.columns = [
    'Commune', 'EPCI', 'Catégorie', 'Score', 
    'Nb manquants', 'Liste commerces manquants'
]

df_display['Score'] = df_display['Score'].round(1)

st.dataframe(df_display, use_container_width=True, hide_index=True)

st.markdown("---")

# ============================================================================
# DISTRIBUTION PAR NOMBRE MANQUANTS
# ============================================================================

st.markdown("## 📊 Distribution des communes par nombre de commerces manquants")

distribution = df_commerces_manquants['nb_commerces_manquants'].value_counts().sort_index()

fig_dist = px.bar(
    x=distribution.index,
    y=distribution.values,
    labels={'x': 'Nombre de commerces manquants', 'y': 'Nombre de communes'},
    color=distribution.values,
    color_continuous_scale='Reds'
)

fig_dist.update_layout(height=400, showlegend=False)
fig_dist.update_traces(text=distribution.values, textposition='outside')

st.plotly_chart(fig_dist, use_container_width=True)

st.markdown("---")
st.markdown(config.FOOTER_TEXT)
