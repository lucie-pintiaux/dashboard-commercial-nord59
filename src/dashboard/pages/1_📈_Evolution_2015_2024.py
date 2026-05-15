"""
Page 1 - Évolution 2015-2024
Analyse temporelle créations/fermetures avec dates historiques réelles
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import sys
from pathlib import Path

# Ajouter utils au path
sys.path.append(str(Path(__file__).parent.parent / "utils"))
import config
import data_loader

# ============================================================================
# CONFIGURATION PAGE
# ============================================================================

st.set_page_config(
    page_title="Évolution 2015-2024",
    page_icon="📈",
    layout=config.LAYOUT
)

# ============================================================================
# TITRE
# ============================================================================

st.title("📈 Évolution 2015-2024")
st.markdown("### Tendances temporelles créations et fermetures")
st.markdown("---")

# ============================================================================
# CHARGEMENT DONNÉES
# ============================================================================

with st.spinner("Chargement des données..."):
    df_etablissements = data_loader.load_etablissements()

if df_etablissements is None:
    st.error("❌ Impossible de charger les données")
    st.stop()

# Calculer évolution temporelle
df_evolution = data_loader.load_evolution_temporelle(df_etablissements)

# ============================================================================
# KPI GLOBAUX
# ============================================================================

st.markdown("## 📊 Indicateurs clés 2015-2024")

col1, col2, col3, col4 = st.columns(4)

with col1:
    taux_moyen = (df_evolution['nb_fermetures'].sum() / 
                  (df_evolution['nb_creations'].sum() + df_evolution['nb_fermetures'].sum()) * 100)
    st.metric(
        label="Taux de fermeture moyen",
        value=f"{taux_moyen:.1f}%"
    )

with col2:
    total_creations = df_evolution['nb_creations'].sum()
    st.metric(
        label="Total créations",
        value=f"{int(total_creations):,}".replace(',', ' ')
    )

with col3:
    total_fermetures = df_evolution['nb_fermetures'].sum()
    st.metric(
        label="Total fermetures",
        value=f"{int(total_fermetures):,}".replace(',', ' ')
    )

with col4:
    solde_total = df_evolution['solde_net'].sum()
    delta_color = "normal" if solde_total > 0 else "inverse"
    st.metric(
        label="Solde net total",
        value=f"{int(solde_total):,}".replace(',', ' '),
        delta="Positif" if solde_total > 0 else "Négatif",
        delta_color=delta_color
    )

st.markdown("---")

# ============================================================================
# GRAPHIQUE ÉVOLUTION TEMPORELLE
# ============================================================================

st.markdown("## 📈 Évolution du nombre de créations et fermetures")

fig = go.Figure()

# Ligne créations
fig.add_trace(go.Scatter(
    x=df_evolution['annee'],
    y=df_evolution['nb_creations'],
    mode='lines+markers',
    name='Créations',
    line=dict(color=config.COLOR_SUCCESS, width=3),
    marker=dict(size=8),
    hovertemplate='<b>%{x}</b><br>Créations: %{y:,}<extra></extra>'
))

# Ligne fermetures
fig.add_trace(go.Scatter(
    x=df_evolution['annee'],
    y=df_evolution['nb_fermetures'],
    mode='lines+markers',
    name='Fermetures',
    line=dict(color=config.COLOR_DANGER, width=3),
    marker=dict(size=8),
    hovertemplate='<b>%{x}</b><br>Fermetures: %{y:,}<extra></extra>'
))

# Ligne solde net
fig.add_trace(go.Scatter(
    x=df_evolution['annee'],
    y=df_evolution['solde_net'],
    mode='lines+markers',
    name='Solde net',
    line=dict(color=config.COLOR_PRIMARY, width=2, dash='dash'),
    marker=dict(size=6),
    hovertemplate='<b>%{x}</b><br>Solde net: %{y:,}<extra></extra>'
))

# Mise en forme
fig.update_layout(
    height=500,
    xaxis_title="Année",
    yaxis_title="Nombre d'établissements",
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ),
    hovermode='x unified'
)

# Annotation COVID
fig.add_vline(
    x=2020, 
    line_dash="dot", 
    line_color="gray",
    annotation_text="COVID-19",
    annotation_position="top"
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ============================================================================
# TABLEAU ÉVOLUTION ANNUELLE
# ============================================================================

st.markdown("## 📋 Détail par année")

# Formater tableau
df_display = df_evolution.copy()
df_display['annee'] = df_display['annee'].astype(int)

# Calculer taux fermeture
df_display['taux_fermeture'] = (
    df_display['nb_fermetures'] / 
    (df_display['nb_creations'] + df_display['nb_fermetures']) * 100
).round(1)

df_display = df_display.rename(columns={
    'annee': 'Année',
    'nb_creations': 'Créations',
    'nb_fermetures': 'Fermetures',
    'solde_net': 'Solde net',
    'taux_fermeture': 'Taux fermeture (%)'
})

st.dataframe(
    df_display,
    use_container_width=True,
    hide_index=True
)

# ============================================================================
# ANALYSE PÉRIODES
# ============================================================================

st.markdown("---")
st.markdown("## 🔍 Analyse par période")

col1, col2, col3 = st.columns(3)

# Avant COVID
avant_covid = df_evolution[df_evolution['annee'] <= 2019]
solde_avant = avant_covid['solde_net'].sum()
taux_avant = (avant_covid['nb_fermetures'].sum() / 
              (avant_covid['nb_creations'].sum() + avant_covid['nb_fermetures'].sum()) * 100)

with col1:
    st.markdown("### 📅 Avant COVID (2015-2019)")
    st.metric("Solde cumulé", f"{int(solde_avant):,}".replace(',', ' '))
    st.metric("Taux fermeture moyen", f"{taux_avant:.1f}%")
    st.metric("Créations totales", f"{int(avant_covid['nb_creations'].sum()):,}".replace(',', ' '))

# Pendant COVID
pendant_covid = df_evolution[
    (df_evolution['annee'] >= 2020) & 
    (df_evolution['annee'] <= 2021)
]
solde_pendant = pendant_covid['solde_net'].sum()
taux_pendant = (pendant_covid['nb_fermetures'].sum() / 
                (pendant_covid['nb_creations'].sum() + pendant_covid['nb_fermetures'].sum()) * 100)

with col2:
    st.markdown("### 🦠 Pendant COVID (2020-2021)")
    st.metric("Solde cumulé", f"{int(solde_pendant):,}".replace(',', ' '))
    st.metric("Taux fermeture moyen", f"{taux_pendant:.1f}%")

    # Pic 2020
    pic_2020 = df_evolution[df_evolution['annee'] == 2020]['nb_creations'].values[0]
    st.metric("Pic créations 2020", f"{int(pic_2020):,}".replace(',', ' '))

# Après COVID
apres_covid = df_evolution[df_evolution['annee'] >= 2022]
solde_apres = apres_covid['solde_net'].sum()
taux_apres = (apres_covid['nb_fermetures'].sum() / 
              (apres_covid['nb_creations'].sum() + apres_covid['nb_fermetures'].sum()) * 100)

with col3:
    st.markdown("### 📈 Après COVID (2022-2024)")
    st.metric("Solde cumulé", f"{int(solde_apres):,}".replace(',', ' '))
    st.metric("Taux fermeture moyen", f"{taux_apres:.1f}%")

    # Evolution
    variation = ((solde_apres - solde_avant) / solde_avant * 100) if solde_avant != 0 else 0
    st.metric("Évolution vs avant COVID", f"{variation:+.1f}%")

# ============================================================================
# FOOTER
# ============================================================================

st.markdown("---")
st.markdown(config.FOOTER_TEXT)
