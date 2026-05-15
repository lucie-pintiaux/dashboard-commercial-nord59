"""
Page 2 - Rupture COVID 2020-2021
Analyse complète impact pandémie
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent / "utils"))
import config
import data_loader

st.set_page_config(page_title="Rupture COVID", page_icon="🦠", layout=config.LAYOUT)

st.title("🦠 Rupture COVID 2020-2021")
st.markdown("### Impact de la pandémie sur la dynamique commerciale")
st.markdown("---")

with st.spinner("Chargement des données..."):
    df_etablissements = data_loader.load_etablissements()

if df_etablissements is None:
    st.error("❌ Impossible de charger les données")
    st.stop()

df_evolution = data_loader.load_evolution_temporelle(df_etablissements)

# Périodes
avant_covid = df_evolution[df_evolution['annee'] <= 2019].copy()
pendant_covid = df_evolution[(df_evolution['annee'] >= 2020) & (df_evolution['annee'] <= 2021)].copy()
apres_covid = df_evolution[df_evolution['annee'] >= 2022].copy()

# Calculs globaux
solde_avant = int(avant_covid['solde_net'].sum())
creations_avant = int(avant_covid['nb_creations'].sum())
fermetures_avant = int(avant_covid['nb_fermetures'].sum())
taux_avant = (fermetures_avant / (creations_avant + fermetures_avant) * 100)

solde_pendant = int(pendant_covid['solde_net'].sum())
creations_pendant = int(pendant_covid['nb_creations'].sum())
fermetures_pendant = int(pendant_covid['nb_fermetures'].sum())
taux_pendant = (fermetures_pendant / (creations_pendant + fermetures_pendant) * 100)

solde_apres = int(apres_covid['solde_net'].sum())
creations_apres = int(apres_covid['nb_creations'].sum())
fermetures_apres = int(apres_covid['nb_fermetures'].sum())
taux_apres = (fermetures_apres / (creations_apres + fermetures_apres) * 100)

# Variations
var_solde = ((solde_pendant/2) / (solde_avant/5) - 1) * 100
var_creations = ((creations_pendant/2) / (creations_avant/5) - 1) * 100
var_fermetures = ((fermetures_pendant/2) / (fermetures_avant/5) - 1) * 100

var_solde_apres = ((solde_apres/3) / (solde_avant/5) - 1) * 100
var_creations_apres = ((creations_apres/3) / (creations_avant/5) - 1) * 100
var_fermetures_apres = ((fermetures_apres/3) / (fermetures_avant/5) - 1) * 100

# ============================================================================
# KPI COMPARATIFS
# ============================================================================

st.markdown("## 📊 Comparaison des trois périodes")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 📅 Avant COVID (2015-2019)")
    st.markdown("**5 années de référence**")

    st.metric("Solde net cumulé", f"{solde_avant:,}".replace(',', ' '))
    st.metric("Créations/an", f"{int(creations_avant/5):,}".replace(',', ' '))
    st.metric("Fermetures/an", f"{int(fermetures_avant/5):,}".replace(',', ' '))
    st.metric("Taux fermeture", f"{taux_avant:.1f}%")

with col2:
    st.markdown("### 🦠 Pendant COVID (2020-2021)")
    st.markdown("**2 années pandémie**")

    delta_text = f"{var_solde:+.1f}% vs avant"
    st.metric("Solde net cumulé", f"{solde_pendant:,}".replace(',', ' '), delta=delta_text)

    delta_text2 = f"{var_creations:+.1f}%"
    st.metric("Créations/an", f"{int(creations_pendant/2):,}".replace(',', ' '), delta=delta_text2)

    delta_text3 = f"{var_fermetures:+.1f}%"
    st.metric("Fermetures/an", f"{int(fermetures_pendant/2):,}".replace(',', ' '), delta=delta_text3)

    delta_text4 = f"{taux_pendant - taux_avant:+.1f} pts"
    st.metric("Taux fermeture", f"{taux_pendant:.1f}%", delta=delta_text4)

with col3:
    st.markdown("### 📈 Après COVID (2022-2024)")
    st.markdown("**3 années post-pandémie**")

    delta_text5 = f"{var_solde_apres:+.1f}% vs avant"
    st.metric("Solde net cumulé", f"{solde_apres:,}".replace(',', ' '), delta=delta_text5, delta_color="inverse")

    delta_text6 = f"{var_creations_apres:+.1f}%"
    st.metric("Créations/an", f"{int(creations_apres/3):,}".replace(',', ' '), delta=delta_text6, delta_color="inverse")

    delta_text7 = f"{var_fermetures_apres:+.1f}%"
    st.metric("Fermetures/an", f"{int(fermetures_apres/3):,}".replace(',', ' '), delta=delta_text7, delta_color="inverse")

    delta_text8 = f"{taux_apres - taux_avant:+.1f} pts"
    st.metric("Taux fermeture", f"{taux_apres:.1f}%", delta=delta_text8, delta_color="inverse")

st.markdown("---")

# ============================================================================
# GRAPHIQUE COMPARAISON
# ============================================================================

st.markdown("## 📊 Comparaison des moyennes annuelles")

periodes_data = pd.DataFrame({
    'Période': ['Avant COVID\n(2015-2019)', 'Pendant COVID\n(2020-2021)', 'Après COVID\n(2022-2024)'],
    'Créations': [creations_avant/5, creations_pendant/2, creations_apres/3],
    'Fermetures': [fermetures_avant/5, fermetures_pendant/2, fermetures_apres/3]
})

fig = go.Figure()
fig.add_trace(go.Bar(
    name='Créations', 
    x=periodes_data['Période'], 
    y=periodes_data['Créations'], 
    marker_color=config.COLOR_SUCCESS,
    text=[f"{int(v):,}".replace(',', ' ') for v in periodes_data['Créations']],
    textposition='outside'
))
fig.add_trace(go.Bar(
    name='Fermetures', 
    x=periodes_data['Période'], 
    y=periodes_data['Fermetures'], 
    marker_color=config.COLOR_DANGER,
    text=[f"{int(v):,}".replace(',', ' ') for v in periodes_data['Fermetures']],
    textposition='outside'
))
fig.update_layout(height=500, yaxis_title="Nombre moyen par an", barmode='group')

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ============================================================================
# TIMELINE AVEC ZONES
# ============================================================================

st.markdown("## 📈 Timeline 2015-2024 avec zones d'impact")

fig2 = go.Figure()
fig2.add_trace(go.Scatter(
    x=df_evolution['annee'], 
    y=df_evolution['solde_net'], 
    mode='lines+markers',
    line=dict(color=config.COLOR_PRIMARY, width=3),
    marker=dict(size=10)
))

# Zones colorées
fig2.add_vrect(x0=2014.5, x1=2019.5, fillcolor=config.COLOR_SUCCESS, opacity=0.1, layer="below", line_width=0)
fig2.add_vrect(x0=2019.5, x1=2021.5, fillcolor=config.COLOR_WARNING, opacity=0.2, layer="below", line_width=0)
fig2.add_vrect(x0=2021.5, x1=2024.5, fillcolor=config.COLOR_DANGER, opacity=0.1, layer="below", line_width=0)

fig2.add_hline(y=0, line_dash="dash", line_color="gray", opacity=0.5)
fig2.update_layout(height=400, xaxis_title="Année", yaxis_title="Solde net", showlegend=False)

st.plotly_chart(fig2, use_container_width=True)

# ============================================================================
# ANALYSE DÉTAILLÉE
# ============================================================================

st.markdown("---")
st.markdown("## 🔍 Analyse détaillée")

tab1, tab2, tab3 = st.tabs(["🦠 Pic 2020", "📉 Convergence 2022-2024", "💡 Interprétation"])

with tab1:
    st.markdown("### 🦠 Pic paradoxal des créations en 2020")

    col1, col2 = st.columns(2)

    with col1:
        donnees_2020 = df_evolution[df_evolution['annee'] == 2020].iloc[0]
        donnees_2019 = df_evolution[df_evolution['annee'] == 2019].iloc[0]

        st.metric("Créations 2020", f"{int(donnees_2020['nb_creations']):,}".replace(',', ' '))
        variation_2020 = ((donnees_2020['nb_creations'] / donnees_2019['nb_creations']) - 1) * 100
        st.metric("vs 2019", f"{variation_2020:+.1f}%")

    with col2:
        st.markdown("""
        **Explications possibles** :
        - Aides massives État (PGE, chômage partiel)
        - Reconversions professionnelles
        - E-commerce (boom achats en ligne)
        - Moratoire sur faillites
        """)

with tab2:
    st.markdown("### 📉 Convergence dangereuse créations/fermetures")

    st.markdown(f"""
    **Observation** : Le solde net s'effondre de {int(solde_avant/5):,} (moyenne avant COVID) 
    à {int(solde_apres/3):,} (moyenne après COVID).

    **Chiffres clés** :
    - Créations : {var_creations_apres:+.1f}% vs avant COVID
    - Fermetures : {var_fermetures_apres:+.1f}% vs avant COVID
    - Taux fermeture : {taux_apres:.1f}% (vs {taux_avant:.1f}% avant)

    **Projection** : Si tendance actuelle continue, solde négatif attendu dès 2025-2026.
    """.replace(',', ' '))

with tab3:
    st.markdown("### 💡 Interprétation globale")

    st.markdown("""
    #### COVID = Choc conjoncturel masquant déclin structurel

    **Phase 1 (2020-2021) : Résilience artificielle**
    - Pic créations 2020 soutenu par aides massives
    - Fermetures contenues par moratoire faillites
    - Solde net élevé = **illusion de dynamisme**

    **Phase 2 (2022-2024) : Rattrapage et déclin**
    - Fin aides → baisse créations (-6,2% vs avant)
    - Rattrapage fermetures différées (+78,8% vs avant)
    - Convergence créations/fermetures révèle **fragilité structurelle**

    #### Implications stratégiques

    - ⚠️ Ne pas comparer 2024 à 2020-2021 (période exceptionnelle)
    - ✅ Comparer à 2015-2019 (période stable de référence)
    - 🎯 Anticiper solde négatif 2025-2026
    - 💡 Cibler interventions sur communes fragilisées post-COVID
    """)

st.markdown("---")
st.markdown(config.FOOTER_TEXT)
