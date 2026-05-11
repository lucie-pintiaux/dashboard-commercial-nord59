# 📋 MÉTADONNÉES — Dataset Enrichi avec Données INSEE

**Fichier** : `etablissements_enrichis_20260511.csv`  
**Date création** : 11/05/2026 20:17:44  
**Sprint** : Sprint 2 — Nettoyage & Enrichissement  
**User Story** : US-011  

---

## 📊 CARACTÉRISTIQUES DU DATASET

| Métrique | Valeur |
|----------|--------|
| **Lignes** | 98,369 |
| **Colonnes** | 20 |
| **Taille fichier** | 17.99 Mo |
| **Établissements actifs** | 39,261 (39.91%) |
| **Établissements fermés** | 59,108 (60.09%) |
| **Communes couvertes** | 647 |

---

## 🧹 TRANSFORMATIONS APPLIQUÉES

### 1. Dataset de base
- **Source** : `etablissements_nettoyes_20260511.csv`
- **Lignes** : 98 369 établissements
- **Colonnes** : 13 (après nettoyage Sprint 2.1)

### 2. Enrichissement INSEE (3 sources)
- **Population communale** : Recensement 2021
- **Emploi/Chômage** : Base CC 2021 (15-64 ans)
- **Revenus** : FiLoSoFi 2021 (revenus déclarés)

### 3. Jointures effectuées
- **Type** : Left join sur `code_commune`
- **Clé** : Code commune INSEE (5 chiffres)
- **Résultat** : 7 nouvelles colonnes ajoutées

---

## 📋 COLONNES DU DATASET (20 colonnes)

### Identification (5)
1. `siret` — Identifiant unique établissement
2. `code_commune` — Code INSEE commune
3. `code_postal` — Code postal
4. `nom_commune` — Nom commune (SIRENE)
5. `nom_commune_insee` — Nom commune (INSEE, source officielle)

### Activité (2)
6. `code_activite` — Code NAF (47xx)
7. `etat_etablissement` — Actif (A) ou Fermé (F)

### Temporalité (5)
8. `date_creation` — Date création établissement
9. `annee_creation` — Année extraction
10. `date_fermeture` — Date fermeture (si fermé)
11. `annee_fermeture` — Année extraction
12. `date_dernier_traitement` — Date MAJ SIRENE

### Géolocalisation (2)
13. `coordonnee_lambert_x` — Lambert 93 X
14. `coordonnee_lambert_y` — Lambert 93 Y

### Données INSEE communales (6)
15. `population` — Population municipale 2021
16. `taux_chomage` — Taux chômage 15-64 ans (%)
17. `nb_chomeurs_15_64` — Nombre chômeurs
18. `nb_actifs_15_64` — Nombre actifs
19. `revenu_median` — Revenu médian déclaré (€)
20. `taux_pauvrete` — Taux pauvreté à 60% (%)

---

## ⚠️ VALEURS MANQUANTES ET SECRET STATISTIQUE

| Colonne | % Complétude | Commentaire |
|---------|--------------|-------------|
| **Colonnes établissement (13)** | | |
| `siret` à `annee_creation` | 99-100% | ✅ Excellente complétude |
| `coordonnee_lambert_x/y` | 86.59% | ⚠️ 13% non géolocalisés |
| **Colonnes INSEE (6)** | | |
| `population` | 99.99% | ✅ Quasi-complète (1 commune manquante) |
| `taux_chomage` | 100.00% | ✅ Complète |
| `nb_chomeurs_15_64` | 100.00% | ✅ Complète |
| `nb_actifs_15_64` | 100.00% | ✅ Complète |
| `revenu_median` | 90.29% | ⚠️ Secret statistique (petites communes) |
| `taux_pauvrete` | 0.00% | ❌ Fichier pauvreté : toutes valeurs masquées |

### Secret statistique INSEE
L'INSEE applique le **secret statistique** aux communes de petite taille (< 50 ménages) ou présentant des risques d'identification. Cela explique :
- **9,71% de revenus médians manquants** (9 555 établissements dans petites communes)
- **100% de taux pauvreté manquants** (fichier PAUVRES inadapté, remplacer par fichier DISP)

---

## 🎯 QUALITÉ DU DATASET

✅ **Excellent** :
- Identification : 100% complète
- Données INSEE emploi : 100% complète
- Population : 99,99% complète

⚠️ **Bon** :
- Revenus : 90% complète (secret statistique attendu)
- Géolocalisation : 87% complète

❌ **À corriger** :
- Taux pauvreté : 0% (mauvais fichier source)

**Recommandation** : Recharger `FILO2021_DISP_COM.csv` au lieu de `FILO2021_DEC_PAUVRES_COM.csv` pour obtenir les taux de pauvreté.

---

## 📂 FICHIERS SOURCES

### Dataset établissements
- **Fichier** : `etablissements_nettoyes_20260511.csv`
- **Source** : SIRENE StockEtablissement (filtré Nord 59 + NAF 47xx)
- **Date extraction** : 07/05/2026

### Données INSEE
- **Population** : `ensemble/donnees_communes.csv` (Recensement 2021)
- **Emploi** : `base-cc-emploi-pop-active-2021.CSV` (154 Mo)
- **Revenus** : `FILO2021_DEC_PAUVRES_COM.csv` (⚠️ à remplacer)

---

## ⏭️ PROCHAINES ÉTAPES

1. **Correction taux pauvreté** : Recharger avec `FILO2021_DISP_COM.csv`
2. **US-012** : Enrichissement hiérarchie NAF (libellés secteurs)
3. **US-013** : Création dictionnaire de données complet
4. **US-014** : Création fichier EPCI/CA

---

**📅 Document créé le** : 11/05/2026 à 20:17:44  
**✍️ Auteur** : Lucie Pintiaux  
**📊 Sprint** : Sprint 2 — Nettoyage & Enrichissement  
**🔗 Repository** : `dashboard-commercial-nord59`
