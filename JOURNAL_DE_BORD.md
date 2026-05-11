# 📓 JOURNAL DE BORD — Dashboard Commercial Nord 59
**Auteur** : Lucie Pintiaux | **Démarrage** : 08/05/2026

---

## 📅 Session du 08/05/2026

### ⏱️ Durée : ~2h
### 🎯 Sprint : Sprint 0 — Initialisation
### 📋 US : US-000 + US-001-PREP

### ✅ Tâches réalisées
- [x] Repo GitHub créé (public, MIT, .gitignore Python)
- [x] Repo cloné localement dans "Dynamique commerciale 59"
- [x] Virtualenv .venv créé et activé
- [x] Arborescence complète créée (13 dossiers)
- [x] Dépendances installées (pandas 3.0.2, streamlit 1.57.0, plotly 6.7.0, scikit-learn 1.8.0...)
- [x] requirements.txt généré (pip freeze)
- [x] .env.example + .env créés
- [x] CONTRIBUTING.md + CODE_OF_CONDUCT.md créés
- [x] README professionnel avec badges et tableaux
- [x] Pre-commit hooks configurés (black, flake8, isort)
- [x] Notebook 00_sprint0_setup.ipynb créé et validé (4 vérifications ✅)
- [x] Journal de bord initié
- [x] 2 commits pushés sur GitHub

### 📁 Fichiers créés/modifiés
- `README.md` — enrichi (badges, fonctionnalités, stack, roadmap)
- `requirements.txt` — généré via pip freeze
- `.env.example` — template variables environnement
- `.pre-commit-config.yaml` — black + flake8 + isort
- `CONTRIBUTING.md` — guidelines contribution
- `CODE_OF_CONDUCT.md` — code de conduite
- `JOURNAL_DE_BORD.md` — ce fichier
- `notebooks/00_sprint0_setup.ipynb` — vérification environnement

### 💬 Décisions prises
- Python 3.14.3 → versions libres des dépendances (pas de pin strict)
- geopandas reporté à Sprint 3 (installation complexe Windows)
- Notebooks Jupyter dans VSCode pour tout le code data
- Scripts .py dans src/ pour code réutilisable et dashboard

### 🚧 Blocages rencontrés
- **Problème** : pandas 2.2.3 incompatible Python 3.14
  **Solution** : pip sans version fixe → pandas 3.0.2 installé
- **Problème** : pre-commit non trouvé dans le venv
  **Solution** : pip install pre-commit dans le terminal VSCode

### 📊 Métriques
- Story points terminés : 5 (US-000 + US-001-PREP)
- Dossiers créés : 13
- Fichiers créés : 8
- Dépendances installées : ~50 packages

### 🔄 Git
- `feat: init projet Sprint 0 - arborescence, venv, requirements, documentation`
- `feat: Sprint 0 complete - pre-commit hooks, README, journal de bord, notebook setup`

### ⏭️ Prochaine session — Sprint 1
- Créer notebook `01_sprint1_collecte_sirene.ipynb`
- US-002 : Télécharger fichier SIRENE StockEtablissement
- US-003 : Filtrer DEP=59 + NAF=47xx
- US-004 : Documenter source et date extraction

---
---

## 📅 Session du 08/05/2026 — Sprint 1

### ⏱️ Durée : ~2h
### 🎯 Sprint : Sprint 1 — Collecte données SIRENE
### 📋 US : US-002 + US-003 + US-004

### ✅ Tâches réalisées
- [x] Notebook `01_sprint1_collecte_sirene.ipynb` créé
- [x] Nouvelle URL SIRENE identifiée (data.gouv.fr mis à jour)
- [x] Téléchargement SIRENE StockEtablissement (2 692 Mo en 22 min)
- [x] Extraction ZIP et lecture par chunks (43,3M lignes)
- [x] Filtrage DEP=59 + NAF=47xx → 98 369 établissements
- [x] Sauvegarde `sirene_nord59_20260507.csv` (22.3 Mo)
- [x] Checksum MD5 calculé
- [x] METADATA.md créé et documenté

### 📁 Fichiers créés/modifiés
- `notebooks/01_sprint1_collecte_sirene.ipynb` — collecte complète
- `data/raw/sirene_nord59_20260507.csv` — dataset filtré (98 369 lignes)
- `data/raw/METADATA.md` — documentation source

### 💬 Décisions prises
- Lecture par chunks de 100 000 lignes (fichier 4 Go non chargeable en mémoire)
- dtype=str pour éviter les conversions automatiques erronées
- Fichier ZIP conservé dans data/raw/ pour reproductibilité

### 🚧 Blocages rencontrés
- **Problème** : URL SIRENE originale retourne 404
  **Solution** : Nouvelle URL trouvée sur data.gouv.fr → `object.files.data.gouv.fr`

### 📊 Métriques
- Story points terminés : 9 (US-002 + US-003 + US-004)
- Total établissements : 98 369
- Actifs : 39 261 (39.9%)
- Fermés : 59 108 (60.1%)
- Communes couvertes : 647/648

### 🔄 Git
- `feat: Sprint 1 complete - collecte SIRENE Nord59, filtrage NAF47, metadata`

### ⏭️ Prochaine session — Sprint 2
- Nettoyage valeurs manquantes et doublons (US-010)
- Enrichissement données INSEE population/revenus (US-011)
- Décodage hiérarchie NAF complète (US-012)

---
---

## 📅 Session du 11/05/2026 — Sprint 2

### ⏱️ Durée : ~4h
### 🎯 Sprint : Sprint 2 — Nettoyage & Enrichissement
### 📋 US : US-010, US-011, US-012

### ✅ Tâches réalisées
- [x] US-010 : Nettoyage complet du dataset SIRENE (valeurs manquantes, doublons)
- [x] US-010 : Création colonnes temporelles (date_fermeture, annee_creation, annee_fermeture)
- [x] US-010 : Réduction 54 → 13 colonnes (-76%), sauvegarde dataset nettoyé
- [x] US-011 : Téléchargement 3 sources INSEE (population, emploi, revenus)
- [x] US-011 : Filtrage département 59 (647-648 communes)
- [x] US-011 : 3 jointures left sur code_commune (6 colonnes ajoutées)
- [x] US-011 : Sauvegarde dataset enrichi INSEE (17,99 Mo, 20 colonnes)
- [x] US-012 : Téléchargement référentiel NAF révision 2 (1 728 codes)
- [x] US-012 : Extraction hiérarchie NAF 5 niveaux (section, division, groupe, classe, sous-classe)
- [x] US-012 : Jointure NAF avec dataset (98,99% correspondance initiale)
- [x] US-012 : Mapping manuel 10 codes NAF anciens (996 établissements)
- [x] US-012 : Complétude NAF finale 100% (98 369 / 98 369)
- [x] US-012 : Sauvegarde dataset final complet (49,45 Mo, 30 colonnes)

### 📁 Fichiers créés/modifiés
- `notebooks/02_sprint2_nettoyage_enrichissement.ipynb` — nettoyage + enrichissement complet
- `data/processed/etablissements_nettoyes_20260511.csv` — 12,06 Mo, 13 colonnes
- `data/processed/METADATA_nettoyage_20260511.md` — documentation nettoyage
- `data/processed/etablissements_enrichis_20260511.csv` — 17,99 Mo, 20 colonnes (INSEE)
- `data/processed/METADATA_enrichissement_20260511.md` — documentation enrichissement INSEE
- `data/processed/etablissements_enrichis_complet_20260511.csv` — 49,45 Mo, 30 colonnes (final)
- `data/processed/METADATA_enrichissement_complet_20260511.md` — documentation complète
- `data/raw/insee_extracted/` — 3 fichiers INSEE extraits (79 Mo)
- `data/raw/naf_rev2_libelles.xls` — référentiel NAF (305 Ko)

### 💬 Décisions prises
- **Colonnes conservées** : 10/54 après nettoyage (SIRET, commune, NAF, état, dates, coordonnées)
- **Fichier revenus INSEE** : FILO2021_DEC_PAUVRES_COM.csv inadapté (100% valeurs masquées) → à remplacer par FILO2021_DISP_COM.csv en V2
- **Codes NAF anciens** : Mapping manuel créé pour 10 codes format 47.XX (47.01-47.10) absents du référentiel NAF Rev2
- **Taille fichier** : Augmentation 17,99 Mo → 49,45 Mo (+175%) acceptable pour analyse exploratoire, optimisation Parquet recommandée en production

### 🚧 Blocages rencontrés
- **Problème** : Fichier population INSEE séparateur ',' au lieu de ';'
  **Solution** : Détection automatique et correction du séparateur
  
- **Problème** : Fichier emploi INSEE volumineux (154 Mo), codes 59 non au début
  **Solution** : Chargement complet puis filtrage (8,9 secondes)
  
- **Problème** : Module xlrd manquant pour lire fichier NAF .xls
  **Solution** : Installation via `pip install xlrd`
  
- **Problème** : 996 codes NAF anciens (1,01%) absents du référentiel
  **Solution** : Création mapping manuel 10 codes (47.01-47.10) avec libellés et hiérarchie

### 📊 Métriques
- **Story points terminés** : 18 (US-010: 5 pts, US-011: 8 pts, US-012: 5 pts)
- **Total vélocité Sprint 2** : 18/23 story points prévus (78%)
- **Dataset final** : 98 369 lignes × 30 colonnes (49,45 Mo)
- **Complétude globale** :
  - Identification : 100%
  - NAF : 100% (dont 996 codes anciens mappés)
  - Population INSEE : 99,99%
  - Chômage INSEE : 100%
  - Revenus INSEE : 90,29% (secret statistique)
  - Taux pauvreté : 0% (fichier source inadapté)
- **Commune manquante** : Bermeries (59070, 12 établissements)
- **Codes NAF uniques** : 97 (87 référentiel + 10 anciens)

### 🔄 Git
- `feat: Sprint 2 - US-010 nettoyage dataset SIRENE (13 colonnes)`
- `feat: Sprint 2 - US-011 enrichissement INSEE (population, chômage, revenus)`
- `feat: Sprint 2 - US-012 enrichissement NAF hiérarchie complète (100% correspondance)`

### 📝 Notes & Apprentissages
- **Secret statistique INSEE** : Communes < 50 ménages ont données masquées ("s") pour protéger anonymat
- **Codes NAF anciens** : Pré-2008, format classe sans suffixe (47.04 vs 47.11A)
- **Hiérarchie NAF** : 5 niveaux (Section G → Division 47 → Groupe 47.1 → Classe 47.11 → Sous-classe 47.11A)
- **Optimisation fichier** : Format Parquet réduirait taille de 60-70% (49 Mo → ~15 Mo)
- **Jointures left** : Conservent 100% établissements même si correspondance manquante (NaN au lieu de perte ligne)

### ⏭️ Prochaine session — Sprint 2 (fin)
- US-013 : Création dictionnaire de données complet (colonnes, types, sources, descriptions)
- US-014 : Création fichier codes EPCI/CA (67 communes, 17 EPCI)
- Sprint Review : Démo des 3 datasets produits
- Sprint Retrospective : Bilan vélocité et amélioration continue

---