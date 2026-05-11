---

## 🚦 Installation

### Prérequis
- Python 3.11+ installé
- Git installé
- 4 Go RAM minimum (chargement datasets)

### 1. Cloner le repository
```bash
git clone https://github.com/ton-username/dashboard-commercial-nord59.git
cd dashboard-commercial-nord59
```

### 2. Créer l'environnement virtuel
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux/Mac
source .venv/bin/activate
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 4. Configurer les variables d'environnement
```bash
cp .env.example .env
# Éditer .env selon vos besoins
```

### 5. Lancer le dashboard (Sprint 5+)
```bash
streamlit run src/dashboard/app.py
```

---

## 📊 Utilisation

### Notebooks d'exploration (Sprint 0-4)
```bash
jupyter notebook notebooks/
```

**Notebooks disponibles** :
- `00_sprint0_setup.ipynb` — Vérification environnement
- `01_sprint1_collecte_sirene.ipynb` — Collecte données SIRENE
- `02_sprint2_nettoyage_enrichissement.ipynb` — Nettoyage + enrichissement INSEE/NAF
- `03_sprint3_exploration.ipynb` — (À venir) KPI et visualisations
- `04_sprint4_analyses_avancees.ipynb` — (À venir) Scoring et clustering

### Dashboard web (Sprint 5+)
```bash
streamlit run src/dashboard/app.py
```
Interface accessible sur `http://localhost:8501`

---

## 👥 Personas Utilisateurs

### Primaires (MVP Sprint 5)
1. **Sophie Marchand** — Chargée de mission CCI
   - Besoin : Analyses territoriales rapides, identification communes prioritaires
   
2. **Claire Deschamps** — Vice-Présidente CA
   - Besoin : Arbitrage budgétaire 800k€, comparaison EPCI
   
3. **Fatima Benali** — Élue municipale
   - Besoin : Diagnostic communal, comparaison avec communes similaires

### Secondaires (Sprint 7)
4. **Jean-Pierre Leclercq** — Directeur CCI (vision stratégique)
5. **Julien Vasseur** — DGS CA (évaluation politiques publiques)
6. **Isabelle Vanderhaegen** — Directrice acquisitions immobilier

---

## 📈 Avancement du Projet

### Métriques globales
| Métrique | Valeur |
|----------|--------|
| **Sprints complétés** | 2 / 8 (25%) |
| **Story points complétés** | 32 / 110 (29%) |
| **User Stories terminées** | 7 / 44 (16%) |
| **Vélocité moyenne** | 16 SP/sprint |

### Sprint en cours : Sprint 2 (fin) — US-013, US-014
**Objectif** : Dictionnaire de données + Fichier EPCI  
**Progression** : 18/23 SP (78%)

### Prochains jalons
- **Fin Mai 2026** : Sprint 3 — Exploration & KPI
- **Début Juin 2026** : Sprint 4 — Scoring & clustering
- **Mi-Juin 2026** : Sprint 5 — Dashboard MVP déployé
- **Fin Juin 2026** : Sprints 6-8 — Finalisation & recommandations

---

## 🤝 Contribution

Les contributions sont les bienvenues ! Merci de lire [CONTRIBUTING.md](CONTRIBUTING.md) avant de proposer une pull request.

### Quick start contributeurs
1. Fork le projet
2. Créer une branche feature (`git checkout -b feature/AmazingFeature`)
3. Commit les changements (`git commit -m 'feat: Add AmazingFeature'`)
4. Push sur la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

### Conventions
- **Commits** : Format conventionnel (`feat:`, `fix:`, `docs:`, `refactor:`)
- **Code** : PEP 8, type hints, docstrings Google style
- **Tests** : Coverage > 80%

---

## 📜 Licence

Ce projet est sous licence MIT. Voir [LICENSE](LICENSE) pour plus de détails.

---

## 📞 Contact & Ressources

### Auteur
**Lucie Pintiaux** — Analyste Data & Product Owner  
📧 Email : [l.pintiaux@gmail.com]  
💼 LinkedIn : [www.linkedin.com/in/lucie-pintiaux]  

### Liens utiles
- 📊 [Données SIRENE](https://www.data.gouv.fr/fr/datasets/base-sirene-des-entreprises-et-de-leurs-etablissements-siren-siret/)
- 📈 [INSEE — Recensement](https://www.insee.fr/fr/statistiques)
- 🏪 [Nomenclature NAF](https://www.insee.fr/fr/information/2406147)
- 🏛️ [Action Cœur de Ville](https://agence-cohesion-territoires.gouv.fr/action-coeur-de-ville-42)

---

## 🙏 Remerciements

- **INSEE** pour les données SIRENE et les référentiels
- **Data.gouv.fr** pour la mise à disposition des données publiques
- **Communauté Streamlit** pour le framework
- **CCI Hauts-de-France** pour l'inspiration du projet

---

**⭐ Si ce projet vous est utile, n'hésitez pas à lui donner une étoile sur GitHub !**

---

**Dernière mise à jour** : 11/05/2026  
**Version** : 0.2.0 (Sprint 2 complété)