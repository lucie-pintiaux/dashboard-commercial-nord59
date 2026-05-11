# 📋 MÉTADONNÉES — Dataset Nettoyé

**Fichier** : `etablissements_nettoyes_20260511.csv`  
**Date création** : 11/05/2026 15:07:51  
**Sprint** : Sprint 2 — Nettoyage & Enrichissement  
**User Story** : US-010  

---

## 📊 CARACTÉRISTIQUES DU DATASET

| Métrique | Valeur |
|----------|--------|
| **Lignes** | 98,369 |
| **Colonnes** | 13 |
| **Taille fichier** | 12.06 Mo |
| **Période couverte** | 1900 - 2026 |
| **Établissements actifs** | 39,261 (39.91%) |
| **Établissements fermés** | 59,108 (60.09%) |

---

## 🧹 TRANSFORMATIONS APPLIQUÉES

### 1. Sélection des colonnes
- **Colonnes initiales** : 54
- **Colonnes retenues** : 10
- **Colonnes créées** : 3 (date_fermeture, annee_fermeture, annee_creation)
- **Total final** : 13 colonnes

### 2. Colonnes conservées
1. `siret` — Identifiant unique établissement
2. `code_commune` — Code INSEE commune (59xxx)
3. `code_postal` — Code postal
4. `nom_commune` — Nom de la commune
5. `code_activite` — Code NAF (47xx)
6. `etat_etablissement` — Actif (A) ou Fermé (F)
7. `date_creation` — Date de création établissement
8. `date_dernier_traitement` — Date MAJ SIRENE
9. `coordonnee_lambert_x` — Coordonnée Lambert X
10. `coordonnee_lambert_y` — Coordonnée Lambert Y

### 3. Colonnes créées
11. `date_fermeture` — Date fermeture (= date_dernier_traitement si état = F)
12. `annee_fermeture` — Année extraction de date_fermeture
13. `annee_creation` — Année extraction de date_creation

### 4. Traitements effectués
- ✅ Suppression doublons sur SIRET : **0 doublons détectés**
- ✅ Renommage colonnes (snake_case)
- ✅ Création colonnes temporelles
- ✅ Vérification intégrité données

---

## ⚠️ VALEURS MANQUANTES

| Colonne | % NaN | Commentaire |
|---------|-------|-------------|
| `siret` | 0.00% | ✅ Complet |
| `code_commune` | 0.00% | ✅ Complet |
| `code_postal` | 0.00% | ✅ Complet |
| `nom_commune` | 0.00% | ✅ Complet |
| `code_activite` | 0.00% | ✅ Complet |
| `etat_etablissement` | 0.00% | ✅ Complet |
| `date_creation` | 0.98% | ⚠️ Info non disponible SIRENE |
| `date_dernier_traitement` | 0.00% | ✅ Complet |
| `coordonnee_lambert_x` | 13.41% | ⚠️ Adresses non géolocalisées |
| `coordonnee_lambert_y` | 13.41% | ⚠️ Adresses non géolocalisées |
| `date_fermeture` | 39.91% | ✅ Normal (= établissements actifs) |
| `annee_fermeture` | 39.91% | ✅ Normal (= établissements actifs) |
| `annee_creation` | 0.98% | ⚠️ Lié à date_creation |

---

## 🎯 QUALITÉ DU DATASET

✅ **Colonnes critiques** : 100% complètes (SIRET, commune, NAF, état)  
✅ **Unicité** : Tous les SIRET sont uniques  
⚠️ **Coordonnées GPS** : 13% manquantes (géocodage alternatif possible)  
✅ **Dates** : < 1% manquantes sur création  

**Conclusion** : Dataset exploitable pour analyses territoriales et temporelles.

---

## 📂 FICHIERS SOURCES

- **Fichier brut** : `sirene_nord59_20260507.csv` (98 369 lignes × 54 colonnes)
- **Source** : SIRENE StockEtablissement INSEE
- **Date extraction** : 07/05/2026
- **Filtres appliqués** : DEP=59 + NAF=47xx

---

## ⏭️ PROCHAINES ÉTAPES

1. **US-011** : Enrichissement données INSEE (population, chômage, revenus)
2. **US-012** : Enrichissement hiérarchie NAF (libellés secteurs)
3. **US-013** : Création dictionnaire de données
4. **US-014** : Création fichier EPCI/CA

---

**📅 Document créé le** : 11/05/2026 à 15:07:51  
**✍️ Auteur** : Lucie Pintiaux  
**🔗 Repository** : `dashboard-commercial-nord59`
