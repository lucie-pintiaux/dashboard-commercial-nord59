"""
Configuration centralisée du dashboard
"""

import os
from pathlib import Path

# ============================================================================
# CHEMINS PROJET (COMPATIBLES WINDOWS + LINUX)
# ============================================================================

# Détection automatique racine projet
# Depuis src/dashboard/utils/ → remonter 3 niveaux
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

# Chemins data
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
EXTERNAL_DATA_DIR = DATA_DIR / "external"

# Chemins outputs
OUTPUTS_DIR = BASE_DIR / "outputs"

# ============================================================================
# FICHIERS DONNÉES
# ============================================================================

# Fichiers principaux
COMMUNES_FILE = PROCESSED_DATA_DIR / "communes_avec_gps_20260513.csv"
COMMUNES_GPS_FILE = PROCESSED_DATA_DIR / "communes_avec_gps_20260513.csv"
ETABLISSEMENTS_FILE = PROCESSED_DATA_DIR / "etablissements_enrichis_final_20260513.csv"
COMMERCES_MANQUANTS_FILE = PROCESSED_DATA_DIR / "commerces_manquants_20260512.csv"
SECTEURS_VULNERABLES_FILE = PROCESSED_DATA_DIR / "secteurs_vulnerables_20260512.csv"

# ============================================================================
# CONFIGURATION STREAMLIT
# ============================================================================

PAGE_TITLE = "Dashboard Commercial Nord 59"
PAGE_ICON = "📊"
LAYOUT = "wide"

# ============================================================================
# CONFIGURATION VISUALISATIONS
# ============================================================================

# Couleurs principales
COLOR_ACTIF = "#2ecc71"  # Vert
COLOR_FERME = "#e74c3c"  # Rouge
COLOR_PRIORITAIRE = "#e67e22"  # Orange
COLOR_STABLE = "#3498db"  # Bleu

# Couleurs additionnelles (pour graphiques)
COLOR_SUCCESS = "#2ecc71"  # Vert
COLOR_DANGER = "#e74c3c"  # Rouge
COLOR_WARNING = "#f39c12"  # Orange foncé
COLOR_INFO = "#3498db"  # Bleu
COLOR_PRIMARY = "#9b59b6"  # Violet

# Couleurs par profil commune (4 profils identifiés)
COLOR_DYNAMIQUE = "#27ae60"  # Vert foncé
COLOR_DESERTIFIE = "#e74c3c"  # Rouge
COLOR_FRAGILISE = "#e67e22"  # Orange
COLOR_RESILIENT = "#3498db"  # Bleu
COLOR_PRECAIRE = "#d35400"  # Orange brûlé
COLOR_METROPOLE = "#8e44ad"  # Violet

# Couleurs par catégorie priorité
COLOR_PRIORITE_A = "#c0392b"  # Rouge foncé
COLOR_PRIORITE_B = "#e67e22"  # Orange
COLOR_NON_PRIORITAIRE = "#27ae60"  # Vert foncé

# Seuils
SEUIL_FRAGILE = 50  # Score fragilité
SEUIL_PRIORITAIRE = 60  # Score priorité A
SEUIL_DENSITE_FAIBLE = 10  # Commerces/1000 hab

# ============================================================================
# CONFIGURATION CARTES GPS
# ============================================================================

MAPBOX_STYLE = "open-street-map"
MAP_CENTER_LAT = 50.629250  # Centre Nord 59
MAP_CENTER_LON = 3.057256
MAP_ZOOM = 8.5

# ============================================================================
# TEXTES INTERFACE
# ============================================================================

FOOTER_TEXT = """
---
**Dashboard Commercial Nord 59** | Données SIRENE 2024 | Développé par Lucie Pintiaux  
📊 [GitHub](https://github.com/lucie-pintiaux/dashboard-commercial-nord59) | 📧 Contact
"""

ABOUT_TEXT = """
## À propos

Dashboard interactif d'analyse de la dynamique commerciale du département du Nord (59).

**Données** : SIRENE (INSEE 2024), enrichies avec données socio-économiques  
**Périmètre** : 647 communes, 98 369 établissements (NAF 47xx)  
**Mise à jour** : Mai 2026
"""
