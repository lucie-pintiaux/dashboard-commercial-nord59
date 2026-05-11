# 📊 Dashboard Commercial Nord 59 — Dynamique Territoriale

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-FF4B4B.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

**Dashboard interactif d'analyse de la dynamique commerciale du département du Nord (59)**

Projet open-source développé selon la méthode Scrum pour visualiser, analyser et comparer la situation commerciale des 648 communes du Nord à partir des données SIRENE enrichies.

---

## 🎯 Problème & Solution

### Problème identifié
Les acteurs du développement économique (CCI, collectivités, communautés d'agglomération) manquent d'outils accessibles pour :
- Identifier rapidement les communes en fragilité commerciale
- Analyser les tendances sectorielles et temporelles
- Prioriser les interventions publiques avec des données objectives

### Solution proposée
**Dashboard web interactif** permettant de :
- ✅ Visualiser la vacance commerciale par commune (carte choroplèthe)
- ✅ Comparer les territoires intercommunaux (EPCI/CA)
- ✅ Analyser les évolutions 2015-2024 (créations/fermetures)
- ✅ Identifier les commerces manquants par commune
- ✅ Filtrer par secteur d'activité (NAF) et type de commerce

---

## 🚀 Fonctionnalités

### ✅ Réalisées (Sprint 0-2)

#### Sprint 0 — Initialisation
- [x] Repository GitHub + structure projet professionnelle
- [x] Environnement Python + dépendances (pandas, streamlit, plotly, scikit-learn)
- [x] Documentation initiale (README, CONTRIBUTING, CODE_OF_CONDUCT)

#### Sprint 1 — Collecte données SIRENE
- [x] Téléchargement automatique SIRENE StockEtablissement (2,7 Go)
- [x] Filtrage département 59 + NAF 47xx (commerce de détail)
- [x] **98 369 établissements** collectés (39% actifs, 61% fermés)
- [x] 647/648 communes couvertes

#### Sprint 2 — Nettoyage & Enrichissement
- [x] **US-010 : Nettoyage complet** 
  - Suppression doublons, traitement valeurs manquantes
  - Création colonnes temporelles (dates création/fermeture)
  - Réduction 54 → 13 colonnes (-76%)
  
- [x] **US-011 : Enrichissement données INSEE**
  - Population communale 2021 (99,99% complétude)
  - Taux de chômage 15-64 ans (100% complétude)
  - Revenus médians 2021 (90% complétude, secret statistique)
  
- [x] **US-012 : Enrichissement hiérarchie NAF complète**
  - 11 colonnes NAF (section, division, groupe, classe, sous-classe + libellés)
  - 100% de correspondance (87 codes référentiel + 10 codes anciens mappés)
  - Hiérarchie complète pour analyses sectorielles

**Dataset final actuel** : **98 369 établissements × 30 colonnes (49 Mo)**

### 🔄 En cours (Sprint 2 — fin)
- [ ] US-013 : Création dictionnaire de données complet
- [ ] US-014 : Fichier codes EPCI/Communautés d'Agglomération

### 📋 Prochains sprints (Sprint 3-8)

#### Sprint 3 — Exploration & KPI (13 SP)
- [ ] Calcul indicateurs par commune (taux mortalité, solde créations/fermetures)
- [ ] Carte interactive vacance commerciale
- [ ] Analyse temporelle 2015-2024 avec rupture COVID

#### Sprint 4 — Analyses avancées (21 SP)
- [ ] Score de fragilité composite (0-100)
- [ ] Clustering communes (K-means, 4 profils)
- [ ] Identification commerces manquants par commune
- [ ] Analyse impact COVID

#### Sprint 5 — Dashboard MVP (21 SP)
- [ ] 5 pages Streamlit : Vue d'ensemble, Focus Commune, Analyse EPCI, Analyse Sectorielle, Documentation
- [ ] Carte choroplèthe interactive
- [ ] Filtres dynamiques (EPCI, secteur NAF, état)

#### Sprint 6 — Déploiement (13 SP)
- [ ] Déploiement Streamlit Cloud
- [ ] Configuration secrets et cache
- [ ] CI/CD GitHub Actions

#### Sprint 7 — Fonctionnalités avancées CA (13 SP)
- [ ] Export PDF diagnostics communaux
- [ ] Export CSV données filtrées
- [ ] Benchmarking entre CA similaires

#### Sprint 8 — Finalisation (8 SP)
- [ ] Recommandations CCI et CA
- [ ] Documentation complète
- [ ] Vidéo démo (5 min)

---

## 📊 Données & Sources

### Dataset principal
| Source | Périmètre | Lignes | Colonnes | Taille |
|--------|-----------|--------|----------|--------|
| **SIRENE StockEtablissement** | Dept 59, NAF 47xx | 98 369 | 30 | 49 Mo |

### Enrichissements

#### 1. Données INSEE communales (6 colonnes)
- **Population municipale 2021** : 99,99% complétude (1 commune manquante : Bermeries)
- **Taux de chômage 2021** : 100% complétude (15-64 ans)
- **Revenus médians 2021** : 90,29% complétude (secret statistique petites communes)
- **Taux pauvreté** : 0% (fichier source inadapté, à corriger)

#### 2. Hiérarchie NAF révision 2 (11 colonnes)
- **Référentiel INSEE** : 1 728 codes tous secteurs, 87 codes division 47
- **Complétude** : 100% (996 codes anciens mappés manuellement)
- **5 niveaux** : Section G → Division 47 → Groupe (47.1-47.9) → Classe (47.11) → Sous-classe (47.11A)

### Périmètre géographique
- **Département** : Nord (59)
- **Communes** : 647/648 (99,85%)
- **EPCI** : 17 intercommunalités
- **Secteur d'activité** : NAF 47 (Commerce de détail, hors automobiles/motocycles)

---

## 🛠️ Stack Technique

### Backend & Data
- **Python 3.11+** — Langage principal
- **Pandas 2.2+** — Manipulation données
- **NumPy** — Calculs numériques
- **Scikit-learn** — Clustering et scoring

### Visualisation
- **Streamlit 1.28+** — Framework dashboard
- **Plotly 5.18+** — Graphiques interactifs
- **Folium / Plotly** — Cartes géographiques

### Qualité & DevOps
- **Black** — Formatage code
- **Flake8** — Linting
- **Pytest** — Tests unitaires
- **Pre-commit hooks** — Validation automatique
- **GitHub Actions** — CI/CD (Sprint 6)

---

## 📂 Structure du Projet
dashboard-commercial-nord59/
├── .github/
│   └── workflows/              # CI/CD (Sprint 6)
├── data/
│   ├── raw/                    # SIRENE brut + référentiels
│   │   ├── sirene_nord59_20260507.csv (22 Mo)
│   │   ├── naf_rev2_libelles.xls (305 Ko)
│   │   └── METADATA.md
│   ├── processed/              # Datasets enrichis
│   │   ├── etablissements_enrichis_complet_20260511.csv (49 Mo)
│   │   └── METADATA_enrichissement_complet_20260511.md
│   └── external/               # Données tierces
├── docs/                       # Documentation
├── notebooks/                  # Exploration Jupyter
│   ├── 00_sprint0_setup.ipynb
│   ├── 01_sprint1_collecte_sirene.ipynb
│   └── 02_sprint2_nettoyage_enrichissement.ipynb
├── src/
│   ├── dashboard/              # Application Streamlit (Sprint 5)
│   ├── data/                   # Scripts collecte/nettoyage
│   ├── models/                 # Scoring/clustering (Sprint 4)
│   └── utils/                  # Fonctions utilitaires
├── tests/                      # Tests unitaires
├── .env.example                # Template variables
├── .gitignore
├── .pre-commit-config.yaml
├── JOURNAL_DE_BORD.md          # Suivi quotidien
├── PRODUCT_BACKLOG.md          # User stories
├── README.md                   # Ce fichier
└── requirements.txt            # Dépendances Python
---

## 🚦 Installation

### Prérequis
- Python 3.11+ installé
- Git installé
- 4 Go RAM minimum (chargement datasets)

### 1. Cloner le repository

```bash
git clone https://github.com/ton-username/dashboard-commercial-nord59.git
cd dashboard-commercial-nord59
```

### 2. Créer environnement virtuel

Windows :
```bash
python -m venv .venv
.venv\Scripts\activate
```

Linux/Mac :
```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Installer dépendances

```bash
pip install -r requirements.txt
```

### 4. Configuration environnement

```bash
cp .env.example .env
```

Éditer .env selon vos besoins

### 5. Lancer le dashboard (Sprint 5+)

```bash
streamlit run src/dashboard/app.py
```

---

## 📊 Utilisation

### Notebooks d'exploration (Sprint 0-4)

```bash
jupyter notebook notebooks/
```

**Notebooks disponibles** :
- `00_sprint0_setup.ipynb` — Vérification environnement
- `01_sprint1_collecte_sirene.ipynb` — Collecte données SIRENE
- `02_sprint2_nettoyage_enrichissement.ipynb` — Nettoyage + enrichissement INSEE/NAF
- `03_sprint3_exploration.ipynb` — (À venir) KPI et visualisations
- `04_sprint4_analyses_avancees.ipynb` — (À venir) Scoring et clustering

### Dashboard web (Sprint 5+)

```bash
streamlit run src/dashboard/app.py
```

Interface accessible sur http://localhost:8501

---

## 👥 Personas Utilisateurs

### Primaires (MVP Sprint 5)
1. **Sophie Marchand** — Chargée de mission CCI
   - Besoin : Analyses territoriales rapides, identification communes prioritaires
   
2. **Claire Deschamps** — Vice-Présidente CA
   - Besoin : Arbitrage budgétaire 800k€, comparaison EPCI
   
3. **Fatima Benali** — Élue municipale
   - Besoin : Diagnostic communal, comparaison avec communes similaires

### Secondaires (Sprint 7)
4. **Jean-Pierre Leclercq** — Directeur CCI (vision stratégique)
5. **Julien Vasseur** — DGS CA (évaluation politiques publiques)
6. **Isabelle Vanderhaegen** — Directrice acquisitions immobilier

---

## 📈 Avancement du Projet

### Métriques globales
| Métrique | Valeur |
|----------|--------|
| **Sprints complétés** | 2 / 8 (25%) |
| **Story points complétés** | 32 / 110 (29%) |
| **User Stories terminées** | 7 / 44 (16%) |
| **Vélocité moyenne** | 16 SP/sprint |

### Sprint en cours : Sprint 2 (fin) — US-013, US-014
**Objectif** : Dictionnaire de données + Fichier EPCI  
**Progression** : 18/23 SP (78%)

### Prochains jalons
- **Fin Mai 2026** : Sprint 3 — Exploration & KPI
- **Début Juin 2026** : Sprint 4 — Scoring & clustering
- **Mi-Juin 2026** : Sprint 5 — Dashboard MVP déployé
- **Fin Juin 2026** : Sprints 6-8 — Finalisation & recommandations

---

## 🤝 Contribution

Les contributions sont les bienvenues ! Merci de lire CONTRIBUTING.md avant de proposer une pull request.

### Quick start contributeurs
1. Fork le projet
2. Créer une branche feature : `git checkout -b feature/AmazingFeature`
3. Commit les changements : `git commit -m 'feat: Add AmazingFeature'`
4. Push sur la branche : `git push origin feature/AmazingFeature`
5. Ouvrir une Pull Request

### Conventions
- **Commits** : Format conventionnel (feat:, fix:, docs:, refactor:)
- **Code** : PEP 8, type hints, docstrings Google style
- **Tests** : Coverage > 80%

---

## 📜 Licence

Ce projet est sous licence MIT. Voir LICENSE pour plus de détails.

---

## 📞 Contact & Ressources

### Auteur
**Lucie Pintiaux** — Analyste Data & Product Owner

### Liens utiles
- 📊 Données SIRENE : https://www.data.gouv.fr/fr/datasets/base-sirene-des-entreprises-et-de-leurs-etablissements-siren-siret/
- 📈 INSEE Recensement : https://www.insee.fr/fr/statistiques
- 🏪 Nomenclature NAF : https://www.insee.fr/fr/information/2406147
- 🏛️ Action Cœur de Ville : https://agence-cohesion-territoires.gouv.fr/action-coeur-de-ville-42

---

## 🙏 Remerciements

- **INSEE** pour les données SIRENE et les référentiels
- **Data.gouv.fr** pour la mise à disposition des données publiques
- **Communauté Streamlit** pour le framework
- **CCI Hauts-de-France** pour l'inspiration du projet

---

**⭐ Si ce projet vous est utile, n'hésitez pas à lui donner une étoile sur GitHub !**

---

**Dernière mise à jour** : 11/05/2026  
**Version** : 0.2.0 (Sprint 2 complété)