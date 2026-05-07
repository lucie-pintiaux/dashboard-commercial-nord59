# 📋 METADATA — Dataset SIRENE Nord 59

## Source
- **Producteur** : INSEE / data.gouv.fr
- **URL source** : https://object.files.data.gouv.fr/data-pipeline-open/siren/stock/StockEtablissement_utf8.zip
- **URL stable** : https://www.data.gouv.fr/api/1/datasets/r/0651fb76-bcf3-4f6a-a38d-bc04fa708576
- **Date mise à jour source** : 01/05/2026
- **Date extraction** : 07/05/2026 15:56

## Périmètre
- **Département** : Nord (59) — code commune commençant par 59
- **Secteur** : Commerce de détail (NAF 47xx)
- **Filtre** : codeCommuneEtablissement LIKE '59%' AND activitePrincipaleEtablissement LIKE '47%'

## Fichier produit
- **Nom** : sirene_nord59_20260507.csv
- **Taille** : 22.3 Mo
- **Checksum MD5** : 746d682394d895ea9de2908bb3583e57
- **Encodage** : UTF-8

## Statistiques
- **Total établissements** : 98,369
- **Établissements actifs (A)** : 39,261
- **Établissements fermés (F)** : 59,108
- **Communes couvertes** : 647
- **Colonnes** : 54

## Reproduction
```bash
# Télécharger le fichier source
wget https://object.files.data.gouv.fr/data-pipeline-open/siren/stock/StockEtablissement_utf8.zip

# Filtrer (voir notebook 01_sprint1_collecte_sirene.ipynb)
# DEP=59 : codeCommuneEtablissement LIKE '59%'
# NAF=47 : activitePrincipaleEtablissement LIKE '47%'
```

## Notes
- Le fichier source complet contient ~43 millions d'établissements (France entière)
- Le dataset filtré représente 0.23% du total national
- Certains établissements anciens ont des dates manquantes (nettoyage Sprint 2)
