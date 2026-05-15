"""
Page 4 - Types de commerces en déclin
Analyse secteurs NAF vulnérables
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

st.set_page_config(page_title="Types commerces en déclin", page_icon="📉", layout=config.LAYOUT)

st.title("📉 Types de commerces en déclin")
st.markdown("### Analyse des secteurs NAF les plus vulnérables")
st.markdown("---")

# ============================================================================
# CHARGEMENT DONNÉES
# ============================================================================

with st.spinner("Chargement des données..."):
    df_secteurs = data_loader.load_secteurs_vulnerables()

if df_secteurs is None:
    st.error("❌ Impossible de charger les données")
    st.stop()

# ============================================================================
# KPI GLOBAUX
# ============================================================================

st.markdown("## 📊 Vue d'ensemble")

col1, col2, col3, col4 = st.columns(4)

with col1:
    nb_secteurs = len(df_secteurs)
    st.metric("Secteurs NAF analysés", nb_secteurs)

with col2:
    taux_moyen = df_secteurs['taux_fermeture'].mean()
    st.metric("Taux fermeture moyen", f"{taux_moyen:.1f}%")

with col3:
    secteur_plus_fragile = df_secteurs.nlargest(1, 'taux_fermeture').iloc[0]
    st.metric("Secteur le plus fragile", f"{secteur_plus_fragile['taux_fermeture']:.1f}%")
    st.caption(secteur_plus_fragile['naf_classe_libelle'][:40] + "...")

with col4:
    total_fermes = df_secteurs['nb_fermes'].sum()
    st.metric("Total établissements fermés", f"{int(total_fermes):,}".replace(',', ' '))

st.markdown("---")

# ============================================================================
# TOP 10 SECTEURS LES PLUS FRAGILES
# ============================================================================

st.markdown("## 📊 Top 10 secteurs les plus fragiles")

top_10 = df_secteurs.nlargest(10, 'taux_fermeture').copy()

fig = px.bar(
    top_10,
    x='taux_fermeture',
    y='naf_classe_libelle',
    orientation='h',
    color='taux_fermeture',
    color_continuous_scale=['green', 'orange', 'red'],
    labels={'taux_fermeture': 'Taux fermeture (%)', 'naf_classe_libelle': 'Secteur'},
    text='taux_fermeture'
)

fig.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
fig.update_layout(height=500, showlegend=False)
fig.update_yaxes(categoryorder='total ascending')

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ============================================================================
# TABLEAU DÉTAILLÉ PAR SECTEUR
# ============================================================================

st.markdown("## 📋 Tableau détaillé par secteur NAF")

# Préparer tableau
df_display = df_secteurs.copy()
df_display = df_display.sort_values('taux_fermeture', ascending=False)

df_display['taux_fermeture'] = df_display['taux_fermeture'].round(1)

df_display = df_display[[
    'naf_classe_libelle', 'total_etablissements', 'nb_actifs', 'nb_fermes', 'taux_fermeture'
]].rename(columns={
    'naf_classe_libelle': 'Libellé secteur',
    'total_etablissements': 'Total',
    'nb_actifs': 'Actifs',
    'nb_fermes': 'Fermés',
    'taux_fermeture': 'Taux (%)'
})

st.dataframe(df_display, use_container_width=True, hide_index=True)

st.markdown("---")

# ============================================================================
# RÉPARTITION ACTIFS / FERMÉS
# ============================================================================

st.markdown("## 📊 Répartition globale actifs vs fermés")

col1, col2 = st.columns([1, 2])

with col1:
    total_actifs = df_secteurs['nb_actifs'].sum()
    total_fermes = df_secteurs['nb_fermes'].sum()
    total_global = total_actifs + total_fermes

    st.markdown("**Statistiques globales** :")
    st.markdown(f"- Actifs : **{int(total_actifs):,}** ({total_actifs/total_global*100:.1f}%)".replace(',', ' '))
    st.markdown(f"- Fermés : **{int(total_fermes):,}** ({total_fermes/total_global*100:.1f}%)".replace(',', ' '))
    st.markdown(f"- Total : **{int(total_global):,}**".replace(',', ' '))

with col2:
    fig_pie = go.Figure(data=[go.Pie(
        labels=['Actifs', 'Fermés'],
        values=[total_actifs, total_fermes],
        marker_colors=[config.COLOR_SUCCESS, config.COLOR_DANGER],
        hole=0.4
    )])

    fig_pie.update_traces(textposition='inside', textinfo='percent+label')
    fig_pie.update_layout(
        title="Répartition établissements",
        showlegend=True
    )

    st.plotly_chart(fig_pie, use_container_width=True)

st.markdown("---")

# ============================================================================
# ANALYSE PAR TRANCHE DE TAUX
# ============================================================================

st.markdown("## 📊 Distribution des secteurs par niveau de fragilité")

# Créer tranches
df_secteurs['tranche'] = pd.cut(
    df_secteurs['taux_fermeture'],
    bins=[0, 40, 55, 70, 100],
    labels=['Faible (0-40%)', 'Modéré (40-55%)', 'Élevé (55-70%)', 'Très élevé (70-100%)']
)

tranches = df_secteurs['tranche'].value_counts().sort_index()

fig_tranches = px.bar(
    x=tranches.index,
    y=tranches.values,
    labels={'x': 'Niveau de fragilité', 'y': 'Nombre de secteurs'},
    color=tranches.index,
    color_discrete_map={
        'Faible (0-40%)': config.COLOR_SUCCESS,
        'Modéré (40-55%)': config.COLOR_WARNING,
        'Élevé (55-70%)': '#ff6b35',
        'Très élevé (70-100%)': config.COLOR_DANGER
    }
)

fig_tranches.update_layout(height=400, showlegend=False)
fig_tranches.update_traces(text=tranches.values, textposition='outside')

st.plotly_chart(fig_tranches, use_container_width=True)

st.markdown("---")
st.markdown(config.FOOTER_TEXT)
