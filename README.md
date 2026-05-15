# 🏪 Dashboard Commercial Nord 59

**Analyse dynamique commerciale du département du Nord à partir des données SIRENE**

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.32+-red.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Dashboard](https://img.shields.io/badge/Dashboard-Live-success.svg)](https://dashboard-commercial-nord59.streamlit.app)

---

## 🎯 À propos

### Problème

Les acteurs du développement économique du Nord (CCI, collectivités, communautés d'agglomération) manquent d'outils accessibles pour analyser la dynamique commerciale territoriale et prendre des décisions éclairées.

### Solution

Dashboard web interactif, open-source et actualisable permettant de **visualiser, analyser et comparer** la situation commerciale des **647 communes** du département du Nord à partir des données SIRENE 2024.

### Valeur ajoutée

- ⏱️ **Gain de temps** : Analyses automatisées vs compilation manuelle Excel (3h → 5 min)
- 🌐 **Accessibilité** : Interface simple sans compétences techniques requises
- 📊 **Transparence** : Méthodologie documentée et données publiques
- 🎯 **Impact territorial** : Aide à la décision pour 203 communes prioritaires identifiées

---

## ✨ Fonctionnalités

### 📊 9 pages d'analyse interactive

1. **Évolution 2015-2024** — Tendances créations/fermetures sur 10 ans
2. **Rupture COVID** — Impact 2020-2021 et analyse comparative
3. **Tendances par commune** — Carte GPS interactive 647 communes
4. **Types commerces en déclin** — Top secteurs NAF vulnérables
5. **Focus Commune** — Diagnostic détaillé avec comparaison département
6. **EPCI / Intercommunalités** — Vision territoriale 17 EPCI
7. **Commerces manquants** — Identification 203 communes avec besoins
8. **Tableaux de bord** — KPI synthétiques multi-dimensions
9. **Données détaillées** — Exports CSV et documentation méthodologie

### 🛠️ Outils avancés

- 📄 **Export PDF** : Fiches diagnostic automatisées par commune
- 📥 **Export CSV** : Données filtrées par EPCI, catégorie, profil
- 🗺️ **Cartes GPS** : 3 cartes interactives (Plotly Mapbox)
- 📈 **25+ graphiques** : Visualisations Plotly interactives

---

## 🖼️ Aperçu

### Dashboard en production

**🌐 URL** : **[https://dashboard-commercial-nord59.streamlit.app](https://dashboard-commercial-nord59.streamlit.app)**

---

## 📊 Données clés

- **98 369 établissements** analysés (codes NAF 47xx — Commerce de détail)
- **647 communes** du département du Nord (59)
- **10 ans d'historique** (2015-2024)
- **4 profils** identifiés : Dynamique, Désertifié, Précaire, Métropole
- **203 communes prioritaires** nécessitant intervention (Priorité A + B)

### Insights principaux

- 🔴 **Taux mortalité moyen : 57,1%** (59 108 fermés vs 39 261 actifs)
- 📉 **Secteurs en déclin** : Textile (-74,7%), Commerce alimentaire spécialisé (-100%)
- 🏜️ **38,5% communes désertifiées** (249 communes profil Désertifié)
- ⚠️ **13 communes en urgence** (Priorité A : Lille, Roubaix, Maubeuge, Avesnes-sur-Helpe...)

---

## 🚀 Installation et utilisation

### Prérequis

- Python 3.11+
- Git
- Git LFS (pour fichiers > 50 MB)

### Installation locale

```bash
# 1. Cloner le repository
git clone https://github.com/lucie-pintiaux/dashboard-commercial-nord59.git
cd dashboard-commercial-nord59

# 2. Installer Git LFS et télécharger fichiers volumineux
git lfs install
git lfs pull

# 3. Créer environnement virtuel
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux/Mac
source .venv/bin/activate

# 4. Installer dépendances
pip install -r requirements.txt

# 5. Lancer dashboard
cd src/dashboard
streamlit run app.py
```

Le dashboard s'ouvre automatiquement dans votre navigateur à `http://localhost:8501`

---

## 🏗️ Architecture

dashboard-commercial-nord59/<br>
├── data/<br>
│   ├── raw/                    # Données brutes SIRENE<br>
│   └── processed/              # Données nettoyées et enrichies<br>
├── docs/                       # Documentation<br>
├── notebooks/                  # Notebooks Jupyter (8 sprints)<br>
├── outputs/                    # Exports PDF/CSV générés<br>
├── src/<br>
│   └── dashboard/              # Application Streamlit<br>
│       ├── pages/              # 9 pages dashboard<br>
│       ├── utils/              # Modules utilitaires<br>
│       └── app.py              # Point d'entrée<br>
└── tests/                      # Tests unitaires<br>

---

### Stack technique

- **Backend** : Python 3.11, Pandas, Scikit-learn
- **Frontend** : Streamlit 1.32+
- **Visualisation** : Plotly, Plotly Mapbox
- **Géolocalisation** : Pyproj (Lambert 93 → WGS84)
- **Export PDF** : ReportLab 4.5
- **Déploiement** : Streamlit Cloud + Git LFS

---

## 📚 Méthodologie

### Sources de données

- **SIRENE** : Base établissements INSEE (stock mai 2024)
- **INSEE** : Population, revenus, chômage par commune
- **IGN** : Contours administratifs et géolocalisation

### Pipeline de traitement

1. **Collecte** : Téléchargement SIRENE StockEtablissement (98 369 lignes)
2. **Nettoyage** : Filtrage NAF 47xx, gestion valeurs manquantes
3. **Enrichissement** : Données socio-économiques INSEE, hiérarchie NAF
4. **Scoring** : Calcul score fragilité 0-100 (5 composantes)
5. **Clustering** : K-Means 4 profils (Dynamique, Désertifié, Précaire, Métropole)
6. **Catégorisation** : Priorité A / Priorité B / Non prioritaire

### Indicateurs calculés

- **Taux mortalité** : (Nb fermés / Total) × 100
- **Score fragilité** : Composite 5 sous-scores (mortalité, solde, actifs, chômage, revenu)
- **Commerces manquants** : Identification 7 types essentiels (boulangerie, épicerie, pharmacie...)

**📖 Documentation complète** : Voir `Page 9 - Données détaillées` du dashboard

---

## 📋 Recommandations

### Pour les CCI

1. **Programme Transition Commerce** (150 k€/an) : Formation digitalisation secteurs vulnérables
2. **Fonds urgence Priorité A** (200 k€/an) : Aide installation 13 communes critiques
3. **Observatoire Alerte Précoce** (50 k€/an) : Monitoring 249 communes désertifiées

### Pour les CA

1. **Allocation budgétaire différenciée** (650 k€/an) : Grille par profil et catégorie
2. **Protocole évaluation avant-après** : Mesure impact investissements
3. **Commerces mutualisés** (300 k€ pilote) : Mutualisation intercommunale zones rurales

**📄 Détails** : Voir notebook `08_sprint8_documentation_finale.ipynb`

---

## 🤝 Contribution

Les contributions sont les bienvenues ! Merci de :

1. Fork le projet
2. Créer une branche (`git checkout -b feature/amelioration`)
3. Commit vos changements (`git commit -m 'Ajout fonctionnalité X'`)
4. Push vers la branche (`git push origin feature/amelioration`)
5. Ouvrir une Pull Request

### Guidelines

- Respecter PEP 8 (linting avec Black + Flake8)
- Ajouter tests unitaires (coverage > 80%)
- Documenter fonctions (docstrings Google style)

---

## 📜 Licence

Ce projet est sous licence **MIT**. Voir [LICENSE](LICENSE) pour plus de détails.

---

## 📞 Contact

**Lucie Pintiaux**

📧 Email : [l.pintiaux@gmail.com](mailto:l.pintiaux@gmail.com)  
📊 Dashboard : [dashboard-commercial-nord59.streamlit.app](https://dashboard-commercial-nord59.streamlit.app)  
💻 GitHub : [github.com/lucie-pintiaux/dashboard-commercial-nord59](https://github.com/lucie-pintiaux/dashboard-commercial-nord59)

---

## 🙏 Remerciements

- **INSEE** pour données SIRENE et socio-économiques
- **Streamlit** pour plateforme déploiement gratuite
- **Plotly** pour bibliothèque visualisation
- **IGN** pour contours administratifs

---

**📅 Dernière mise à jour** : Mai 2026  
**📊 Version** : 1.0  
**🚀 Statut** : Production (Dashboard en ligne 24/7)

