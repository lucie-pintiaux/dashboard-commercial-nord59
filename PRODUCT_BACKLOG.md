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

## 🔜 SPRINTS À VENIR

### Sprint 5 — Dashboard MVP (21 SP)
**Objectif** : Créer dashboard fonctionnel avec 5 pages

**User Stories** :
- 🔴 **US-040** : Architecture dashboard Streamlit (5 SP)
- 🔴 **US-041** : Page 1 Vue d'ensemble (KPI globaux + carte) (8 SP)
- 🔴 **US-042** : Page 2 Focus Commune (détail + comparaison) (8 SP)
- 🔴 **US-043** : Page 3 Analyse EPCI/CA (8 SP)
- 🔴 **US-044** : Page 4 Analyse Sectorielle (8 SP)
- 🔴 **US-045** : Page 5 Documentation (5 SP)
- 🟠 **US-046** : Tests fonctionnels dashboard (5 SP)

**Critères d'acceptation** :
- Dashboard lance localement sans erreur
- Navigation fluide entre 5 pages
- Filtres fonctionnels (EPCI, secteur NAF)
- Temps chargement < 3 secondes

---

### Sprint 6 — Déploiement & Sécurité (13 SP)
**Objectif** : Déployer en production avec sécurité

**User Stories** :
- 🔴 **US-050** : Déployer sur Streamlit Cloud (3 SP)
- 🔴 **US-051** : Sécuriser secrets et variables environnement (2 SP)
- 🟠 **US-052** : Optimiser performances (cache & lazy loading) (5 SP)
- 🟠 **US-053** : Configurer logging et monitoring (3 SP)
- 🟠 **US-054** : Créer CI/CD GitHub Actions (5 SP)
- 🟠 **US-055** : Tests sécurité (OWASP) (3 SP)

**Critères d'acceptation** :
- URL publique fonctionnelle 24/7
- Secrets non exposés dans le code
- Temps réponse < 5 secondes

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