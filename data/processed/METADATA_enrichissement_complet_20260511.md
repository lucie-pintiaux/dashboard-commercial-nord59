# 📋 MÉTADONNÉES — Dataset Complet Enrichi (INSEE + NAF)

**Fichier** : `etablissements_enrichis_complet_20260511.csv`  
**Date création** : 11/05/2026 20:39:41  
**Sprint** : Sprint 2 — Nettoyage & Enrichissement  
**User Stories** : US-010, US-011, US-012  

---

## 📊 CARACTÉRISTIQUES DU DATASET

| Métrique | Valeur |
|----------|--------|
| **Lignes** | 98,369 |
| **Colonnes** | 30 |
| **Taille fichier** | 49.45 Mo |
| **Établissements actifs** | 39,261 (39.91%) |
| **Établissements fermés** | 59,108 (60.09%) |
| **Communes couvertes** | 647 |
| **Codes NAF uniques** | 60 |

---

## 🧹 TRANSFORMATIONS APPLIQUÉES

### Sprint 2.1 — Nettoyage (US-010)
- Source : SIRENE StockEtablissement brut (98 369 établissements)
- Nettoyage valeurs manquantes et doublons
- Création colonnes temporelles (date_fermeture, annee_creation, annee_fermeture)
- Réduction : 54 → 13 colonnes (-76%)

### Sprint 2.2 — Enrichissement INSEE (US-011)
- 3 sources INSEE : Population 2021, Emploi/Chômage 2021, Revenus 2021
- 6 colonnes ajoutées : population, taux_chomage, nb_chomeurs, nb_actifs, revenu_median, taux_pauvrete
- Complétude : 99,99% population, 100% chômage, 90% revenus

### Sprint 2.3 — Enrichissement NAF (US-012)
- Référentiel NAF révision 2 (1 728 codes)
- 11 colonnes ajoutées : hiérarchie NAF complète (section, division, groupe, classe, sous-classe + libellés)
- Traitement codes anciens (47.01-47.10) avec mapping manuel
- **Complétude : 100%** (98 369 / 98 369 établissements)

---

## 📋 STRUCTURE DU DATASET (30 COLONNES)

### Identification (5)
1. `siret` — Identifiant unique établissement
2. `code_commune` — Code INSEE commune (5 chiffres)
3. `code_postal` — Code postal
4. `nom_commune` — Nom commune (source SIRENE)
5. `nom_commune_insee` — Nom commune (source INSEE officielle)

### Activité NAF (11)
6. `code_activite` — Code NAF révision 2 (ex: 47.11B, 47.59A)
7. `naf_section` — Section (G = Commerce)
8. `naf_division` — Division (47 = Commerce de détail)
9. `naf_groupe` — Groupe (47.1, 47.2, etc.)
10. `naf_classe` — Classe (47.11, 47.59, etc.)
11. `naf_libelle` — Libellé complet de l'activité
12. `naf_section_libelle` — Libellé section
13. `naf_division_libelle` — Libellé division
14. `naf_groupe_libelle` — Libellé groupe
15. `naf_classe_libelle` — Libellé classe
16. `naf_sous_classe_libelle` — Libellé sous-classe

### État (1)
17. `etat_etablissement` — A = Actif, F = Fermé

### Temporalité (5)
18. `date_creation` — Date création établissement
19. `annee_creation` — Année création
20. `date_fermeture` — Date fermeture (si fermé)
21. `annee_fermeture` — Année fermeture
22. `date_dernier_traitement` — Date dernière MAJ SIRENE

### Géolocalisation (2)
23. `coordonnee_lambert_x` — Coordonnée Lambert 93 X
24. `coordonnee_lambert_y` — Coordonnée Lambert 93 Y

### Données communales INSEE (6)
25. `population` — Population municipale 2021
26. `taux_chomage` — Taux chômage 15-64 ans (%)
27. `nb_chomeurs_15_64` — Nombre de chômeurs 15-64 ans
28. `nb_actifs_15_64` — Nombre d'actifs 15-64 ans
29. `revenu_median` — Revenu médian déclaré 2021 (€)
30. `taux_pauvrete` — Taux pauvreté à 60% (%)

---

## 📊 COMPLÉTUDE DES DONNÉES

| Catégorie | % Complétude | Commentaire |
|-----------|--------------|-------------|
| **Identification** | 100% | ✅ Excellente |
| **Activité NAF** | 100% | ✅ Complète (codes anciens mappés) |
| **État** | 100% | ✅ Complète |
| **Temporalité** | 99-100% | ✅ Excellente |
| **Géolocalisation** | 86,59% | ⚠️ 13% non géolocalisés |
| **Population INSEE** | 99,99% | ✅ Quasi-complète |
| **Chômage INSEE** | 100% | ✅ Complète |
| **Revenus INSEE** | 90,29% | ⚠️ Secret statistique petites communes |
| **Taux pauvreté** | 0% | ❌ Fichier source inadapté |

---

## 🎯 QUALITÉ GLOBALE

### Excellent ✅
- Identification : 100%
- NAF : 100% (dont 996 codes anciens mappés manuellement)
- Chômage : 100%
- Population : 99,99%

### Bon ⚠️
- Revenus : 90% (secret statistique attendu)
- Géolocalisation : 87%

### À corriger ❌
- Taux pauvreté : 0% (utiliser FILO2021_DISP_COM.csv à la place)

---

## 🔍 CODES NAF ANCIENS TRAITÉS

10 codes NAF anciens (format 47.XX sans suffixe) ont été mappés manuellement :

| Code | Libellé | Nb établissements |
|------|---------|-------------------|
| 47.01 | Commerce de détail en magasin non spécialisé | 238 |
| 47.02 | Commerce de détail alimentaire en magasin spécialisé | 107 |
| 47.03 | Commerce de détail de carburants | 39 |
| 47.04 | Commerce de détail d'équipements IT | 489 |
| 47.05 | Commerce de détail d'équipements du foyer | 36 |
| 47.06 | Commerce de détail de biens culturels | 1 |
| 47.07 | Autres commerces de détail en magasin spécialisé | 5 |
| 47.08 | Commerce de détail sur éventaires et marchés | 24 |
| 47.09 | Commerce de détail hors magasin | 33 |
| 47.10 | Commerce de détail en magasin non spécialisé | 24 |

**Total** : 996 établissements (1,01% du dataset)

---

## 📂 FICHIERS SOURCES

### Dataset établissements
- **Fichier** : SIRENE StockEtablissement
- **Filtres** : Département 59 + NAF 47xx
- **Date extraction** : 07/05/2026

### Données INSEE
- **Population** : Recensement 2021 (647 communes)
- **Emploi** : Base CC 2021 (648 communes)
- **Revenus** : FILO2021_DEC_PAUVRES_COM (648 communes, à remplacer)

### Référentiel NAF
- **Source** : INSEE NAF révision 2
- **Fichier** : int_courts_naf_rev_2.xls
- **Codes** : 1 728 codes (dont 87 codes 47xx + 10 anciens mappés)

---

## ⏭️ PROCHAINES ÉTAPES

**US-013** : Création dictionnaire de données complet  
**US-014** : Création fichier codes EPCI/CA  
**Sprint 3** : Calcul des indicateurs communaux et création des KPI  

---

**📅 Document créé le** : 11/05/2026 à 20:39:41  
**✍️ Auteur** : Lucie Pintiaux  
**📊 Sprint** : Sprint 2 — Nettoyage & Enrichissement  
**🔗 Repository** : `dashboard-commercial-nord59`
