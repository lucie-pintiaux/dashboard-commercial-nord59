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
