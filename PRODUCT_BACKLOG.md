# 📋 PRODUCT BACKLOG — Dashboard Commercial Nord 59

**Gestion Scrum — Priorisation MoSCoW**

---

## 📊 VUE D'ENSEMBLE

| Métrique | Valeur |
|----------|--------|
| **Total User Stories** | 44 |
| **Must Have** | 24 |
| **Should Have** | 15 |
| **Could Have** | 5 |
| **Total Story Points** | 139 SP |
| **Story Points complétés** | 84 SP (60%) |

---

## 🎯 LÉGENDE PRIORITÉS

- 🔴 **MUST** — Indispensable pour le MVP, bloquant
- 🟠 **SHOULD** — Important, apporte forte valeur ajoutée
- 🟡 **COULD** — Nice to have, si temps disponible
- ⚫ **WON'T** — Hors périmètre actuel, reporté V2

**Estimation** : Fibonacci (1, 2, 3, 5, 8, 13, 21)

---

## 📊 RÉCAPITULATIF STORY POINTS

| Sprint | Objectif | Story Points | Vélocité cumulée | Status |
|--------|----------|--------------|------------------|--------|
| Sprint 0 | Setup | — | — | ✅ Complété |
| Sprint 1 | Collecte | 9 | 9 | ✅ Complété (113%) |
| Sprint 2 | Nettoyage | 23 | 32 | ✅ Complété (177%) |
| Sprint 3 | Exploration | 18 | 50 | ✅ Complété (138%) |
| Sprint 4 | Analyses | 34 | 84 | ✅ Complété (162%) |
| Sprint 5 | Dashboard MVP | 21 | 105 | 🔜 À venir |
| Sprint 6 | Déploiement | 13 | 118 | 📅 Planifié |
| Sprint 7 | Avancées CA | 13 | 131 | 📅 Planifié |
| Sprint 8 | Finalisation | 8 | 139 | 📅 Planifié |

**Total** : 139 story points sur 8 semaines  
**Complété** : 84 / 139 SP (60%)  
**Vélocité moyenne** : 21 SP/sprint

---

## ✅ SPRINTS COMPLÉTÉS

### Sprint 0 — Initialisation ✅
- Setup environnement Python + Git + VSCode
- Structure projet professionnelle
- README initial avec badges

### Sprint 1 — Collecte données SIRENE ✅ (9 SP)
- **US-002** : Téléchargement fichier SIRENE StockEtablissement
- **US-003** : Filtrage Nord 59 + NAF 47xx (~100k établissements)
- **US-004** : Documentation source et métadonnées

**Livrable** : `sirene_nord59_20260508.csv` (100 Mo)

---

### Sprint 2 — Nettoyage & Enrichissement ✅ (23 SP)
- **US-010** : Nettoyage valeurs manquantes et doublons
- **US-011** : Enrichissement données INSEE (population, chômage, revenus)
- **US-012** : Enrichissement hiérarchie NAF complète
- **US-013** : Création dictionnaire de données
- **US-014** : Création fichier codes EPCI/CA

**Livrables** : 
- `etablissements_enrichis_final_20260512.csv` (98 369 lignes)
- `dictionnaire_donnees_20260512.csv`
- `epci_communes_20260512.csv`

---

### Sprint 3 — Exploration & KPI ✅ (18 SP)
- **US-020** : Calcul indicateurs de base par commune (647 communes)
- **US-021** : Carte choroplètre vacance commerciale
- **US-022** : Analyse évolution créations/fermetures 2015-2024

**Livrables** :
- `communes_kpi_20260512.csv` (647 × 13 colonnes)
- `carte_mortalite_commerciale_20260512.html`
- `evolution_creations_fermetures_20260512.png`

**Découvertes** :
- Taux mortalité moyen : 57,07%
- Pic COVID 2020 : +14,7% créations
- Déclin post-COVID : solde -79%

---

### Sprint 4 — Analyses avancées & Scoring ✅ (34 SP)
- **US-030** : Score de fragilité composite (0-100) — 8 SP
- **US-031** : Clustering K-Means (4 profils) — 8 SP
- **US-032** : Catégorisation priorités (A/B/Non) — 3 SP
- **US-033** : Commerces manquants — 5 SP
- **US-034** : Secteurs vulnérables — 5 SP
- **US-035** : Corrélations socio-économiques — 5 SP

**Livrables** :
- `communes_scored_20260512.csv` (647 × 17 colonnes, 88 Ko)
- `communes_clustered_20260512.csv` (647 × 19 colonnes, 98 Ko)
- `communes_categorisees_20260512.csv` (647 × 20 colonnes, 107 Ko)
- `commerces_manquants_20260512.csv` (203 × 7 colonnes, 26 Ko)
- `secteurs_vulnerables_20260512.csv` (39 × 5 colonnes, 4 Ko)

**Découvertes** :
- 4 profils : Dynamique (41%), Précaire (20%), Métropole (0,3%), Désertifié (39%)
- 203 communes prioritaires (31% du territoire)
- 105 déserts commerciaux totaux (7/7 commerces manquants)
- Chômage = prédicteur principal (r = 0.848 avec score)
- Mortalité faiblement corrélée chômage (r = 0.126)

---
### 📦 Sprint 5 — Dashboard MVP (Semaine 5) ✅ TERMINÉ

**Objectif** : Créer dashboard fonctionnel avec 9 pages

**User Stories terminées** :

✅ **US-040** | Créer architecture dashboard Streamlit
- Configuration centralisée (config.py)
- Data loader avec cache (data_loader.py)
- Homepage navigation (app.py)
- **Résultat** : 3 modules utils fonctionnels

✅ **US-041** | Page 1 : Vue d'ensemble (Évolution 2015-2024)
- KPI globaux + graphiques temporels
- Annotation COVID, analyse 3 périodes
- **Résultat** : Page fonctionnelle, dates historiques validées

✅ **US-042** | Page 2 : Rupture COVID 2020-2021
- Comparaison 3 périodes (avant/pendant/après)
- Bar charts, timeline, 3 onglets analyse
- **Résultat** : Page complète avec analyses détaillées

✅ **US-043** | Page 3 : Tendances par commune (Carte GPS)
- Conversion Lambert 93 → WGS84 (642 communes)
- Carte scatter mapbox interactive
- Filtres, classements, répartition profils
- **Résultat** : Carte GPS fonctionnelle, 99,2% communes géolocalisées

✅ **US-044** | Page 4 : Types commerces en déclin
- Top 10 secteurs NAF vulnérables
- Tableau détaillé, distribution fragilité
- **Résultat** : 39 secteurs analysés, taux fermeture moyens

✅ **US-045** | Page 5 : Focus Commune
- Recherche parmi 647 communes
- KPI détaillés, comparaison département
- Évolution temporelle, commerces manquants
- **Résultat** : Analyse détaillée toute commune

✅ **US-046** | Page 6 : EPCI / Intercommunalités
- Filtrage par EPCI, comparaison 17 territoires
- Classement communes EPCI, carte conditionnelle
- **Résultat** : Vision territoriale intercommunale

✅ **US-047** | Page 7 : Commerces manquants
- Identification 203 communes avec besoins
- Top 10 types manquants, carte GPS
- **Résultat** : 1 155 commerces manquants identifiés

✅ **US-048** | Page 8 : Tableaux de bord
- KPI multi-dimensions (5 catégories)
- Synthèse globale, top/flop communes
- **Résultat** : Dashboard pilotage décideurs

✅ **US-049** | Page 9 : Données détaillées
- Exports CSV 4 datasets
- Statistiques, structure, documentation
- **Résultat** : Transparence et réutilisabilité données

**Livrables** :
- ✅ 9 pages Streamlit fonctionnelles
- ✅ 3 cartes GPS interactives
- ✅ 25+ graphiques Plotly
- ✅ Exports CSV opérationnels
- ✅ Dashboard testable en local

**Critères d'acceptation** :
- [x] Dashboard lance localement sans erreur
- [x] Navigation fluide entre pages
- [x] Filtres fonctionnels (EPCI, secteur NAF, profil, catégorie)
- [x] Temps chargement < 3 secondes
- [x] Cartes GPS avec 642 communes
- [x] Exports CSV fonctionnels

**Durée réalisée** : 21 story points (1 session intensive - 13 mai 2026)

**Statut** : ✅ **TERMINÉ À 100%** (9/9 pages validées)

---

### 📦 Sprint 6 — Déploiement & Sécurité (Semaine 6) ✅ TERMINÉ

**Objectif** : Déployer en production avec sécurité et Git LFS

**User Stories terminées** :

✅ **US-050** | Déployer sur Streamlit Cloud
- Création compte Streamlit Cloud
- Connexion repository GitHub
- Configuration déploiement (repository, branch, main file path)
- URL publique obtenue : `dashboard-commercial-nord59.streamlit.app`
- **Résultat** : Dashboard accessible 24/7

✅ **US-051** | Configurer secrets et variables d'environnement
- Fichier requirements.txt créé (10 dépendances)
- Config.py adapté chemins relatifs (Path())
- Aucun secret sensible dans code (pas besoin .streamlit/secrets.toml)
- **Résultat** : Configuration production sécurisée

✅ **US-052** | Implémenter cache données (amélioration performances)
- Cache Streamlit @st.cache_data déjà implémenté (Sprint 5)
- Validation performance < 3 sec/page
- **Résultat** : Performance optimale maintenue

✅ **US-053** | Configuration Git LFS pour fichiers volumineux
- Installation Git LFS version 3.7.1
- Initialisation Git LFS dans repository
- Tracking fichier 55 MB (.gitattributes)
- Modification .gitignore (exception fichier LFS)
- Upload 58 MB via GitHub LFS (2,3 MB/s)
- **Résultat** : Dashboard 100% fonctionnel avec données historiques complètes

**Livrables** :
- ✅ requirements.txt (10 dépendances Python)
- ✅ config.py (chemins relatifs + 13 variables)
- ✅ .gitattributes (configuration Git LFS)
- ✅ .gitignore (exception fichier 55 MB)
- ✅ Fichier 55 MB uploadé GitHub LFS
- ✅ Dashboard déployé Streamlit Cloud
- ✅ URL publique accessible

**Critères d'acceptation** :
- [x] URL publique fonctionnelle 24/7
- [x] Secrets non exposés dans le code
- [x] Temps réponse < 3 secondes par page
- [x] 9/9 pages fonctionnelles (100%)
- [x] Données historiques complètes 2015-2024
- [x] Redéploiement automatique sur push GitHub

**Durée réalisée** : 13 story points (1 session intensive - 15 mai 2026)

**Statut** : ✅ **TERMINÉ À 100%** (Git LFS Option 2 validée)

**Notes techniques** :
- Git LFS requis pour fichier > 50 MB (GitHub limite standard)
- Option 1 (18 MB) testée mais abandonnée (Pages 1-2 non fonctionnelles)
- Option 2 (55 MB Git LFS) solution finale pour analyses temporelles complètes
- Limite GitHub LFS gratuite : 1 GB stockage + 1 GB bande passante/mois

---

## 🔜 SPRINTS À VENIR

---

### Sprint 7 — Fonctionnalités avancées CA (13 SP)
**Objectif** : Fonctionnalités spécifiques Communautés d'Agglomération

**User Stories** :
- 🟠 **US-060** : Fiche diagnostic PDF automatisée par commune (8 SP)
- 🟠 **US-061** : Export CSV données filtrées par EPCI (3 SP)
- 🟠 **US-062** : Graphique évolution personnalisé (5 SP)
- 🟠 **US-063** : Benchmarking entre CA similaires (8 SP)

---

### Sprint 8 — Finalisation & Recommandations (8 SP)
**Objectif** : Documentation finale et livrables actionnables

**User Stories** :
- 🟡 **US-070** : Rédiger 3 recommandations CCI (3 SP)
- 🟡 **US-071** : Rédiger 3 recommandations CA (3 SP)
- 🟡 **US-072** : Finaliser README complet (2 SP)
- 🟡 **US-073** : Créer vidéo démo (5 min) (5 SP)
- 🟡 **US-074** : Préparer slides présentation (3 SP)

---

## ⛔ USER STORIES HORS PÉRIMÈTRE (Won't Have)

**US-036** : Mesurer impact plan commerce CA (avant/après) — 8 SP  
**Raison** : Nécessite données externes plan commerce (non disponibles)

**US-WH-01** : Données nationales (toute la France)  
**Raison** : Périmètre limité au Nord 59

**US-WH-02** : Données en temps réel  
**Raison** : Analyse sur stock, pas de flux temps réel

**US-WH-03** : Prévisions futures (ML)  
**Raison** : Analyse descriptive uniquement, pas prédictive

**US-WH-04** : Chiffre d'affaires commerces  
**Raison** : Donnée non disponible dans SIRENE public

**US-WH-05** : Intégration SI CA  
**Raison** : Livrable = dashboard standalone

**US-WH-06** : Application mobile native  
**Raison** : Dashboard web responsive suffisant

---

## 📊 SYNTHÈSE PAR PRIORITÉ

| Priorité | Nb US | Story Points | Complétés | Restants |
|----------|-------|--------------|-----------|----------|
| 🔴 MUST | 24 | 76 SP | 58 SP | 18 SP |
| 🟠 SHOULD | 15 | 52 SP | 26 SP | 26 SP |
| 🟡 COULD | 5 | 11 SP | 0 SP | 11 SP |
| **Total** | **44** | **139 SP** | **84 SP** | **55 SP** |

---

**📅 Document créé le** : 12/05/2026  
**✍️ Auteur** : Lucie Pintiaux  
**📊 Version** : 1.1  
**🔗 Repository** : `dashboard-commercial-nord59`
