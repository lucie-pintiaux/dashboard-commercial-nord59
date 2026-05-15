"""
Page 6 - EPCI / Intercommunalités
Analyse territoriale intercommunale
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

st.set_page_config(page_title="EPCI / Intercommunalités", page_icon="🤝", layout=config.LAYOUT)

st.title("🤝 EPCI / Intercommunalités")
st.markdown("### Analyse territoriale par intercommunalité")
st.markdown("---")

# ============================================================================
# CHARGEMENT DONNÉES
# ============================================================================

with st.spinner("Chargement des données..."):
    df_communes = data_loader.load_communes_avec_gps()

if df_communes is None:
    st.error("❌ Impossible de charger les données")
    st.stop()

# Vérifier colonne EPCI
if 'epci_nom' not in df_communes.columns and 'nom_epci' not in df_communes.columns:
    st.warning("⚠️ Données EPCI non disponibles dans le fichier")
    st.stop()

# Détecter nom colonne EPCI
col_epci = 'epci_nom' if 'epci_nom' in df_communes.columns else 'nom_epci'

# ============================================================================
# FILTRES
# ============================================================================

st.markdown("## 🔍 Sélection EPCI")

epci_list = ['Tous'] + sorted(df_communes[col_epci].dropna().unique().tolist())
epci_selectionne = st.selectbox("Sélectionnez un EPCI", epci_list, index=0)

# Filtrer données
if epci_selectionne == 'Tous':
    df_filtre = df_communes.copy()
else:
    df_filtre = df_communes[df_communes[col_epci] == epci_selectionne].copy()

st.markdown("---")

# ============================================================================
# KPI GLOBAUX
# ============================================================================

titre = f"## 📊 Vue d'ensemble" if epci_selectionne == 'Tous' else f"## 📊 {epci_selectionne}"
st.markdown(titre)

col1, col2, col3, col4 = st.columns(4)

with col1:
    nb_communes = len(df_filtre)
    st.metric("Communes", nb_communes)

with col2:
    nb_actifs = int(df_filtre['nb_actifs'].sum())
    st.metric("Établissements actifs", f"{nb_actifs:,}".replace(',', ' '))

with col3:
    if 'population' in df_filtre.columns:
        pop_totale = int(df_filtre['population'].sum())
        st.metric("Population totale", f"{pop_totale:,}".replace(',', ' '))
    else:
        st.metric("Population", "N/A")

with col4:
    score_moyen = df_filtre['score_fragilite'].mean()
    st.metric("Score fragilité moyen", f"{score_moyen:.1f}")

st.markdown("---")

# ============================================================================
# CLASSEMENT COMMUNES EPCI SÉLECTIONNÉ
# ============================================================================

if epci_selectionne != 'Tous':
    st.markdown(f"## 📊 Classement des communes de {epci_selectionne}")

    df_classement = df_filtre[[
        'nom_commune', 'taux_mortalite', 'score_fragilite', 'nb_actifs', 'profil', 'categorie_priorite'
    ]].copy()

    df_classement = df_classement.sort_values('score_fragilite', ascending=False)

    df_classement.columns = ['Commune', 'Taux mortalité (%)', 'Score', 'Nb actifs', 'Profil', 'Catégorie']
    df_classement['Taux mortalité (%)'] = df_classement['Taux mortalité (%)'].round(1)
    df_classement['Score'] = df_classement['Score'].round(1)

    st.dataframe(df_classement, use_container_width=True, hide_index=True)

    st.markdown("---")

# ============================================================================
# COMPARAISON ENTRE EPCI
# ============================================================================

st.markdown("## 📊 Comparaison entre EPCI du département")

# Agréger par EPCI
epci_stats = df_communes.groupby(col_epci).agg({
    'nom_commune': 'count',
    'nb_actifs': 'sum',
    'taux_mortalite': 'mean',
    'score_fragilite': 'mean'
}).reset_index()

epci_stats.columns = ['EPCI', 'Nb communes', 'Total actifs', 'Taux mortalité moyen', 'Score moyen']
epci_stats = epci_stats.sort_values('Score moyen', ascending=False)

# Graphique comparaison
fig = px.bar(
    epci_stats,
    x='Score moyen',
    y='EPCI',
    orientation='h',
    color='Score moyen',
    color_continuous_scale=['green', 'orange', 'red'],
    labels={'Score moyen': 'Score fragilité moyen'},
    hover_data=['Nb communes', 'Total actifs', 'Taux mortalité moyen']
)

fig.update_layout(height=600, showlegend=False)
fig.update_traces(texttemplate='%{x:.1f}', textposition='outside')

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ============================================================================
# TABLEAU DÉTAILLÉ EPCI
# ============================================================================

st.markdown("## 📋 Tableau détaillé par EPCI")

epci_stats['Taux mortalité moyen'] = epci_stats['Taux mortalité moyen'].round(1)
epci_stats['Score moyen'] = epci_stats['Score moyen'].round(1)

st.dataframe(epci_stats, use_container_width=True, hide_index=True)

st.markdown("---")

# ============================================================================
# CARTE EPCI SÉLECTIONNÉ (si pas Tous)
# ============================================================================

if epci_selectionne != 'Tous':
    st.markdown(f"## 🗺️ Carte des communes de {epci_selectionne}")

    # Filtrer communes avec GPS
    df_carte = df_filtre[df_filtre['latitude'].notna() & df_filtre['longitude'].notna()].copy()

    if len(df_carte) > 0:
        fig_carte = px.scatter_mapbox(
            df_carte,
            lat='latitude',
            lon='longitude',
            color='score_fragilite',
            size='nb_actifs',
            hover_name='nom_commune',
            hover_data={
                'latitude': False,
                'longitude': False,
                'taux_mortalite': ':.1f',
                'score_fragilite': ':.1f',
                'nb_actifs': True,
                'profil': True
            },
            color_continuous_scale=['green', 'orange', 'red'],
            labels={'score_fragilite': 'Score'},
            zoom=9,
            height=500
        )

        fig_carte.update_layout(
            mapbox_style="open-street-map",
            margin={"r":0,"t":0,"l":0,"b":0}
        )

        st.plotly_chart(fig_carte, use_container_width=True)
    else:
        st.info("Coordonnées GPS non disponibles pour cet EPCI")

    st.markdown("---")

# ============================================================================
# FOOTER
# ============================================================================

st.markdown(config.FOOTER_TEXT)
