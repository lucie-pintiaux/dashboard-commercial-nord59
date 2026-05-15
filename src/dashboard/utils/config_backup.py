"""
Configuration centralisée du dashboard
"""

import os

# ============================================================================
# CHEMINS FICHIERS (CHEMINS ABSOLUS)
# ============================================================================

# Chemin racine projet (remonter de src/dashboard/utils/ vers racine)
BASE_DIR = r"C:\Users\lpint\OneDrive\Bureau\Dynamique commerciale 59\dashboard-commercial-nord59"
DATA_DIR = os.path.join(BASE_DIR, "data", "processed")

# Fichiers de données
COMMUNES_FILE = os.path.join(DATA_DIR, "communes_avec_gps_20260513.csv")
COMMERCES_MANQUANTS_FILE = os.path.join(DATA_DIR, "commerces_manquants_20260512.csv")
SECTEURS_VULNERABLES_FILE = os.path.join(DATA_DIR, "secteurs_vulnerables_20260512.csv")
ETABLISSEMENTS_FILE = os.path.join(DATA_DIR, "etablissements_avec_gps_20260513.csv")

# ============================================================================
# CONFIGURATION STREAMLIT
# ============================================================================

PAGE_TITLE = "Dashboard Commercial Nord 59"
LAYOUT = "wide"
PAGE_ICON = "📊"

# ============================================================================
# COULEURS MOCKUP
# ============================================================================

COLOR_PRIMARY = "#1f77b4"
COLOR_SUCCESS = "#2ca02c"
COLOR_DANGER = "#d62728"
COLOR_WARNING = "#ff9800"

# Couleurs priorités
COLOR_PRIORITE_A = "#d32f2f"
COLOR_PRIORITE_B = "#ff9800"
COLOR_NON_PRIORITAIRE = "#66bb6a"

# Couleurs profils
COLOR_DYNAMIQUE = "#4caf50"
COLOR_PRECAIRE = "#ff9800"
COLOR_METROPOLE = "#e91e63"
COLOR_DESERTIFIE = "#9e9e9e"

# Colorscale carte choroplèthe
COLORSCALE_CHOROPLETH = [
    [0.0, "#4caf50"],  # Vert
    [0.5, "#ff9800"],  # Orange
    [1.0, "#d32f2f"],  # Rouge
]

# ============================================================================
# SEUILS MÉTIER
# ============================================================================

SEUIL_TAUX_DYNAMIQUE = 45
SEUIL_TAUX_FRAGILE = 55
SEUIL_SCORE_PRIORITE_A = 60
SEUIL_DENSITE_FAIBLE = 8

# ============================================================================
# FOOTER
# ============================================================================

FOOTER_TEXT = """
---
**Source** : SIRENE INSEE (2024) | **Projet** : Lucie Pintiaux | **Version** : 0.5.0 (Sprint 5)
"""
