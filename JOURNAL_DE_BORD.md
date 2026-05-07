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