# 🗺️ Dashboard Commercial Nord 59

![Python](https://img.shields.io/badge/Python-3.14-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.57-red)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-En%20développement-orange)

> Dashboard web interactif d'analyse de la dynamique commerciale du département du Nord (59)  
> Données SIRENE — Open Source — Déployé sur Streamlit Cloud

---

## 🎯 Objectif

Les acteurs du développement économique (CCI, collectivités, communautés d'agglomération)
manquent d'outils accessibles pour analyser la dynamique commerciale territoriale.

Ce dashboard permet de **visualiser, analyser et comparer** la situation commerciale
des 648 communes du Nord à partir des données publiques SIRENE.

**Gain de temps** : 3h de compilation Excel → 5 minutes d'analyse

---

## ✨ Fonctionnalités

- 🗺️ **Carte choroplèthe** interactive — vacance commerciale par commune
- 🏘️ **Focus Commune** — diagnostic détaillé + comparaison départementale  
- 🤝 **Analyse EPCI/CA** — comparaison intercommunale
- 📊 **Analyse Sectorielle** — filtrage par type de commerce (NAF)
- 🏆 **Score de fragilité** — classement objectif 0-100
- 📄 **Export PDF** — fiches diagnostics automatisées

---

## 🚀 Installation

```bash
# Cloner le repo
git clone https://github.com/lucie-pintiaux/dashboard-commercial-nord59.git
cd dashboard-commercial-nord59

# Créer et activer le virtualenv
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac

# Installer les dépendances
pip install -r requirements.txt

# Configurer les variables d'environnement
copy .env.example .env
```

---

## 📊 Données sources

| Source | Contenu | MAJ |
|--------|---------|-----|
| [SIRENE INSEE](https://www.data.gouv.fr/fr/datasets/base-sirene-des-entreprises-et-de-leurs-etablissements-siren-siret/) | Établissements commerciaux | Mensuelle |
| [INSEE FiLoSoFi](https://www.insee.fr/fr/statistiques/7233950) | Revenus ménages | Annuelle |
| [INSEE Populations](https://www.insee.fr/fr/statistiques/7739582) | Population communale | Annuelle |
| [IGN AdminExpress](https://geoservices.ign.fr/adminexpress) | Contours communes | Trimestrielle |

---

## 🗂️ Structure du projet
dashboard-commercial-nord59/
├── data/
│   ├── raw/          # Données brutes SIRENE
│   ├── processed/    # Données nettoyées et enrichies
│   └── external/     # Données tierces (INSEE, IGN)
├── notebooks/        # Jupyter notebooks par sprint
├── src/
│   ├── dashboard/    # Application Streamlit (5 pages)
│   ├── data/         # Scripts collecte et nettoyage
│   ├── models/       # Scoring et clustering
│   └── utils/        # Fonctions utilitaires
└── tests/            # Tests unitaires et intégration
---

## 👥 Personas cibles

- **Sophie** — Chargée de mission CCI (analyse territoriale)
- **Claire** — Vice-Présidente CA (arbitrage budgétaire)
- **Fatima** — Élue municipale (diagnostic commune)

---

## 🛠️ Stack technique

| Outil | Usage |
|-------|-------|
| Python 3.14 | Langage principal |
| Pandas | Manipulation données |
| Streamlit | Dashboard web |
| Plotly | Visualisations interactives |
| Scikit-learn | Scoring + clustering |
| GeoPandas | Cartographie |

---

## 📅 Roadmap

| Sprint | Objectif | Statut |
|--------|----------|--------|
| Sprint 0 | Setup environnement | 🟡 En cours |
| Sprint 1 | Collecte données SIRENE | ⏳ À venir |
| Sprint 2 | Nettoyage & enrichissement | ⏳ À venir |
| Sprint 3 | Exploration & KPI | ⏳ À venir |
| Sprint 4 | Analyses avancées & scoring | ⏳ À venir |
| Sprint 5 | Dashboard MVP | ⏳ À venir |
| Sprint 6 | Déploiement | ⏳ À venir |
| Sprint 7 | Fonctionnalités avancées | ⏳ À venir |
| Sprint 8 | Finalisation | ⏳ À venir |

---

## 🤝 Contribution

Voir [CONTRIBUTING.md](CONTRIBUTING.md) pour les guidelines.

---

## 📄 Licence

MIT — Voir [LICENSE](LICENSE)

---

**✍️ Auteur** : Lucie Pintiaux | **Démarrage** : 08/05/2026
