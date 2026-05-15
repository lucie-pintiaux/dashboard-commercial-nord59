"""
Page 8 - Tableaux de bord
Synthèse multi-indicateurs
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

st.set_page_config(page_title="Tableaux de bord", page_icon="📊", layout=config.LAYOUT)

st.title("📊 Tableaux de bord")
st.markdown("### Vue d'ensemble consolidée")
st.markdown("---")

# ============================================================================
# CHARGEMENT DONNÉES
# ============================================================================

with st.spinner("Chargement des données..."):
    df_communes = data_loader.load_communes_avec_gps()
    df_etablissements = data_loader.load_etablissements()
    df_secteurs = data_loader.load_secteurs_vulnerables()
    df_commerces_manquants = data_loader.load_commerces_manquants()

if df_communes is None or df_etablissements is None:
    st.error("❌ Impossible de charger les données")
    st.stop()

# ============================================================================
# SECTION 1 : INDICATEURS TERRITORIAUX
# ============================================================================

st.markdown("## 🗺️ Indicateurs territoriaux")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    nb_communes = len(df_communes)
    st.metric("Communes", nb_communes)

with col2:
    nb_actifs = int(df_communes['nb_actifs'].sum())
    st.metric("Établissements actifs", f"{nb_actifs:,}".replace(',', ' '))

with col3:
    nb_fermes = int(df_communes['nb_fermes'].sum()) if 'nb_fermes' in df_communes.columns else 0
    st.metric("Établissements fermés", f"{nb_fermes:,}".replace(',', ' '))

with col4:
    taux_moyen = df_communes['taux_mortalite'].mean()
    st.metric("Taux mortalité moyen", f"{taux_moyen:.1f}%")

with col5:
    nb_prioritaires = len(df_communes[df_communes['categorie_priorite'].isin(['Priorité A', 'Priorité B'])])
    pct_prioritaires = (nb_prioritaires / nb_communes * 100)
    st.metric("Communes prioritaires", f"{nb_prioritaires} ({pct_prioritaires:.1f}%)")

st.markdown("---")

# ============================================================================
# SECTION 2 : RÉPARTITION PAR PROFIL
# ============================================================================

st.markdown("## 📊 Répartition par profil et catégorie")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Par profil")

    profils = df_communes['profil'].value_counts()

    fig_profils = px.pie(
        values=profils.values,
        names=profils.index,
        color=profils.index,
        color_discrete_map={
            'Dynamique': config.COLOR_DYNAMIQUE,
            'Précaire': config.COLOR_PRECAIRE,
            'Métropole': config.COLOR_METROPOLE,
            'Désertifié': config.COLOR_DESERTIFIE
        },
        hole=0.4
    )

    fig_profils.update_traces(textposition='inside', textinfo='percent+label')
    fig_profils.update_layout(showlegend=True)

    st.plotly_chart(fig_profils, use_container_width=True)

with col2:
    st.markdown("### Par catégorie priorité")

    categories = df_communes['categorie_priorite'].value_counts()

    fig_categories = px.pie(
        values=categories.values,
        names=categories.index,
        color=categories.index,
        color_discrete_map={
            'Priorité A': config.COLOR_PRIORITE_A,
            'Priorité B': config.COLOR_PRIORITE_B,
            'Non prioritaire': config.COLOR_NON_PRIORITAIRE
        },
        hole=0.4
    )

    fig_categories.update_traces(textposition='inside', textinfo='percent+label')
    fig_categories.update_layout(showlegend=True)

    st.plotly_chart(fig_categories, use_container_width=True)

st.markdown("---")

# ============================================================================
# SECTION 3 : INDICATEURS PAR PROFIL
# ============================================================================

st.markdown("## 📊 Comparaison des profils")

# Statistiques par profil
profil_stats = df_communes.groupby('profil').agg({
    'taux_mortalite': 'mean',
    'score_fragilite': 'mean',
    'nb_actifs': 'mean'
}).reset_index()

profil_stats.columns = ['Profil', 'Taux mortalité moyen', 'Score fragilité moyen', 'Nb actifs moyen']
profil_stats['Taux mortalité moyen'] = profil_stats['Taux mortalité moyen'].round(1)
profil_stats['Score fragilité moyen'] = profil_stats['Score fragilité moyen'].round(1)
profil_stats['Nb actifs moyen'] = profil_stats['Nb actifs moyen'].round(0).astype(int)

st.dataframe(profil_stats, use_container_width=True, hide_index=True)

st.markdown("---")

# ============================================================================
# SECTION 4 : ÉVOLUTION TEMPORELLE SYNTHÈSE
# ============================================================================

st.markdown("## 📈 Évolution temporelle synthèse")

if df_etablissements is not None:
    df_evolution = data_loader.load_evolution_temporelle(df_etablissements)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Solde net 2015-2024")

        fig_solde = go.Figure()

        fig_solde.add_trace(go.Scatter(
            x=df_evolution['annee'],
            y=df_evolution['solde_net'],
            mode='lines+markers',
            fill='tozeroy',
            line=dict(color=config.COLOR_PRIMARY, width=2),
            marker=dict(size=8)
        ))

        fig_solde.add_hline(y=0, line_dash="dash", line_color="gray")
        fig_solde.update_layout(height=300, xaxis_title="", yaxis_title="Solde net")

        st.plotly_chart(fig_solde, use_container_width=True)

    with col2:
        st.markdown("### Taux fermeture annuel")

        df_evolution['taux'] = (df_evolution['nb_fermetures'] / (df_evolution['nb_creations'] + df_evolution['nb_fermetures']) * 100)

        fig_taux = go.Figure()

        fig_taux.add_trace(go.Bar(
            x=df_evolution['annee'],
            y=df_evolution['taux'],
            marker_color=config.COLOR_DANGER
        ))

        fig_taux.update_layout(height=300, xaxis_title="", yaxis_title="Taux (%)")

        st.plotly_chart(fig_taux, use_container_width=True)

st.markdown("---")

# ============================================================================
# SECTION 5 : TOP/FLOP
# ============================================================================

st.markdown("## 🏆 Top & Flop communes")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🟢 Top 5 communes dynamiques")

    top_5 = df_communes.nsmallest(5, 'taux_mortalite')[['nom_commune', 'taux_mortalite', 'score_fragilite']]
    top_5.columns = ['Commune', 'Taux (%)', 'Score']
    top_5['Taux (%)'] = top_5['Taux (%)'].round(1)
    top_5['Score'] = top_5['Score'].round(1)

    st.dataframe(top_5, use_container_width=True, hide_index=True)

with col2:
    st.markdown("### 🔴 Top 5 communes fragiles")

    flop_5 = df_communes.nlargest(5, 'taux_mortalite')[['nom_commune', 'taux_mortalite', 'score_fragilite']]
    flop_5.columns = ['Commune', 'Taux (%)', 'Score']
    flop_5['Taux (%)'] = flop_5['Taux (%)'].round(1)
    flop_5['Score'] = flop_5['Score'].round(1)

    st.dataframe(flop_5, use_container_width=True, hide_index=True)

st.markdown("---")

# ============================================================================
# SECTION 6 : COMMERCES MANQUANTS SYNTHÈSE
# ============================================================================

if df_commerces_manquants is not None:
    st.markdown("## 🏪 Commerces manquants - Synthèse")

    col1, col2, col3 = st.columns(3)

    with col1:
        nb_communes_manquants = len(df_commerces_manquants)
        pct_communes = (nb_communes_manquants / nb_communes * 100)
        st.metric("Communes avec commerces manquants", f"{nb_communes_manquants} ({pct_communes:.1f}%)")

    with col2:
        total_manquants = df_commerces_manquants['nb_commerces_manquants'].sum()
        st.metric("Total commerces manquants", int(total_manquants))

    with col3:
        moyenne = df_commerces_manquants['nb_commerces_manquants'].mean()
        st.metric("Moyenne par commune", f"{moyenne:.1f}")

    st.markdown("---")

# ============================================================================
# FOOTER
# ============================================================================

st.markdown(config.FOOTER_TEXT)
