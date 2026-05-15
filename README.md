# 📊 Dashboard Commercial Nord 59

Dashboard interactif d'analyse de la dynamique commerciale du département du Nord (59) à partir des données SIRENE.

![Version](https://img.shields.io/badge/version-0.5.0-blue)
![Python](https://img.shields.io/badge/python-3.11+-green)
![Streamlit](https://img.shields.io/badge/streamlit-1.31+-red)
![License](https://img.shields.io/badge/license-MIT-yellow)

---

## 🎯 Objectif

Fournir un outil d'analyse accessible aux acteurs du développement économique (CCI, collectivités, CA) pour :
- Visualiser la dynamique commerciale des 647 communes du Nord
- Identifier les zones prioritaires d'intervention
- Analyser l'impact COVID sur le commerce local
- Cibler les aides à l'installation

---

## ✨ Fonctionnalités

### 9 pages interactives

1. **📈 Évolution 2015-2024** : Tendances créations/fermetures avec dates historiques
2. **🦠 Rupture COVID** : Analyse impact pandémie (avant/pendant/après)
3. **🗺️ Tendances Commune** : Carte GPS interactive 642 communes
4. **📉 Types commerces déclin** : Secteurs NAF les plus vulnérables
5. **🏘️ Focus Commune** : Analyse détaillée par commune (recherche 647)
6. **🤝 EPCI** : Comparaison intercommunale (17 territoires)
7. **🏪 Commerces manquants** : Besoins non couverts (203 communes)
8. **📊 Tableaux de bord** : KPI multi-dimensions pour pilotage
9. **📋 Données détaillées** : Exports CSV et données brutes

### Visualisations

- 🗺️ **3 cartes GPS interactives** (Plotly Mapbox)
- 📊 **25+ graphiques** (line plots, bar charts, pie charts)
- 🔍 **15+ filtres dynamiques** (profil, EPCI, secteur, catégorie)
- 💾 **Exports CSV** (communes, établissements, secteurs, commerces manquants)

---

## 🚀 Installation

### Prérequis

- Python 3.11+
- pip

### Étapes

```bash
# Cloner le repository
git clone https://github.com/votre-username/dashboard-commercial-nord59.git
cd dashboard-commercial-nord59

# Créer environnement virtuel
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

# Installer dépendances
pip install -r requirements.txt
```

---

## 📊 Utilisation

### Lancer le dashboard

```bash
cd src/dashboard
python -m streamlit run app.py
```

Le dashboard s'ouvre automatiquement dans votre navigateur à l'adresse : `http://localhost:8501`

### Naviguer

- Utilisez le **menu latéral** pour accéder aux 9 pages
- **Filtres dynamiques** : profil, EPCI, secteur NAF, catégorie priorité
- **Cartes interactives** : zoom, pan, hover pour détails
- **Exports CSV** : Page 9 pour téléchargements

---

## 📂 Structure du projet

dashboard-commercial-nord59/<br>
├── data/<br>
│   ├── raw/                    # Données brutes SIRENE<br>
│   └── processed/              # Données enrichies (GPS, scores)<br>
├── src/<br>
│   └── dashboard/<br>
│       ├── pages/              # 9 pages Streamlit<br>
│       ├── utils/              # config.py, data_loader.py<br>
│       └── app.py              # Homepage navigation<br>
├── docs/                       # Documentation<br>
├── ROADMAP_ET_JOURNAL_DE_BORD.md<br>
├── PRODUCT_BACKLOG.md<br>
└── README.md<br>
---

## 📈 Données

### Sources

- **SIRENE** : Base établissements INSEE (stock 2024)
- **INSEE** : Population, chômage, revenus communaux
- **Traitement** : Enrichissement GPS (Lambert 93 → WGS84), scoring, clustering

### Périmètre

- **Département** : Nord (59)
- **Secteur** : Commerce (NAF 47xx)
- **Communes** : 647 (642 avec GPS - 99,2%)
- **Établissements** : 98 369 analysés

### Mises à jour

- Snapshot SIRENE : 2024
- Dates fermetures historiques : 2015-2024 enrichies
- Coordonnées GPS : Converties mai 2026

---

## 🛠️ Technologies

- **Frontend** : Streamlit 1.31+
- **Visualisation** : Plotly 5.18+
- **Data** : Pandas 2.1+, NumPy 1.26+
- **Geo** : Pyproj 3.6+ (conversion coordonnées)
- **Python** : 3.11+

---

## 📊 Métriques Dashboard

- **9 pages** fonctionnelles
- **25+ graphiques** interactifs
- **3 cartes GPS** (Plotly Mapbox)
- **642 communes** géolocalisées (99,2%)
- **98 369 établissements** analysés
- **Performance** : < 3 sec chargement/page

---

## 🎯 Personas cibles

- **CCI** : Analyse territoriale, secteurs vulnérables
- **Communautés d'Agglomération** : Pilotage intercommunal, benchmarking
- **Élus municipaux** : Diagnostic commune, comparaison département
- **Créateurs d'entreprise** : Choix implantation, besoins non couverts

---

## 🚀 Déploiement (À venir - Sprint 6)

Déploiement prévu sur **Streamlit Cloud** :
- URL publique accessible 24/7
- Mise à jour automatique depuis GitHub
- Accès gratuit consultation

---

## 📝 Licence

Ce projet est sous licence **MIT**.

Les données SIRENE sont sous **Licence Ouverte** (INSEE).

---

## 👤 Auteur

**Lucie Pintiaux**  
Projet M2 - Dashboard Commercial Nord 59  
📅 Mai 2026

---

## 🤝 Contribution

Les contributions sont les bienvenues ! Consultez [CONTRIBUTING.md](CONTRIBUTING.md) pour les guidelines.

---

## 📞 Contact

- GitHub : [@votre-username](https://github.com/votre-username)
- Email : votre.email@example.com

---

**⭐ Star ce projet si vous le trouvez utile !**
