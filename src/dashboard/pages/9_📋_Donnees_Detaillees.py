"""
Page 9 - Données détaillées
Exports et données brutes
"""

import streamlit as st
import pandas as pd
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent / "utils"))
import config
import data_loader

st.set_page_config(page_title="Données détaillées", page_icon="📋", layout=config.LAYOUT)

st.title("📋 Données détaillées")
st.markdown("### Accès aux données brutes et exports")
st.markdown("---")

# ============================================================================
# INTRODUCTION
# ============================================================================

st.markdown("""
Cette page vous permet d'accéder aux données brutes du dashboard pour vos propres analyses.

**Formats disponibles** :
- 📊 Visualisation interactive dans le navigateur
- 💾 Export CSV pour Excel, R, Python, etc.

**Licence** : Données publiques sous licence ouverte (SIRENE INSEE)
""")

st.markdown("---")

# ============================================================================
# SÉLECTION DATASET
# ============================================================================

st.markdown("## 📂 Sélection du dataset")

datasets_disponibles = {
    "Communes (avec GPS)": "communes",
    "Établissements (avec GPS)": "etablissements",
    "Commerces manquants": "commerces_manquants",
    "Secteurs vulnérables": "secteurs_vulnerables"
}

dataset_choisi = st.selectbox(
    "Choisissez un dataset",
    list(datasets_disponibles.keys())
)

st.markdown("---")

# ============================================================================
# CHARGEMENT DATASET SÉLECTIONNÉ
# ============================================================================

dataset_key = datasets_disponibles[dataset_choisi]

with st.spinner(f"Chargement {dataset_choisi}..."):
    if dataset_key == "communes":
        df = data_loader.load_communes_avec_gps()
    elif dataset_key == "etablissements":
        df = data_loader.load_etablissements(nrows=10000)  # Limiter à 10k pour performance
        if df is not None and len(df) == 10000:
            st.info("ℹ️ Affichage limité aux 10 000 premières lignes pour performance. Utilisez l'export CSV pour données complètes.")
    elif dataset_key == "commerces_manquants":
        df = data_loader.load_commerces_manquants()
    elif dataset_key == "secteurs_vulnerables":
        df = data_loader.load_secteurs_vulnerables()
    else:
        df = None

if df is None:
    st.error("❌ Impossible de charger le dataset")
    st.stop()

# ============================================================================
# STATISTIQUES DATASET
# ============================================================================

st.markdown(f"## 📊 Statistiques - {dataset_choisi}")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Nombre de lignes", f"{len(df):,}".replace(',', ' '))

with col2:
    st.metric("Nombre de colonnes", len(df.columns))

with col3:
    taille_mb = df.memory_usage(deep=True).sum() / (1024**2)
    st.metric("Taille mémoire", f"{taille_mb:.1f} MB")

with col4:
    valeurs_manquantes = df.isnull().sum().sum()
    st.metric("Valeurs manquantes", f"{valeurs_manquantes:,}".replace(',', ' '))

st.markdown("---")

# ============================================================================
# BOUTON EXPORT CSV
# ============================================================================

st.markdown("## 💾 Export CSV")

csv = df.to_csv(index=False, encoding='utf-8-sig')  # UTF-8 with BOM pour Excel

st.download_button(
    label=f"📥 Télécharger {dataset_choisi} (CSV)",
    data=csv,
    file_name=f"{dataset_key}_{pd.Timestamp.now().strftime('%Y%m%d')}.csv",
    mime="text/csv"
)

st.markdown("---")

# ============================================================================
# APERÇU DONNÉES
# ============================================================================

st.markdown("## 👁️ Aperçu des données")

# Slider nombre lignes
nb_lignes = st.slider("Nombre de lignes à afficher", 5, 100, 20)

st.dataframe(df.head(nb_lignes), use_container_width=True)

st.markdown("---")

# ============================================================================
# STRUCTURE DONNÉES (COLONNES)
# ============================================================================

st.markdown("## 📋 Structure des données")

with st.expander("Voir la liste des colonnes et types"):
    df_structure = pd.DataFrame({
        'Colonne': df.columns,
        'Type': df.dtypes.astype(str),
        'Valeurs uniques': [df[col].nunique() for col in df.columns],
        'Valeurs manquantes': [df[col].isnull().sum() for col in df.columns],
        '% manquantes': [(df[col].isnull().sum() / len(df) * 100).round(1) for col in df.columns]
    })

    st.dataframe(df_structure, use_container_width=True, hide_index=True)

st.markdown("---")

# ============================================================================
# STATISTIQUES DESCRIPTIVES
# ============================================================================

st.markdown("## 📈 Statistiques descriptives")

with st.expander("Voir les statistiques des colonnes numériques"):
    colonnes_numeriques = df.select_dtypes(include=['int64', 'float64']).columns

    if len(colonnes_numeriques) > 0:
        st.dataframe(df[colonnes_numeriques].describe(), use_container_width=True)
    else:
        st.info("Aucune colonne numérique dans ce dataset")

st.markdown("---")

# ============================================================================
# FILTRES SIMPLES
# ============================================================================

st.markdown("## 🔍 Filtres rapides")

if dataset_key == "communes":
    col1, col2 = st.columns(2)

    with col1:
        if 'profil' in df.columns:
            profils = ['Tous'] + sorted(df['profil'].dropna().unique().tolist())
            filtre_profil = st.selectbox("Filtrer par profil", profils)

            if filtre_profil != 'Tous':
                df_filtre = df[df['profil'] == filtre_profil]
                st.info(f"{len(df_filtre)} communes avec profil '{filtre_profil}'")

    with col2:
        if 'categorie_priorite' in df.columns:
            categories = ['Tous'] + sorted(df['categorie_priorite'].dropna().unique().tolist())
            filtre_cat = st.selectbox("Filtrer par catégorie", categories)

            if filtre_cat != 'Tous':
                df_filtre = df[df['categorie_priorite'] == filtre_cat]
                st.info(f"{len(df_filtre)} communes avec catégorie '{filtre_cat}'")

elif dataset_key == "etablissements":
    col1, col2 = st.columns(2)

    with col1:
        if 'etat_administratif' in df.columns:
            etats = ['Tous'] + sorted(df['etat_administratif'].dropna().unique().tolist())
            filtre_etat = st.selectbox("Filtrer par état", etats)

            if filtre_etat != 'Tous':
                df_filtre = df[df['etat_administratif'] == filtre_etat]
                st.info(f"{len(df_filtre)} établissements avec état '{filtre_etat}'")

    with col2:
        if 'naf_classe' in df.columns:
            st.text_input("Rechercher un secteur NAF", help="Ex: 4711, boulangerie, etc.")

st.markdown("---")

# ============================================================================
# DOCUMENTATION
# ============================================================================

st.markdown("## 📚 Documentation")

with st.expander("ℹ️ À propos des données"):
    st.markdown("""
    ### Sources
    - **SIRENE** : Base établissements INSEE (2024)
    - **INSEE** : Population, chômage, revenus communaux
    - **Traitement** : Sprint 4 (scoring, clustering, enrichissement GPS)

    ### Mises à jour
    - Données SIRENE : Snapshot 2024
    - Coordonnées GPS : Converties Lambert 93 → WGS84
    - Enrichissements : Sprint 4 (mai 2026)

    ### Limitations
    - Snapshot ponctuel (pas de flux temps réel)
    - Délai radiations établissements (~6 mois)
    - Coordonnées GPS : 99,2% communes (5 manquantes)

    ### Contact
    - GitHub : dashboard-commercial-nord59
    - Auteur : Lucie Pintiaux
    - Licence : Données publiques (Licence Ouverte)
    """)

st.markdown("---")
st.markdown(config.FOOTER_TEXT)
