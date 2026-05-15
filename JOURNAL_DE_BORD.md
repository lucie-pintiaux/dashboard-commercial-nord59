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
---

## 📅 Session du 12/05/2026 — Sprint 2 (fin)

### ⏱️ Durée : ~3h
### 🎯 Sprint : Sprint 2 — Finalisation
### 📋 US : US-013, US-014

### ✅ Tâches réalisées
- [x] US-013 : Génération dictionnaire de données (30 colonnes documentées)
- [x] US-013 : Correction bug naf_classe_libelle (55,69% → 100%)
- [x] US-013 : Sauvegarde dictionnaire CSV (4,88 Ko)
- [x] US-013 : Sauvegarde dataset corrigé (52,35 Mo, 30 colonnes)
- [x] US-014 : Exploration fichier EPCI 2026 (34 871 lignes)
- [x] US-014 : Filtrage département 59 (17 EPCI, 651 communes)
- [x] US-014 : Création table EPCI-Communes (651 lignes × 5 colonnes)
- [x] US-014 : Jointure EPCI avec dataset principal (99,99% complétude)
- [x] US-014 : Sauvegarde dataset final avec EPCI (56,25 Mo, 33 colonnes)
- [x] Sprint 2 complété à 100% (23/23 story points)

### 📁 Fichiers créés/modifiés
- `notebooks/02_sprint2_nettoyage_enrichissement.ipynb` — US-013 et US-014 ajoutées
- `data/processed/dictionnaire_donnees_20260512.csv` — 4,88 Ko, 30 lignes
- `data/processed/etablissements_enrichis_complet_20260512.csv` — 52,35 Mo, 30 colonnes (correction NAF)
- `data/processed/epci_communes_20260512.csv` — 35,71 Ko, 651 lignes × 5 colonnes
- `data/processed/etablissements_enrichis_final_20260512.csv` — 56,25 Mo, 98 369 × 33 colonnes
- `data/raw/epcicom2026.xlsx` — référentiel EPCI (2 885 Ko)

### 💬 Décisions prises
- **Correction NAF** : naf_classe_libelle manquant pour codes avec suffixe Z → rempli avec naf_libelle (43 592 lignes corrigées)
- **Optimisation EPCI** : Exclusion nb_communes et total_pop_mun (calculables) → seulement 3 colonnes ajoutées au lieu de 5
- **Fichier séparé** : Table de référence EPCI-Communes créée pour filtres dashboard (651 lignes, léger)
- **17 EPCI identifiés** : 8 CA, 7 CC, 1 METRO (MEL - 95 communes), 1 CU (Dunkerque - 17 communes)

### 🚧 Blocages rencontrés
- **Problème** : naf_classe_libelle à 55,69% de complétude (inattendu)
  **Solution** : Codes NAF avec suffixe Z sont des classes sans sous-classes → remplissage automatique
  
- **Problème** : Fichier EPCI nommé epcicom2026.xlsx (avec C) au lieu de epdcom2026
  **Solution** : Correction du chemin dans le code
  
- **Problème** : Kernel Jupyter bloqué sur environnement 'base'
  **Solution** : Changement vers environnement .venv (Python 3.14.3)

### 📊 Métriques
- **Story points terminés** : 5 (US-013: 2 pts, US-014: 3 pts)
- **Total Sprint 2** : 23/23 story points (100%) ✅
- **Dataset final** : 98 369 lignes × 33 colonnes (56,25 Mo)
- **Complétude finale** :
  - NAF (après correction) : 100% (naf_classe_libelle fixé)
  - EPCI : 99,99% (1 commune manquante : Bermeries)
  - Complétude moyenne globale : 92,72%
- **EPCI du Nord** : 17 intercommunalités, 651 communes
- **Fichiers produits Sprint 2** : 9 fichiers (3 datasets intermédiaires + 1 final + 3 métadonnées + 1 dictionnaire + 1 référence EPCI)

### 🔄 Git
- `feat: Sprint 2 - US-013 dictionnaire données (30 colonnes, correction naf_classe_libelle)`
- `feat: Sprint 2 - US-014 fichier EPCI (17 EPCI, 651 communes, 33 colonnes final)`
- `docs: update README, JOURNAL, .gitignore - Sprint 2 complete 100%`

### 📝 Notes & Apprentissages
- **Dictionnaire de données** : 8 dimensions d'information par colonne (nom, type, source, description, valeurs, exemple, complétude, notes)
- **Bug NAF détecté** : Codes avec suffixe Z (47.25Z, 47.77Z...) sont des classes finales sans décomposition en sous-classes
- **EPCI MEL** : 95 communes (14,6% du département), plus grand EPCI du Nord
- **Optimisation taille** : Exclusion colonnes calculables limite augmentation dataset à +7,4% au lieu de +12%
- **Bermeries** : Commune absente de tous les référentiels (INSEE population, EPCI) → commune nouvelle ou fusionnée récente

### ⏭️ Prochaine session — Sprint 3
- US-020 : Calcul indicateurs de base par commune (Nb_actifs, Nb_fermés, Taux_mortalité)
- US-021 : Création carte choroplèthe vacance commerciale
- US-022 : Analyse évolution créations/fermetures 2015-2024
- US-023 : Identification rupture tendance COVID (2020-2021)

---

🎉 **SPRINT 2 COMPLÉTÉ À 100% !** 🎉

**Bilan global Sprint 2** :
- ✅ **5 User Stories terminées** : US-010, US-011, US-012, US-013, US-014
- 📊 **23/23 story points** (vélocité 100%)
- 💾 **Dataset final** : 98 369 établissements × 33 colonnes (56,25 Mo)
- 📁 **9 fichiers produits** : 1 dataset final + 3 intermédiaires + 3 métadonnées + 1 dictionnaire + 1 référence EPCI
- ⏱️ **Durée** : 3 sessions (11-12 mai 2026)
- 🚀 **Prêt pour Sprint 3** : Exploration & KPI

---
---

## 📅 Session du 12/05/2026 — Sprint 3 (complet)

### ⏱️ Durée : ~6h
### 🎯 Sprint : Sprint 3 — Exploration & KPI de base
### 📋 US : US-020, US-021, US-022

### ✅ Tâches réalisées
- [x] US-020 : Calcul indicateurs de base par commune (5 SP)
- [x] US-020 : Agrégation 98 369 établissements → 647 communes
- [x] US-020 : Calcul 5 KPI (total, actifs, fermés, taux_mortalité, densité)
- [x] US-020 : Validation cohérence (39 261 + 59 108 = 98 369 ✅)
- [x] US-021 : Téléchargement GeoJSON communes Nord (648 communes)
- [x] US-021 : Création carte choroplèthe interactive Plotly
- [x] US-021 : Configuration colormap vert→orange→rouge (3 niveaux)
- [x] US-021 : Export HTML optimisé (410 Ko, CDN)
- [x] US-022 : Découverte fichier enrechissement_date_fermeture.csv
- [x] US-022 : Investigation API SIRENE (échec, dates non exploitables)
- [x] US-022 : Enrichissement avec dates fermetures historiques (90% match)
- [x] US-022 : Agrégation temporelle 2015-2024 (créations + fermetures)
- [x] US-022 : Création graphique Plotly 3 courbes (annotations COVID)
- [x] US-022 : Installation Kaleido + export PNG haute résolution
- [x] Sprint Review Sprint 3 réalisée

### 📁 Fichiers créés/modifiés
- `notebooks/03_sprint3_exploration.ipynb` — US-020, US-021, US-022 complètes
- `data/processed/communes_kpi_20260512.csv` — 71,59 Ko, 647 × 13 colonnes
- `data/external/communes_nord59.geojson` — 0,35 Mo, 648 communes
- `outputs/carte_mortalite_commerciale_20260512.html` — 410,84 Ko
- `outputs/evolution_creations_fermetures_20260512.png` — 288 Ko, 2800×1600 px
- `data/raw/enrechissement_date_fermeture.csv` — 37,82 Mo (découverte clé)

### 💬 Décisions prises
- **Dates fermetures SIRENE** : Fichier Stock contient dates administratives (2024-2026), pas dates réelles → Enrichissement nécessaire
- **Fichier enrichissement** : Utilisation version antérieure SIRENE avec dates préservées (90% correspondance)
- **US-022 étendue** : Ajout enrichissement dates (non prévu) car opportunité découverte
- **API SIRENE** : Tests API échoués (400 errors, dates manquantes) → Abandon piste API
- **Export graphiques** : Installation Kaleido pour PNG haute résolution (nécessite restart kernel)
- **US-023 intégrée** : Analyse COVID déjà couverte dans US-022 (zone orange, annotations)

### 🚧 Blocages rencontrés
- **Problème 1** : Dates fermetures toutes en 2024 dans fichier SIRENE Stock  
  **Solution** : Découverte fichier `enrechissement_date_fermeture.csv` avec dates historiques préservées
  
- **Problème 2** : API Recherche-Entreprises retourne 400 Bad Request  
  **Solution** : Tests multiples syntaxes échoués, abandon API, utilisation fichier enrichissement
  
- **Problème 3** : API INSEE requiert token (54h pour 98k requêtes)  
  **Solution** : Temps prohibitif, confirmation utilisation fichier enrichissement
  
- **Problème 4** : Kaleido non installé (ValueError export PNG)  
  **Solution** : `pip install kaleido` + restart kernel Jupyter

### 📊 Métriques
- **Story points terminés** : 18 (US-020: 5, US-021: 8, US-022: 5)
- **Total Sprint 3** : 18/13 SP prévus (138%) ✅
- **Fichiers produits** : 5 (2 data, 2 viz, 1 enrichissement)
- **Correspondance enrichissement** : 90% (88 518 / 98 369 SIRET)
- **Complétude dates fermetures** : 89,43% (52 860 / 59 108 fermés)

### 🔄 Git commits
- `feat: Sprint 3 - US-020 calcul KPI communaux (647 communes, 5 indicateurs)`
- `feat: Sprint 3 - US-021 carte choroplèthe interactive (647 communes, HTML)`
- `feat: Sprint 3 - US-022 analyse temporelle avec dates réelles (2015-2024, PNG HD)`
- `docs: Sprint Review Sprint 3 + update README, JOURNAL, .gitignore`

### 📝 Notes & Apprentissages
- **Fichier SIRENE Stock** : La colonne `date_fermeture` est mise à jour lors des traitements administratifs INSEE, pas à la cessation d'activité réelle
- **Fichiers flux SIRENE** : Alternative pour dates réelles mais 89 fichiers mensuels (180 Go décompressés) → trop lourd pour Sprint 3
- **Version antérieure préservée** : Les anciennes extractions SIRENE conservent parfois les dates originales avant écrasement
- **GeoJSON France** : Source `france-geojson.gregoiredavid.fr` fournit contours départements découpés
- **Plotly CDN** : `include_plotlyjs='cdn'` réduit taille HTML de 80% (3 Mo → 400 Ko)
- **Kaleido** : Package nécessaire pour export PNG/PDF depuis Plotly (nécessite restart kernel après install)
- **Correspondance 90%** : Les 10% SIRET manquants dans fichier enrichissement sont probablement des créations récentes (2023-2024)

### ⏭️ Prochaine session — Sprint 4
- US-030 : Construire score de fragilité composite (0-100)
- US-031 : Segmenter communes en clusters (K-means, 4 profils)
- US-032 : Catégoriser communes en niveaux priorité (A/B/Non)
- US-033 : Identifier commerces manquants par commune

---

🎉 **SPRINT 3 COMPLÉTÉ À 138% !** 🎉

**Bilan global Sprint 3** :
- ✅ **3 User Stories terminées** : US-020, US-021, US-022
- 📊 **18/13 story points** (vélocité 138%)
- 💾 **5 fichiers produits** : 2 datasets + 2 visualisations + 1 enrichissement
- 🎯 **Découverte clé** : Fichier dates fermetures historiques (game changer)
- ⏱️ **Durée** : 1 journée (au lieu de 1 semaine prévue)
- 🚀 **Prêt pour Sprint 4** : Scoring et clustering

---

---

## 📅 Session du 12/05/2026 — Sprint 4 (complet)

### ⏱️ Durée : ~8h (session intensive)
### 🎯 Sprint : Sprint 4 — Analyses avancées & Scoring
### 📋 US : US-030, US-031, US-032, US-033, US-034, US-035

### ✅ Tâches réalisées
- [x] US-030 : Construction score de fragilité composite (0-100)
- [x] US-030 : Normalisation Min-Max 4 variables (exclusion revenu_median)
- [x] US-030 : Validation corrélation score vs mortalité (0.730)
- [x] US-030 : Identification 10 communes exceptionnellement fragiles
- [x] US-031 : Préparation données clustering (standardisation Z-score)
- [x] US-031 : Détermination K optimal (Elbow + Silhouette)
- [x] US-031 : Application K-Means K=4 (convergence 15 itérations)
- [x] US-031 : Nommage profils (Dynamique, Précaire, Métropole, Désertifié)
- [x] US-031 : Analyse répartition (41% Dynamique, 39% Désertifié)
- [x] US-032 : Définition règles métier catégorisation (A/B/Non)
- [x] US-032 : Application règles (13 Priorité A, 190 Priorité B)
- [x] US-032 : Analyse répartition par EPCI (17 EPCI, 1 critique)
- [x] US-033 : Définition 7 commerces essentiels (codes NAF)
- [x] US-033 : Détection absences pour 203 communes prioritaires
- [x] US-033 : Identification 105 déserts commerciaux totaux (7/7 manquants)
- [x] US-034 : Calcul taux fermeture par secteur NAF (46 secteurs)
- [x] US-034 : Filtrage secteurs représentatifs (39 avec ≥100 établissements)
- [x] US-034 : Analyse croisée secteur × profil commune
- [x] US-035 : Calcul matrice corrélations (6 variables)
- [x] US-035 : Identification 3 corrélations fortes (|r| > 0.5)
- [x] US-035 : Tests significativité (p-value)

### 📁 Fichiers créés/modifiés
- `notebooks/04_sprint4_analyses_avancees.ipynb` — Notebook complet Sprint 4
- `data/processed/communes_scored_20260512.csv` — 647 communes × 17 colonnes (88 Ko)
- `data/processed/communes_clustered_20260512.csv` — 647 communes × 19 colonnes (98 Ko)
- `data/processed/communes_categorisees_20260512.csv` — 647 communes × 20 colonnes (107 Ko)
- `data/processed/commerces_manquants_20260512.csv` — 203 communes × 7 colonnes (26 Ko)
- `data/processed/secteurs_vulnerables_20260512.csv` — 39 secteurs × 5 colonnes (4 Ko)

### 💬 Décisions prises
- **Exclusion revenu_median du score** : 65,7% valeurs manquantes (secret INSEE), score basé sur 4 variables au lieu de 5 pour couverture 99,8% communes
- **K=4 retenu malgré silhouette faible (0.301)** : Coude Elbow net + cohérence métier, homogénéité territoriale explique silhouette < 0.4
- **Règles catégorisation ajustées** : 203 communes prioritaires (31%) vs 59 attendues (9%), densité < 8 capture fragilité réelle terrain
- **Coiffeur et Bar exclus analyse commerces manquants** : Codes NAF 96.02A et 56.30Z hors périmètre 47xx, absence à 100% = limite méthodologique
- **Codes NAF obsolètes identifiés** : 3 secteurs à 100% fermeture = anciens codes pré-2008, pas vulnérabilité réelle

### 🚧 Blocages rencontrés
- **Problème 1** : Imports lourds (matplotlib, seaborn, scipy) bloquent kernel Jupyter  
  **Solution** : Imports retirés, calculs manuels p-value, standardisation manuelle Z-score
  
- **Problème 2** : Colonne `code_naf` absente fichier établissements  
  **Solution** : Nom réel = `code_activite`, correction requêtes
  
- **Problème 3** : Colonnes scores absentes fichier clustered lors sauvegarde  
  **Solution** : Fusion avec fichier scored pour récupérer toutes colonnes
  
- **Problème 4** : Colonne `revenu_median` absente fichier clustered  
  **Solution** : Fusion fichiers KPI + clustered pour corrélations

### 📊 Métriques
- **Story points terminés** : 34 SP (US-030: 8, US-031: 8, US-032: 3, US-033: 5, US-034: 5, US-035: 5)
- **Total Sprint 4** : 34/21 SP prévus (162%) ✅
- **Fichiers produits** : 6 datasets (323 Ko total)
- **Communes analysées** : 646-647 selon variables (99,8% couverture)
- **Tests validés** : Corrélation score 0.730, Silhouette 0.301, p-values < 0.05

### 🔄 Git commits
*(À compléter après commit final)*

### 📝 Notes & Apprentissages
- **Silhouette faible ≠ mauvais clustering** : Score 0.301 reflète homogénéité territoriale réelle (écart-type score 5,66), pas défaut méthodologique
- **Score composite vs mortalité** : Deux dimensions distinctes de fragilité, score corrélé chômage (0.848) mais mortalité non (0.126)
- **Polarisation territoriale** : 41% Dynamique vs 39% Désertifié révèle bipolarisation, peu de transitions graduelles (20% Précaire)
- **Déserts commerciaux massifs** : 51,7% communes prioritaires sans aucun commerce essentiel, ampleur inattendue
- **Chômage = prédicteur principal** : r = 0.848 avec score, confirme priorité volet emploi sur soutien commercial direct
- **Codes NAF obsolètes** : Anciens codes (pré-2008) affichent 100% fermeture = reclassement administratif, filtrer avant analyse
- **Métropoles = cas particulier** : Lille + Roubaix forment cluster à part (0,3%), rotation extrême (solde -2983) nécessite stratégie spécifique

### ⏭️ Prochaine session — Sprint 5
- US-040 : Architecture dashboard Streamlit
- US-041 : Page 1 Vue d'ensemble (KPI globaux + carte)
- US-042 : Page 2 Focus Commune (détail + comparaison)
- US-043 : Page 3 Analyse EPCI
- US-044 : Page 4 Analyse Sectorielle
- US-045 : Page 5 Documentation

---

🎊 **SPRINT 4 COMPLÉTÉ À 162% !** 🎊

**Bilan Sprint 4** :
- ✅ **6 User Stories terminées** : US-030 à US-035
- 📊 **34/21 story points** (vélocité 162%)
- 💾 **6 fichiers produits** : scores, clusters, catégories, manquants, secteurs
- 🎯 **Découvertes clés** : Polarisation territoriale, déserts massifs, chômage = prédicteur
- ⏱️ **Durée** : 1 journée intensive (au lieu de 1-2 semaines prévues)
- 🚀 **Prêt pour Sprint 5** : Dashboard MVP (21 SP)

---

## 📅 Session du 13 mai 2026

### ⏱️ Durée : 8 heures (session intensive)

### 🎯 Sprint actuel : Sprint 5 — Dashboard MVP

### ✅ Tâches réalisées

#### Phase 1 : Correction données historiques
- [x] Enrichissement dates fermeture historiques 2015-2024
- [x] Conversion Lambert 93 → WGS84 (70 541 établissements)
- [x] Création fichiers GPS : `etablissements_avec_gps_20260513.csv` + `communes_avec_gps_20260513.csv`
- [x] Validation 642/647 communes avec GPS (99,2%)

#### Phase 2 : Architecture dashboard
- [x] Mise à jour `config.py` avec chemins absolus et PAGE_TITLE
- [x] Création/correction `data_loader.py` avec 6 fonctions cache
- [x] Mise à jour `app.py` avec navigation 9 pages

#### Phase 3 : Création 9 pages dashboard
- [x] Page 1 : Évolution 2015-2024 (graphiques temporels, KPI, analyse périodes)
- [x] Page 2 : Rupture COVID (3 périodes, bar charts, timeline, 3 onglets)
- [x] Page 3 : Tendances Commune (CARTE GPS, filtres, classements, profils)
- [x] Page 4 : Types commerces déclin (Top 10 secteurs, tableau, distribution)
- [x] Page 5 : Focus Commune (recherche 647 communes, détail, comparaison)
- [x] Page 6 : EPCI (filtrage, comparaison 17 territoires, carte conditionnelle)
- [x] Page 7 : Commerces manquants (Top 10, carte GPS 203 communes, tableau)
- [x] Page 8 : Tableaux de bord (KPI multi-dimensions, synthèse globale)
- [x] Page 9 : Données détaillées (exports CSV, statistiques, documentation)

### 📁 Fichiers créés/modifiés

**Données** :
- `data/processed/etablissements_avec_gps_20260513.csv` (55,8 MB)
- `data/processed/communes_avec_gps_20260513.csv` (0,10 MB)

**Configuration** :
- `src/dashboard/utils/config.py`
- `src/dashboard/utils/data_loader.py`
- `src/dashboard/app.py`

**Pages dashboard** (9 fichiers) :
- `src/dashboard/pages/1_📈_Evolution_2015_2024.py`
- `src/dashboard/pages/2_🦠_Rupture_COVID.py`
- `src/dashboard/pages/3_🗺️_Tendances_Commune.py`
- `src/dashboard/pages/4_📉_Types_Commerces_Declin.py`
- `src/dashboard/pages/5_🏘️_Focus_Commune.py`
- `src/dashboard/pages/6_🤝_EPCI_Intercommunalites.py`
- `src/dashboard/pages/7_🏪_Commerces_Manquants.py`
- `src/dashboard/pages/8_📊_Tableaux_Bord.py`
- `src/dashboard/pages/9_📋_Donnees_Detaillees.py`

### 💬 Décisions prises

**Décision 1** : Conversion coordonnées GPS (Lambert 93 → WGS84)
- **Justification** : Plotly Mapbox nécessite WGS84 pour cartes interactives
- **Résultat** : 642/647 communes géolocalisées (99,2%)

**Décision 2** : Chemins absolus dans config.py
- **Justification** : Chemins relatifs causaient erreurs FileNotFoundError
- **Note** : À paramétrer pour déploiement Streamlit Cloud (Sprint 6)

**Décision 3** : Limitation 10k lignes page 9
- **Justification** : Performance navigateur (98k lignes trop lourd)
- **Solution** : Export CSV complet disponible

### 🚧 Blocages rencontrés

**Problème 1** : Colonnes manquantes (`naf_libelle` vs `naf_classe_libelle`)
- **Solution** : Vérification structure datasets via pandas + adaptation code

**Problème 2** : Caractères spéciaux dans f-strings (page 2)
- **Solution** : Pré-calcul variables avant st.metric()

**Problème 3** : Chemins relatifs BASE_DIR incorrects
- **Solution** : Chemins absolus explicites

### 📊 Métriques

- Story points terminés : **21/21 (100%)**
- Pages créées : **9/9**
- Tests passés : **9/9 pages validées**
- Code coverage : N/A (tests manuels)
- Performance : < 3 sec chargement/page


```

### 📝 Notes & Apprentissages

- **Cache Streamlit** : Gain performance 5 sec → < 1 sec avec @st.cache_data
- **Plotly Mapbox** : Scatter map plus rapide que choroplèthe (pas de GeoJSON)
- **UTF-8-sig** : Nécessaire pour exports CSV compatibles Excel Windows
- **Structure multipage** : Numérotation fichiers contrôle ordre menu

### ⏭️ Prochaine session

**Sprint 6 : Déploiement & Sécurité**
- Déploiement Streamlit Cloud
- Configuration secrets/variables environnement
- URL publique accessible 24/7
- Tests sécurité basiques

---

## 📅 Session du 15 mai 2026

### ⏱️ Durée : 6 heures (session intensive déploiement)

### 🎯 Sprint actuel : Sprint 6 — Déploiement & Sécurité

### ✅ Tâches réalisées

#### Phase 1 : Préparation fichiers
- [x] Création requirements.txt avec 10 dépendances
- [x] Adaptation config.py pour chemins relatifs (Path())
- [x] Test local dashboard avec nouveaux chemins
- [x] Correction 13 variables manquantes config.py
- [x] Validation 9/9 pages fonctionnelles en local

#### Phase 2 : Tentative déploiement Option 1 (18 MB)
- [x] Commit requirements.txt + config.py
- [x] Création compte Streamlit Cloud
- [x] Configuration déploiement initial
- [x] Détection erreur : Pages 1-2 non fonctionnelles (données historiques incomplètes)

#### Phase 3 : Déploiement Option 2 (55 MB Git LFS)
- [x] Installation et vérification Git LFS (version 3.7.1)
- [x] Initialisation Git LFS dans repository
- [x] Configuration tracking fichier 55 MB (.gitattributes)
- [x] Modification .gitignore (exception fichier LFS)
- [x] Upload fichier 58 MB via Git LFS (2,3 MB/s)
- [x] Redéploiement Streamlit Cloud automatique
- [x] Validation 9/9 pages 100% fonctionnelles

### 📁 Fichiers créés/modifiés

**Configuration** :
- `requirements.txt` (10 dépendances Python)
- `src/dashboard/utils/config.py` (chemins relatifs + 13 variables)
- `src/dashboard/utils/config_backup.py` (backup chemins absolus)

**Git LFS** :
- `.gitattributes` (tracking Git LFS)
- `.gitignore` (exception fichier 55 MB)

**Données** :
- `data/processed/etablissements_enrichis_final_20260513.csv` (55,8 MB via Git LFS)

**Documentation** :
- `notebooks/06_sprint6_deploiement.ipynb`

### 💬 Décisions prises

**Décision 1** : Option 1 (18 MB) → Option 2 (55 MB Git LFS)
- **Justification** : Pages 1-2 (Évolution et COVID) critiques pour utilisateurs CCI/CA
- **Résultat** : Dashboard 100% fonctionnel avec analyses temporelles complètes

**Décision 2** : Configuration Git LFS
- **Justification** : Fichier 55 MB trop volumineux pour Git standard (> 50 MB)
- **Solution** : Git LFS héberge fichier sur GitHub LFS storage séparé

**Décision 3** : Exception .gitignore pour fichier LFS
- **Justification** : .gitignore bloquait fichier `etablissements_enrichis_final_*.csv`
- **Solution** : Ajout ligne `!data/processed/etablissements_enrichis_final_20260513.csv`

**Décision 4** : URL Streamlit Cloud publique
- **Justification** : Dashboard destiné à usage CCI/CA/collectivités (accès libre)
- **URL** : `dashboard-commercial-nord59.streamlit.app`

### 🚧 Blocages rencontrés

**Problème 1** : Fichier 55 MB manquant sur Streamlit Cloud (Option 1)
- **Cause** : Fichier dans .gitignore, pas sur GitHub
- **Solution** : Passage à Git LFS pour héberger gros fichier

**Problème 2** : Variables config.py manquantes
- **Cause** : Nouveau config.py chemins relatifs incomplet vs ancien
- **Solution** : Ajout 13 variables (couleurs profils, priorités, fichiers)

**Problème 3** : Git LFS bloqué par .gitignore
- **Cause** : Règle `etablissements_enrichis_final_*.csv` ignorait fichier
- **Solution** : Exception `!etablissements_enrichis_final_20260513.csv`

**Problème 4** : Tests multiples déploiement
- **Cause** : Itérations Option 1 → Option 2 avec corrections progressives
- **Solution** : Process validé et documenté pour futurs gros fichiers

### 📊 Métriques

**Story points terminés** : 13/13 (100%)

**Déploiement** :
- Tentatives : 2 (Option 1 puis Option 2)
- Durée totale : 6 heures
- Upload LFS : 58 MB en ~25 secondes
- Redéploiement Streamlit : 3-5 minutes

**Dashboard production** :
- URL publique : ✅ Opérationnelle
- Pages fonctionnelles : 9/9 (100%)
- Performance : < 3 sec chargement/page
- Disponibilité : 24/7

### 🔄 Git commits

```bash
# Commit 1 : Préparation déploiement
git add requirements.txt src/dashboard/utils/config.py src/dashboard/utils/config_backup.py
git commit -m "feat(deploy): prepare Streamlit Cloud deployment (requirements + relative paths)"
git push origin main
# Commit ID : a0b40d7

# Commit 2 : Tentative Option 1
git add src/dashboard/utils/config.py
git commit -m "fix(deploy): use 18MB file instead of 55MB for Streamlit Cloud" --no-verify
git push origin main
# Commit ID : 898380a

# Commit 3 : Option 2 Git LFS
git add .gitattributes .gitignore data/processed/etablissements_enrichis_final_20260513.csv src/dashboard/utils/config.py
git commit -m "feat(deploy): add 55MB file with Git LFS for complete historical data" --no-verify
git push origin main
# Commit ID : c311af4
```

### 📝 Notes & Apprentissages

**Note 1** : Git LFS requis pour fichiers > 50 MB
- GitHub limite taille fichiers standards à ~100 MB
- Git LFS héberge sur storage séparé avec pointeurs Git
- Upload initial plus long mais clones futurs optimisés

**Note 2** : Streamlit Cloud télécharge automatiquement fichiers LFS
- Configuration transparente côté Streamlit Cloud
- Aucune config supplémentaire secrets/variables requise
- Temps démarrage rallongé ~30 sec (téléchargement LFS)

**Note 3** : Chemins relatifs Path() essentiels multi-OS
- Chemins absolus Windows (`C:\Users\...`) incompatibles Linux (Streamlit Cloud)
- `Path(__file__).resolve().parent.parent.parent.parent` détecte racine automatiquement
- Opérateur `/` compatible tous OS

**Note 4** : Déploiement continu automatique
- Push GitHub → Détection Streamlit Cloud → Redéploiement auto
- Workflow simplifié pour mises à jour futures
- Aucune intervention manuelle requise

**Note 5** : Limites Git LFS gratuites
- 1 GB stockage total
- 1 GB bande passante/mois
- Dashboard actuel : 58 MB (6% limite stockage)
- À surveiller si ajout futurs gros fichiers

### ⏭️ Prochaine session

**Sprint 7 : Fonctionnalités avancées CA (optionnel)**
- [ ] Export PDF fiches communes automatisées
- [ ] Graphiques personnalisés exportables
- [ ] Benchmarking CA similaires

**Sprint 8 : Finalisation documentation (optionnel)**
- [ ] README complet GitHub avec badges
- [ ] Recommandations CCI/CA chiffrées
- [ ] Vidéo démo 5 minutes
- [ ] Slides présentation projet

**Maintenance dashboard**
- [ ] Monitoring usage Streamlit Cloud
- [ ] Actualisation données SIRENE (trimestrielle)
- [ ] Collecte feedbacks utilisateurs CCI/CA

---

---

## 📅 Session du 15 mai 2026 (Suite)

### ⏱️ Durée : 4 heures (Sprint 7 - Phases 1 & 2)

### 🎯 Sprint actuel : Sprint 7 — Fonctionnalités avancées CA

### ✅ Tâches réalisées

#### US-060 : Export PDF fiches communes (8 SP)
- [x] Installation ReportLab 4.5.0 dans environnement .venv
- [x] Migration environnement Spyder → VSCode (détection .venv automatique)
- [x] Création fonction generate_commune_pdf()
- [x] Template PDF professionnel 3 sections (Identité, KPI, Classification)
- [x] Mise en forme avec code couleur catégories priorités
- [x] Test génération PDF commune Priorité A
- [x] Validation cas d'usage VP CA

#### US-061 : Export CSV données filtrées (3 SP)
- [x] Création fonction export_filtered_data()
- [x] 5 types filtres : EPCI, catégorie, profil, score min/max
- [x] Format UTF-8 with BOM (compatible Excel)
- [x] Génération fichiers metadata automatiques
- [x] 4 tests scénarios : EPCI, prioritaires, profil+score, complet
- [x] Validation exports (95, 203, 31, 647 communes)

### 📁 Fichiers créés/modifiés

**Sprint 7** :
- `notebooks/07_sprint7_fonctionnalites_avancees_ca.ipynb`
- Fonction `generate_commune_pdf()` (template PDF)
- Fonction `export_filtered_data()` (exports filtrés)
- `outputs/fiche_*.pdf` (tests PDF)
- `outputs/export_test*.csv` (4 tests CSV + metadata)

### 💬 Décisions prises

**Décision 1** : Environnement VSCode au lieu de Spyder
- **Justification** : VSCode détecte automatiquement .venv pour notebooks
- **Résultat** : Import ReportLab fonctionnel, meilleure intégration Git

**Décision 2** : Arrêt Sprint 7 après US-060 et US-061
- **Justification** : PDF et CSV = fonctionnalités les plus utiles CA
- **US reportées** : US-062 (graphiques personnalisés), US-063 (benchmarking)
- **Résultat** : Priorité documentation finale (Sprint 8)

**Décision 3** : Template PDF minimaliste mais professionnel
- **Justification** : 3 sections essentielles sans surcharge visuelle
- **Résultat** : Fiche 2-3 pages, générée en < 10 secondes

### 🚧 Blocages rencontrés

**Problème 1** : ReportLab non accessible depuis Spyder
- **Cause** : Spyder utilise son propre interpréteur Python (pas le .venv)
- **Solution** : Migration VSCode avec détection .venv automatique

### 📊 Métriques

**Story points terminés** : 11/13 (85% Sprint 7)

**Sprint 7 partiel** :
- ✅ US-060 : PDF (8 SP)
- ✅ US-061 : CSV (3 SP)
- ⏸️ US-062 : Graphiques (5 SP) — Reporté
- ⏸️ US-063 : Benchmarking (8 SP) — Reporté

**Tests réalisés** :
- 1 test PDF (commune Priorité A)
- 4 tests CSV (EPCI, prioritaires, profil+score, complet)

### 🔄 Git commits

```bash
# Commit Sprint 7 (à faire)
git add notebooks/07_sprint7_fonctionnalites_avancees_ca.ipynb outputs/
git commit -m "feat(sprint7): add PDF export and advanced CSV filtering (US-060, US-061)"
git push origin main
```

### 📝 Notes & Apprentissages

**Note 1** : ReportLab 4.5.0 très complet pour PDF professionnels
- Tableaux avec styles (couleurs, bordures, alignement)
- Support texte formaté (Paragraph avec HTML-like)
- Mise en page structurée (SimpleDocTemplate)

**Note 2** : UTF-8 with BOM essentiel pour Excel
- Encodage standard UTF-8 ne s'ouvre pas correctement dans Excel
- UTF-8-sig (with BOM) = compatible Excel Windows

**Note 3** : Métadonnées exports = transparence
- Fichiers _metadata.txt avec date, filtres, stats
- Traçabilité exports pour audits

**Note 4** : US-062 et US-063 moins prioritaires
- Graphiques personnalisés = niche use case
- Benchmarking CA = nécessite données complémentaires externes
- Documentation finale (Sprint 8) plus importante pour projet

### ⏭️ Prochaine session

**Sprint 8 : Finalisation & Documentation**
- [ ] Mise à jour PRODUCT_BACKLOG.md (Sprint 7 partiel)
- [ ] Mise à jour README.md (section fonctionnalités)
- [ ] Rédaction recommandations CCI (3)
- [ ] Rédaction recommandations CA (3)
- [ ] Préparation présentation projet (optionnel)

---
