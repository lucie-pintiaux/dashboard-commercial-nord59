"""
Dashboard Commercial Nord 59 - Page d'accueil
Point d'entrée principal de l'application Streamlit
"""

import sys
from pathlib import Path

import streamlit as st

# Ajouter utils au path
sys.path.append(str(Path(__file__).parent / "utils"))
import config

# ============================================================================
# CONFIGURATION PAGE
# ============================================================================

st.set_page_config(
    page_title=config.PAGE_TITLE, page_icon=config.PAGE_ICON, layout=config.LAYOUT
)

# ============================================================================
# HEADER
# ============================================================================

st.title("📊 Dashboard Commercial Nord 59")
st.markdown("### Analyse de la dynamique commerciale du département")

st.markdown("---")

# ============================================================================
# PRÉSENTATION
# ============================================================================

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
    ## 🎯 Objectif

    Ce dashboard permet d'analyser la **fragilité commerciale** des 647 communes 
    du département du Nord à partir des données SIRENE enrichies.

    **Analyses disponibles** :
    - Évolution temporelle 2015-2024 (dates historiques réelles)
    - Impact COVID-19 (rupture 2020-2021)
    - Score de fragilité par commune (0-100)
    - Clustering territorial (4 profils)
    - Commerces manquants (déserts commerciaux)
    - Secteurs vulnérables (taux fermeture NAF)
    - Analyses EPCI/Intercommunalités

    **Personas cibles** :
    - 👩‍💼 Chargées de mission CCI (analyse territoriale)
    - 🏛️ Élus CA (arbitrage budgétaire)
    - 🏢 Directeurs développement économique
    """
    )

with col2:
    st.markdown(
        """
    ## 📊 Données

    **Source** : INSEE SIRENE (extraction 2024)  
    **Périmètre** : 
    - 647 communes du Nord (59)
    - 98 369 établissements NAF 47xx (commerce détail)
    - Données socio-économiques INSEE (population, chômage, revenus)

    **Période** : 2015-2024 (10 ans)

    **Livrables Sprint 4** :
    - Score fragilité composite (4 dimensions)
    - 4 profils : Dynamique, Précaire, Métropole, Désertifié
    - 203 communes prioritaires identifiées
    - 105 déserts commerciaux (7/7 commerces manquants)

    **Enrichissement Sprint 5** :
    - ✅ Dates fermetures historiques réelles récupérées
    - ✅ 35 630 fermetures 2015-2024 exploitables
    """
    )

# ============================================================================
# NAVIGATION
# ============================================================================

st.markdown("---")

st.markdown("## 🧭 Navigation")

st.markdown(
    """
Utilisez le **menu latéral** pour accéder aux 9 pages thématiques :

### 📈 Analyses temporelles
1. **Évolution 2015-2024** — Tendances créations/fermetures (dates historiques)
2. **Rupture COVID** — Impact 2020-2021 et analyse post-COVID

### 🗺️ Analyses territoriales
3. **Tendances par commune** — Carte interactive + classements
4. **Types de commerces en déclin** — Secteurs NAF vulnérables
5. **Focus Commune** — Analyse détaillée commune individuelle
6. **EPCI / Intercommunalités** — Comparaisons territoriales

### 🏪 Analyses thématiques
7. **Commerces manquants** — Déserts commerciaux et carences
8. **Tableaux de bord** — KPI et métriques globales
9. **Données détaillées** — Tableaux exportables (CSV)

---

**💡 Conseil** : Commencez par la page **Tendances par commune** (carte) pour une vue d'ensemble,  
puis explorez les pages thématiques selon vos besoins.
"""
)

# ============================================================================
# MÉTHODOLOGIE
# ============================================================================

st.markdown("---")

st.markdown("## 📚 Méthodologie")

with st.expander("📖 En savoir plus sur les données et calculs"):
    st.markdown(
        """
    ### Sources de données

    - **SIRENE** : Base établissements INSEE (Stock + Enrichissement historique)
    - **INSEE Recensement** : Population communale 2021
    - **INSEE FiLoSoFi** : Revenus médians 2021
    - **France Travail** : Taux de chômage 2022
    - **NAF** : Nomenclature d'activités française (codes 47xx)

    ### Indicateurs clés

    - **Taux de mortalité** : (Nb fermés / Total établissements) × 100
    - **Score de fragilité** : Moyenne normalisée (mortalité + solde + densité + chômage)
    - **Densité commerciale** : Nb actifs / 1000 habitants
    - **Solde net** : Créations - Fermetures

    ### Enrichissement dates historiques (Sprint 5)

    Le fichier SIRENE Stock actuel contient des dates administratives (2024-2026). 
    Nous avons enrichi avec un fichier historique préservant les **vraies dates de cessation** 
    déclarées à l'INSEE, permettant l'analyse temporelle 2015-2024.

    - ✅ 53,7% établissements avec dates historiques
    - ✅ 35 630 fermetures 2015-2024 exploitables
    - ✅ 89,4% établissements fermés avec date réelle
    """
    )

# ============================================================================
# FOOTER
# ============================================================================

st.markdown("---")

st.markdown(config.FOOTER_TEXT)

st.markdown(
    """
<div style='text-align: center; color: #666; font-size: 0.9em; margin-top: 2em;'>
    <p>Dashboard développé dans le cadre du projet de stage M2 Data Science</p>
    <p>CCI Grand Hainaut × Université de Valenciennes</p>
</div>
""",
    unsafe_allow_html=True,
)
