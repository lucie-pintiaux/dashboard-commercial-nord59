# 📝 USER STORIES — Dashboard Commercial Nord 59

**Gestion Scrum — Priorisation par Persona et Epic**

---

## 📊 VUE D'ENSEMBLE

| Métrique | Valeur |
|----------|--------|
| **Total User Stories** | 45 |
| **Must Have** | 8 |
| **Should Have** | 24 |
| **Could Have** | 11 |
| **Won't Have** | 2 |
| **Sprints concernés** | Sprint 1 à Sprint 8 |

---

## 🎯 LÉGENDE

### Priorités MoSCoW

- 🔴 **MUST** — Indispensable pour le MVP, bloquant
- 🟠 **SHOULD** — Important, apporte forte valeur ajoutée
- 🟡 **COULD** — Nice to have, si temps disponible
- ⚫ **WON'T** — Hors périmètre actuel, reporté V2

### Personas (références croisées)

- **P1** : Sophie Marchand (Chargée de mission CCI)
- **P2** : Jean-Pierre Leclercq (Directeur CCI)
- **P3** : Claire Deschamps (Vice-Présidente CA)
- **P4** : Fatima Benali (Adjointe au Maire)
- **P5** : Marc Dutilleul (Directeur développement économique)
- **P6** : Julien Vasseur (DGS CA)
- **P7** : Isabelle Vanderhaegen (Directrice acquisitions)
- **P8** : Thomas Hennion (Responsable développement commerce)
- **P9** : Amina Chouaibi (Créatrice d'entreprise)
- **P10** : Kevin Desrumaux (Artisan boulanger)

---

## 🗺️ EPIC 1 — VISUALISATION TERRITORIALE

### Objectif
Permettre aux utilisateurs de voir la situation commerciale sur une carte interactive et d'identifier visuellement les zones prioritaires d'intervention.

---

**US-VIZ-01** | Carte choroplèthe de la vacance commerciale  
**En tant que** chargée de mission CCI (Sophie P1)  
**Je veux** voir le taux de vacance commerciale par commune sur une carte choroplèthe interactive  
**Afin d'** identifier rapidement les zones prioritaires d'intervention et construire un argumentaire solide pour les élus.

**Critères d'acceptation** :
- [ ] Carte affiche les 648 communes du Nord
- [ ] Colormap : vert (faible vacance) → orange → rouge (forte vacance)
- [ ] Tooltip au survol : nom commune, taux vacance, nb actifs, nb fermés
- [ ] Légende avec seuils de catégorisation
- [ ] Temps chargement < 3 secondes

**Priorité** : 🔴 MUST  
**Sprint** : 3  
**Lien Product Backlog** : US-021

---

**US-VIZ-02** | Positionnement relatif de ma commune  
**En tant qu'** élue municipale (Fatima P4)  
**Je veux** voir ma commune positionnée par rapport aux 647 autres communes du Nord  
**Afin d'** évaluer objectivement l'urgence de la situation et construire un plan d'action crédible pour mes administrés.

**Critères d'acceptation** :
- [ ] Selectbox de recherche commune
- [ ] Mise en évidence de la commune sélectionnée sur la carte
- [ ] Tableau comparatif : ma commune vs moyenne département
- [ ] Classement de la commune (rang sur 648)
- [ ] Catégorie de fragilité affichée

**Priorité** : 🔴 MUST  
**Sprint** : 5 (Page Focus Commune)  
**Lien Product Backlog** : US-042

---

**US-VIZ-03** | Carte colorée par niveau d'urgence  
**En tant que** chargée de mission CCI (Sophie P1)  
**Je veux** visualiser la vacance commerciale sur une carte colorée par niveau d'urgence (Priorité A, B, Non prioritaire)  
**Afin de** communiquer visuellement les résultats à des décideurs non-techniciens lors de présentations.

**Critères d'acceptation** :
- [ ] 3 couleurs distinctes pour les 3 catégories
- [ ] Légende explicite avec définition de chaque catégorie
- [ ] Possibilité d'exporter la carte en PNG haute résolution
- [ ] Nombre de communes par catégorie affiché

**Priorité** : 🟠 SHOULD  
**Sprint** : 5  
**Lien Product Backlog** : US-041

---

**US-VIZ-04** | Carte des commerces manquants  
**En tant qu'** élue municipale (Fatima P4)  
**Je veux** voir les commerces essentiels manquants sur ma commune affichés sur une carte  
**Afin de** cibler les aides à l'installation les plus pertinentes pour mon territoire.

**Critères d'acceptation** :
- [ ] Liste commerces essentiels : boulangerie, épicerie, pharmacie, boucherie, poste
- [ ] Carte avec icônes par type de commerce manquant
- [ ] Focus sur les 59 communes prioritaires
- [ ] Export liste en CSV

**Priorité** : 🟠 SHOULD  
**Sprint** : 4  
**Lien Product Backlog** : US-033

---

**US-VIZ-05** | Carte interactive EPCI/CA  
**En tant que** Vice-Présidente CA (Claire P3)  
**Je veux** visualiser mon territoire intercommunal sur une carte dédiée avec les 35 communes de la CA  
**Afin d'** avoir une vue d'ensemble de mon périmètre et identifier les communes les plus fragiles.

**Critères d'acceptation** :
- [ ] Filtre par EPCI (17 EPCI du Nord)
- [ ] Zoom automatique sur le territoire sélectionné
- [ ] Affichage des limites intercommunales
- [ ] KPI agrégés au niveau EPCI

**Priorité** : 🟠 SHOULD  
**Sprint** : 5  
**Lien Product Backlog** : US-043

---

## 📈 EPIC 2 — ANALYSE TEMPORELLE ET DYNAMIQUE

### Objectif
Permettre aux utilisateurs de comprendre l'évolution de la situation commerciale sur la période 2015-2024 et d'identifier les ruptures de tendance (notamment COVID).

---

**US-TEMP-01** | Évolution du taux de fermeture 2015-2024  
**En tant que** directrice acquisitions (Isabelle P7)  
**Je veux** analyser l'évolution du taux de fermeture 2015-2024 par commune  
**Afin de** détecter les tendances et évaluer le risque avant une implantation immobilière.

**Critères d'acceptation** :
- [ ] Graphique line plot : taux fermeture par année
- [ ] Filtre par commune ou groupe de communes
- [ ] Calcul tendance linéaire (régression)
- [ ] Identification communes avec tendance haussière vs baissière
- [ ] Export données temporelles en CSV

**Priorité** : 🟠 SHOULD  
**Sprint** : 3  
**Lien Product Backlog** : US-022

---

**US-TEMP-02** | Rupture de tendance COVID (2020-2021)  
**En tant qu'** analyste immobilier (Isabelle P7)  
**Je veux** identifier les ruptures de tendance avant et après COVID (2020-2021)  
**Afin de** distinguer les fermetures conjoncturelles des fermetures structurelles.

**Critères d'acceptation** :
- [ ] Graphique : avant COVID (2015-2019) vs pendant (2020-2021) vs après (2022-2024)
- [ ] Test statistique de significativité (t-test)
- [ ] % variation fermetures 2020 vs moyenne 2015-2019
- [ ] Identification des 20 communes les plus impactées

**Priorité** : 🟠 SHOULD  
**Sprint** : 3  
**Lien Product Backlog** : US-023

---

**US-TEMP-03** | Communes ayant perdu un commerce récemment  
**En tant qu'** artisan boulanger (Kevin P10)  
**Je veux** voir les communes ayant perdu un commerce de mon type dans les 3 dernières années  
**Afin de** repérer rapidement les opportunités d'implantation disponibles.

**Critères d'acceptation** :
- [ ] Filtre par code NAF ou libellé commerce
- [ ] Filtre par période (1 an, 2 ans, 3 ans)
- [ ] Liste communes avec date fermeture
- [ ] Indication population et revenus pour évaluer viabilité
- [ ] Carte avec marqueurs des opportunités

**Priorité** : 🟠 SHOULD  
**Sprint** : 4  
**Lien Product Backlog** : US-033

---

**US-TEMP-04** | Zones en déclin vs zones en transition  
**En tant que** responsable développement foncier (Thomas P8)  
**Je veux** visualiser l'évolution du tissu commercial par territoire sur 9 ans  
**Afin de** détecter les zones en déclin irréversible vs les zones en transition pour cibler mes prospections.

**Critères d'acceptation** :
- [ ] Classification automatique : déclin / stable / croissance
- [ ] Seuils : déclin si Δ > -15% sur 9 ans
- [ ] Carte avec 3 couleurs selon classification
- [ ] Graphique sparkline évolution par commune
- [ ] Export liste communes en transition

**Priorité** : 🟡 COULD  
**Sprint** : 4  
**Lien Product Backlog** : US-022

---

**US-TEMP-05** | Impact du plan commerce CA (avant/après)  
**En tant que** DGS CA (Julien P6)  
**Je veux** comparer l'évolution des communes bénéficiaires du plan commerce 2021-2024 vs un groupe contrôle  
**Afin d'** évaluer l'impact des 2M€ investis et ajuster la stratégie future.

**Critères d'acceptation** :
- [ ] Sélection communes bénéficiaires (liste prédéfinie)
- [ ] Groupe contrôle : communes similaires non bénéficiaires
- [ ] Graphique avant/après avec lignes de tendance
- [ ] Test statistique (t-test pairé)
- [ ] Rapport synthétique : impact positif / nul / négatif

**Priorité** : 🟠 SHOULD  
**Sprint** : 4  
**Lien Product Backlog** : US-036

---

## 🏪 EPIC 3 — ANALYSE PAR TYPE DE COMMERCE

### Objectif
Permettre aux utilisateurs d'identifier quels types de commerces (codes NAF) sont les plus vulnérables et où se trouvent les manques d'équipement commercial.

---

**US-NAF-01** | Types de commerces fermant en premier  
**En tant que** chargée de mission CCI (Sophie P1)  
**Je veux** identifier quels types de commerces ferment en premier  
**Afin de** cibler les aides à l'installation sur les secteurs les plus fragilisés.

**Critères d'acceptation** :
- [ ] Calcul taux fermeture par naf_classe
- [ ] Graphique bar chart : Top 10 secteurs les plus fragiles
- [ ] Tri décroissant par taux fermeture
- [ ] Analyse croisée : secteur × profil commune
- [ ] Export tableau secteurs vulnérables

**Priorité** : 🟠 SHOULD  
**Sprint** : 4  
**Lien Product Backlog** : US-034

---

**US-NAF-02** | Commerces vulnérables selon profil territoire  
**En tant que** développeur commercial (Thomas P8)  
**Je veux** savoir quels commerces sont les plus vulnérables selon le profil du territoire (urbain, péri-urbain, rural)  
**Afin de** proposer des programmes d'implantation adaptés au tissu économique local.

**Critères d'acceptation** :
- [ ] Segmentation communes : urbain / péri-urbain / rural (critère population)
- [ ] Analyse taux fermeture par secteur NAF × type territoire
- [ ] Tableau croisé avec heatmap
- [ ] Identification secteurs spécifiquement vulnérables en milieu rural
- [ ] Recommandations par profil territoire

**Priorité** : 🟠 SHOULD  
**Sprint** : 4  
**Lien Product Backlog** : US-034

---

**US-NAF-03** | Filtre carte par type de commerce  
**En tant qu'** artisan boulanger (Kevin P10)  
**Je veux** filtrer la carte par type de commerce (boulangeries, épiceries, pharmacies...)  
**Afin de** localiser précisément les communes sous-équipées dans mon secteur d'activité.

**Critères d'acceptation** :
- [ ] Multiselect codes NAF ou libellés
- [ ] Carte mise à jour dynamiquement
- [ ] Nombre d'établissements par commune affiché
- [ ] Couleur : vert (bien équipé) → rouge (sous-équipé / absent)
- [ ] Export liste communes sous-équipées

**Priorité** : 🟠 SHOULD  
**Sprint** : 5  
**Lien Product Backlog** : US-044

---

**US-NAF-04** | Communes sous-équipées en commerce alimentaire  
**En tant que** créatrice d'entreprise (Amina P9)  
**Je veux** identifier les communes sous-équipées en commerce alimentaire avec une population suffisante (> 2 000 habitants)  
**Afin de** choisir le meilleur emplacement pour mon épicerie et maximiser mes chances de succès.

**Critères d'acceptation** :
- [ ] Filtre NAF 47.11 (Supérettes) et 47.29 (Alimentation générale)
- [ ] Filtre population min (slider)
- [ ] Tableau communes : nom, population, nb commerces alimentaires, score opportunité
- [ ] Carte avec marqueurs opportunités
- [ ] Info revenus médians pour estimer pouvoir d'achat

**Priorité** : 🟠 SHOULD  
**Sprint** : 4  
**Lien Product Backlog** : US-033

---

**US-NAF-05** | Top secteurs NAF par commune  
**En tant qu'** élue municipale (Fatima P4)  
**Je veux** voir les 10 principaux secteurs d'activité présents dans ma commune  
**Afin de** comprendre la structure de mon tissu commercial et identifier les spécialisations locales.

**Critères d'acceptation** :
- [ ] Graphique bar chart horizontal
- [ ] Top 10 NAF par nombre d'établissements
- [ ] Comparaison avec moyenne départementale
- [ ] Identification sur/sous-représentation secteurs
- [ ] Export détail en CSV

**Priorité** : 🟠 SHOULD  
**Sprint** : 5  
**Lien Product Backlog** : US-042

---

## 📊 EPIC 4 — CORRÉLATION SOCIO-ÉCONOMIQUE

### Objectif
Permettre aux utilisateurs de comprendre les facteurs explicatifs de la vacance commerciale en croisant avec des données socio-économiques.

---

**US-SOCIO-01** | Corrélation vacance × revenu médian  
**En tant que** directeur développement économique (Marc P5)  
**Je veux** croiser le taux de vacance commerciale avec le revenu médian des communes  
**Afin de** comprendre si les communes les plus pauvres perdent davantage de commerces et justifier des zonages prioritaires.

**Critères d'acceptation** :
- [ ] Scatter plot : taux vacance vs revenu médian
- [ ] Calcul corrélation Pearson avec p-value
- [ ] Ligne de tendance (régression linéaire)
- [ ] Identification outliers (communes atypiques)
- [ ] Interprétation métier de la corrélation

**Priorité** : 🟠 SHOULD  
**Sprint** : 4  
**Lien Product Backlog** : US-035

---

**US-SOCIO-02** | Corrélation vacance × taux de chômage  
**En tant que** directeur développement économique (Marc P5)  
**Je veux** croiser la vacance commerciale avec le taux de chômage communal  
**Afin de** justifier les zones prioritaires pour les demandes de financement État/Région.

**Critères d'acceptation** :
- [ ] Scatter plot : taux vacance vs taux chômage
- [ ] Matrice de corrélation avec heatmap
- [ ] Identification communes avec chômage > 12% ET vacance > 25%
- [ ] Liste communes prioritaires double critère
- [ ] Export pour dossiers financements

**Priorité** : 🟠 SHOULD  
**Sprint** : 4  
**Lien Product Backlog** : US-035

---

**US-SOCIO-03** | Justification plan revitalisation avec données objectives  
**En tant qu'** élue municipale (Fatima P4)  
**Je veux** voir une corrélation entre le niveau de revenu de ma commune et son taux de fermeture  
**Afin de** justifier un plan de revitalisation auprès du Conseil Régional avec des données objectives.

**Critères d'acceptation** :
- [ ] Fiche synthétique commune exportable en PDF
- [ ] Indicateurs clés : revenu, chômage, vacance, population
- [ ] Positionnement vs moyenne département
- [ ] Graphiques comparatifs
- [ ] Argumentaire pré-rédigé pour demande financement

**Priorité** : 🟡 COULD  
**Sprint** : 7  
**Lien Product Backlog** : US-060

---

**US-SOCIO-04** | Impact population sur la dynamique commerciale  
**En tant que** directrice acquisitions (Isabelle P7)  
**Je veux** analyser la corrélation entre la taille de population et la densité commerciale  
**Afin d'** identifier les seuils de viabilité pour mes projets d'implantation.

**Critères d'acceptation** :
- [ ] Scatter plot : population vs densité commerciale (commerces / 1000 hab)
- [ ] Identification seuil critique (ex : < 1 500 hab = fragilité)
- [ ] Segmentation par tranche population
- [ ] Analyse densité optimale par type territoire
- [ ] Recommandations d'implantation par tranche

**Priorité** : 🟡 COULD  
**Sprint** : 4  
**Lien Product Backlog** : US-035

---

## 🎯 EPIC 5 — SEGMENTATION ET SCORING

### Objectif
Permettre aux utilisateurs de classer objectivement les 648 communes selon leur fragilité et d'identifier des typologies de territoires.

---

**US-SEG-01** | Clustering des 648 communes  
**En tant que** directeur développement économique (Marc P5)  
**Je veux** voir les 648 communes segmentées en clusters selon leur dynamique commerciale  
**Afin d'** identifier des typologies de territoires et adapter les politiques d'intervention par profil.

**Critères d'acceptation** :
- [ ] Algorithme K-Means avec 4 clusters
- [ ] Profils nommés : Dynamique, Stable, Fragilisé, En difficulté
- [ ] Carte avec couleurs par cluster
- [ ] Caractéristiques moyennes de chaque cluster
- [ ] Nombre communes par cluster

**Priorité** : 🔴 MUST  
**Sprint** : 4  
**Lien Product Backlog** : US-031

---

**US-SEG-02** | Top 10 communes les plus fragilisées  
**En tant que** chargée de mission CCI (Sophie P1)  
**Je veux** voir le top 10 des communes les plus fragilisées (score > 70)  
**Afin de** prioriser les interventions avec les budgets disponibles.

**Critères d'acceptation** :
- [ ] Tableau : rang, nom commune, score, catégorie, population
- [ ] Tri décroissant par score fragilité
- [ ] Mise en évidence sur la carte
- [ ] Détail des 5 sous-scores pour chaque commune
- [ ] Export liste prioritaire en CSV

**Priorité** : 🟠 SHOULD  
**Sprint** : 4  
**Lien Product Backlog** : US-032

---

**US-SEG-03** | Profil détaillé par territoire  
**En tant que** directrice acquisitions (Isabelle P7)  
**Je veux** voir le profil détaillé de chaque territoire (taux fermeture, revenus, population, tendance)  
**Afin d'** évaluer le potentiel de chaque type de territoire avant investissement.

**Critères d'acceptation** :
- [ ] Fiche territoire avec 12 indicateurs
- [ ] Graphique radar 5 dimensions
- [ ] Évolution temporelle 2015-2024
- [ ] Classement vs communes similaires
- [ ] Recommandation investissement : Go / No Go / Attendre

**Priorité** : 🟡 COULD  
**Sprint** : 5  
**Lien Product Backlog** : US-042

---

**US-SEG-04** | Score de fragilité composite (0-100)  
**En tant que** Vice-Présidente CA (Claire P3)  
**Je veux** disposer d'un score de fragilité objectif et transparent pour chaque commune  
**Afin d'** arbitrer l'allocation budgétaire de manière équitable entre les 35 communes de la CA.

**Critères d'acceptation** :
- [ ] Score = somme de 5 sous-scores (0-20 chacun)
- [ ] Sous-scores : mortalité, solde, densité, chômage, revenu
- [ ] Documentation formules de calcul
- [ ] Validation : corrélation score vs taux mortalité > 0.7
- [ ] Export méthodologie en PDF

**Priorité** : 🔴 MUST  
**Sprint** : 4  
**Lien Product Backlog** : US-030

---

**US-SEG-05** | Catégorisation en niveaux de priorité  
**En tant que** Vice-Présidente CA (Claire P3)  
**Je veux** que les communes soient catégorisées automatiquement en Priorité A, Priorité B, Non prioritaire  
**Afin d'** appliquer des critères transparents pour l'attribution des aides.

**Critères d'acceptation** :
- [ ] Règles métier :
  - Priorité A : Score > 60 ET Chômage > 12%
  - Priorité B : Densité < 10 commerces/1000 hab
  - Non prioritaire : autres
- [ ] ~59 communes prioritaires (A+B)
- [ ] Répartition budgétaire proposée par catégorie
- [ ] Validation en Conseil Communautaire

**Priorité** : 🔴 MUST  
**Sprint** : 4  
**Lien Product Backlog** : US-032

---

## 🖥️ EPIC 6 — DASHBOARD ET INTERFACE

### Objectif
Rendre l'analyse accessible à tous les profils utilisateurs via un dashboard interactif sans compétences techniques requises.

---

**US-DASH-01** | Vue synthétique avec KPI clés  
**En tant que** directeur CCI (Jean-Pierre P2)  
**Je veux** obtenir une vue synthétique avec les indicateurs clés (nb actifs, taux moyen, communes prioritaires)  
**Afin de** présenter rapidement la situation en 2 minutes lors des réunions stratégiques.

**Critères d'acceptation** :
- [ ] 4 KPI cards en haut de page
- [ ] KPI : Total communes, Total actifs, Taux vacance moyen, Communes prioritaires
- [ ] Mise à jour automatique selon filtres appliqués
- [ ] Comparaison vs année précédente (Δ)
- [ ] Temps chargement < 2 secondes

**Priorité** : 🟠 SHOULD  
**Sprint** : 5  
**Lien Product Backlog** : US-041

---

**US-DASH-02** | Filtres par arrondissement et bassin d'emploi  
**En tant que** directeur développement économique (Marc P5)  
**Je veux** filtrer toute l'analyse par arrondissement ou bassin d'emploi  
**Afin d'** adapter les recommandations à chaque territoire et produire des rapports ciblés.

**Critères d'acceptation** :
- [ ] Sidebar avec multiselect arrondissements (6 du Nord)
- [ ] Tous graphiques et cartes réactifs au filtre
- [ ] Sauvegarde filtre dans URL (partage lien)
- [ ] Reset filtre en 1 clic
- [ ] Export données filtrées en CSV

**Priorité** : 🟠 SHOULD  
**Sprint** : 5  
**Lien Product Backlog** : US-043, US-044

---

**US-DASH-03** | Dashboard utilisable sans compétences techniques  
**En tant que** directeur CCI (Jean-Pierre P2)  
**Je veux** utiliser un dashboard interactif sans compétences techniques  
**Afin de** présenter les données directement en réunion sans préparation préalable ni formation.

**Critères d'acceptation** :
- [ ] Interface intuitive (aucun terme technique)
- [ ] Navigation entre pages fluide
- [ ] Tooltips explicatifs sur tous les indicateurs
- [ ] Pas de message d'erreur technique
- [ ] Responsive (tablette et desktop)

**Priorité** : 🟡 COULD  
**Sprint** : 5  
**Lien Product Backlog** : US-040

---

**US-DASH-04** | Documentation sources et limites  
**En tant que** porteur de projet (Kevin P10)  
**Je veux** accéder à un onglet documentation expliquant les sources et les limites  
**Afin de** comprendre la fiabilité des données avant de prendre une décision d'implantation.

**Critères d'acceptation** :
- [ ] Page dédiée "Documentation"
- [ ] Sections : Sources, Périmètre, Méthodologie, Limites, Contact
- [ ] Dates de mise à jour des données
- [ ] Liens vers sources officielles (INSEE, SIRENE)
- [ ] Avertissement : snapshot 2024, délai radiations

**Priorité** : 🟡 COULD  
**Sprint** : 5  
**Lien Product Backlog** : US-045

---

**US-DASH-05** | Interface simplifiée pour entrepreneurs  
**En tant que** créatrice d'entreprise (Amina P9)  
**Je veux** utiliser un outil simple avec une carte et un filtre par type de commerce  
**Afin de** prendre une décision d'implantation sans avoir de compétences en analyse de données.

**Critères d'acceptation** :
- [ ] Page dédiée "Trouver mon emplacement"
- [ ] 2 filtres : type commerce + population min
- [ ] Carte avec résultats sous forme de marqueurs
- [ ] Liste top 10 opportunités
- [ ] Bouton "Contacter la CCI" avec lien email pré-rempli

**Priorité** : 🟠 SHOULD  
**Sprint** : 5  
**Lien Product Backlog** : US-044

---

**US-DASH-06** | Navigation multipage professionnelle  
**En tant que** développeur  
**Je veux** une architecture multipage Streamlit professionnelle  
**Afin de** faciliter la maintenance et l'ajout de nouvelles fonctionnalités.

**Critères d'acceptation** :
- [ ] 5 pages : Vue ensemble, Focus Commune, Analyse EPCI, Analyse Sectorielle, Documentation
- [ ] Menu latéral avec icônes
- [ ] Configuration centralisée (config.py)
- [ ] Cache données avec @st.cache_data
- [ ] Tests intégration navigation

**Priorité** : 🔴 MUST  
**Sprint** : 5  
**Lien Product Backlog** : US-040

---

## 🎁 EPIC 7 — FONCTIONNALITÉS AVANCÉES CA

### Objectif
Fournir des outils spécifiques aux Communautés d'Agglomération pour faciliter leur travail de pilotage et d'évaluation.

---

**US-CA-01** | Export fiche diagnostic PDF par commune  
**En tant que** Vice-Présidente CA (Claire P3)  
**Je veux** exporter automatiquement une fiche diagnostic PDF pour une commune  
**Afin de** répondre rapidement aux demandes des maires lors des réunions intercommunales.

**Critères d'acceptation** :
- [ ] Bouton "Exporter PDF" dans Page Focus Commune
- [ ] Template professionnel avec logo CA
- [ ] Contenu : KPI, graphiques, comparaisons, recommandations
- [ ] Génération < 10 secondes
- [ ] Téléchargement automatique fichier

**Priorité** : 🟠 SHOULD  
**Sprint** : 7  
**Lien Product Backlog** : US-060

---

**US-CA-02** | Export CSV données filtrées par EPCI  
**En tant que** DGS CA (Julien P6)  
**Je veux** exporter en CSV les données de mon EPCI avec tous les indicateurs  
**Afin de** les intégrer dans mes outils de reporting internes et produire des analyses personnalisées.

**Critères d'acceptation** :
- [ ] Bouton "Export CSV" dans Page EPCI
- [ ] Filtre actif appliqué à l'export
- [ ] Toutes colonnes : communes, KPI, scores, catégories
- [ ] Encodage UTF-8 avec BOM (Excel compatible)
- [ ] Nom fichier : export_EPCI_DATE.csv

**Priorité** : 🟠 SHOULD  
**Sprint** : 7  
**Lien Product Backlog** : US-061

---

**US-CA-03** | Graphique évolution personnalisé multi-communes  
**En tant que** DGS CA (Julien P6)  
**Je veux** créer un graphique d'évolution sur mesure comparant plusieurs communes de mon territoire  
**Afin de** l'intégrer dans mes présentations au Conseil Communautaire.

**Critères d'acceptation** :
- [ ] Multiselect communes (max 10)
- [ ] Choix métrique (Nb actifs, Taux mortalité, Score)
- [ ] Slider période (2015-2024)
- [ ] Graphique line plot avec légende
- [ ] Export PNG haute résolution (300 dpi)

**Priorité** : 🟠 SHOULD  
**Sprint** : 7  
**Lien Product Backlog** : US-062

---

**US-CA-04** | Benchmarking entre CA similaires  
**En tant que** DGS CA (Julien P6)  
**Je veux** comparer ma CA avec des territoires similaires (population ±20%, score ±10)  
**Afin d'** identifier les bonnes pratiques et ajuster notre stratégie de développement commercial.

**Critères d'acceptation** :
- [ ] Algorithme de similarité (population, revenus, structure économique)
- [ ] Sélection automatique 3-5 CA comparables
- [ ] Graphique radar 5 dimensions
- [ ] Tableau indicateurs clés comparés
- [ ] Identification points forts / axes amélioration

**Priorité** : 🟠 SHOULD  
**Sprint** : 7  
**Lien Product Backlog** : US-063

---

## 📚 EPIC 8 — RECOMMANDATIONS ET FINALISATION

### Objectif
Transformer l'analyse en livrables actionnables pour les décideurs et finaliser la documentation projet.

---

**US-REC-01** | 3 recommandations chiffrées CCI  
**En tant que** chargée de mission CCI (Sophie P1)  
**Je veux** obtenir 3 recommandations chiffrées et sourcées  
**Afin d'** agir concrètement avec les budgets disponibles et justifier mes choix auprès de ma direction.

**Critères d'acceptation** :
- [ ] Fichier docs/RECOMMENDATIONS_CCI.md
- [ ] 3 recommandations : Constat → Action → Impact attendu
- [ ] Ciblage : communes prioritaires, secteurs vulnérables, aides
- [ ] Chiffrage budgétaire indicatif
- [ ] Sources citées pour chaque recommandation

**Priorité** : 🟡 COULD  
**Sprint** : 8  
**Lien Product Backlog** : US-070

---

**US-REC-02** | 3 recommandations chiffrées CA  
**En tant que** Vice-Présidente CA (Claire P3)  
**Je veux** obtenir 3 recommandations adaptées au contexte intercommunal  
**Afin d'** optimiser l'allocation budgétaire et évaluer l'impact de nos politiques publiques.

**Critères d'acceptation** :
- [ ] Fichier docs/RECOMMENDATIONS_CA.md
- [ ] Focus : allocation budgétaire, évaluation impact, benchmarking
- [ ] Méthodologie d'arbitrage proposée
- [ ] Indicateurs de suivi recommandés
- [ ] Calendrier mise en œuvre proposé

**Priorité** : 🟡 COULD  
**Sprint** : 8  
**Lien Product Backlog** : US-071

---

**US-REC-03** | README complet et professionnel  
**En tant que** directeur CCI (Jean-Pierre P2)  
**Je veux** consulter un README complet documentant la méthodologie  
**Afin de** comprendre les limites de l'analyse et valider les hypothèses avant utilisation.

**Critères d'acceptation** :
- [ ] Sections : About, Features, Installation, Usage, Data, Contributing, License
- [ ] Badges : build status, license, Python version
- [ ] Screenshots dashboard
- [ ] Commandes installation testées
- [ ] Liens vers démo live

**Priorité** : 🟡 COULD  
**Sprint** : 8  
**Lien Product Backlog** : US-072

---

**US-REC-04** | Publication et partage du projet  
**En tant que** chargée de mission CCI (Sophie P1)  
**Je veux** voir le projet publié sur GitHub avec documentation complète  
**Afin de** partager la démarche avec d'autres CCI et collectivités pour essaimage.

**Critères d'acceptation** :
- [ ] Repository GitHub public
- [ ] Dashboard déployé sur Streamlit Cloud
- [ ] Vidéo démo 5 min sur YouTube
- [ ] Article de blog (optionnel)
- [ ] Présentation slides exportable PDF

**Priorité** : 🟡 COULD  
**Sprint** : 8  
**Lien Product Backlog** : US-073, US-074

---

**US-REC-05** | Scalabilité à d'autres territoires  
**En tant que** directeur développement économique (Marc P5)  
**Je veux** voir l'analyse répliquée sur les Hauts-de-France  
**Afin de** valider que la méthodologie est scalable à d'autres territoires.

**Critères d'acceptation** :
- [ ] Documentation : guide réplication autre département
- [ ] Scripts génériques (paramètre DEP)
- [ ] Tests sur département voisin (62 ou 02)
- [ ] Identification points de vigilance
- [ ] Roadmap V2 : extension régionale

**Priorité** : 🟡 COULD  
**Sprint** : 8  
**Lien Product Backlog** : Hors périmètre initial

---

## 🔧 EPIC 9 — INFRASTRUCTURE DATA

### Objectif
Garantir la qualité, la reproductibilité et la performance de la chaîne de traitement des données.

---

**US-DATA-01** | Filtrage SIRENE DEP=59 et NAF=47xx  
**En tant que** data analyste  
**Je veux** filtrer le fichier SIRENE sur le département 59 et les codes NAF 47xx  
**Afin d'** obtenir un dataset gérable sans saturer la mémoire et accélérer les analyses.

**Critères d'acceptation** :
- [ ] Script src/data/filter_sirene.py
- [ ] Filtres : DEP=59 ET NAF LIKE '47%'
- [ ] Dataset filtré : data/raw/sirene_nord59_YYYYMMDD.csv
- [ ] 95 000 - 105 000 établissements
- [ ] Temps exécution < 5 minutes

**Priorité** : 🔴 MUST  
**Sprint** : 1  
**Lien Product Backlog** : US-003

---

**US-DATA-02** | Dataset nettoyé et documenté  
**En tant que** data analyste  
**Je veux** disposer d'un dataset nettoyé avec un dictionnaire de données complet  
**Afin de** garantir la fiabilité de toutes les analyses aval et faciliter la collaboration.

**Critères d'acceptation** :
- [ ] < 1% valeurs manquantes sur colonnes clés
- [ ] 100% codes NAF décodés
- [ ] Fichier data/processed/dictionnaire_donnees.csv
- [ ] Documentation : nom colonne, type, source, description, valeurs possibles
- [ ] Tests unitaires pipeline nettoyage

**Priorité** : 🔴 MUST  
**Sprint** : 2  
**Lien Product Backlog** : US-010, US-013

---

**US-DATA-03** | Enrichissement données communales INSEE  
**En tant que** data analyste  
**Je veux** enrichir le dataset avec population, chômage, revenus par commune  
**Afin d'** analyser les corrélations socio-économiques et contextualiser la vacance commerciale.

**Critères d'acceptation** :
- [ ] Téléchargement automatique FiLoSoFi, recensement, chômage
- [ ] Jointure sur code commune INSEE
- [ ] Colonnes : population_2021, chomage_2022, revenu_median_2021
- [ ] < 5% communes sans données socio-éco
- [ ] Documentation sources et dates

**Priorité** : 🔴 MUST  
**Sprint** : 2  
**Lien Product Backlog** : US-011

---

**US-DATA-04** | Versioning et traçabilité des données  
**En tant que** data analyste  
**Je veux** versionner les datasets avec métadonnées (source, date, checksum)  
**Afin de** garantir la reproductibilité et tracer l'origine de chaque analyse.

**Critères d'acceptation** :
- [ ] Fichier data/raw/METADATA.md
- [ ] Contenu : URL source, date téléchargement, version SIRENE, nb lignes
- [ ] Checksum MD5 pour intégrité
- [ ] Commande reproduction documentée
- [ ] Logs téléchargement et transformation

**Priorité** : 🟠 SHOULD  
**Sprint** : 1  
**Lien Product Backlog** : US-004

---

**US-DATA-05** | Tests de qualité données automatisés  
**En tant que** data analyste  
**Je veux** des tests automatisés sur la qualité des données (Great Expectations ou pytest)  
**Afin de** détecter rapidement les anomalies lors de nouvelles extractions.

**Critères d'acceptation** :
- [ ] Tests : plages valeurs, types colonnes, unicité SIRET
- [ ] Tests : cohérence codes INSEE, NAF, EPCI
- [ ] Intégration CI/CD (GitHub Actions)
- [ ] Rapport qualité HTML automatique
- [ ] Alertes si échec tests

**Priorité** : 🟡 COULD  
**Sprint** : 2  
**Lien Product Backlog** : US-010

---

## ⚫ USER STORIES HORS PÉRIMÈTRE (WON'T HAVE)

### US-WH-01 | Données nationales toute France
**En tant que** analyste CCI  
**Je veux** disposer de données sur toute la France  
**Afin de** comparer le Nord avec d'autres départements

**Raison exclusion** : Périmètre limité au Nord 59 pour MVP. Extension régionale/nationale en V2.

---

### US-WH-02 | Données en temps réel
**En tant que** chargée de mission CCI  
**Je veux** des données actualisées en temps réel  
**Afin de** suivre les fermetures au jour le jour

**Raison exclusion** : Analyse sur stock (snapshot), pas de flux temps réel. Contraintes techniques (API SIRENE) et volumétrie.

---

## 📊 SYNTHÈSE PAR EPIC ET PRIORITÉ

| Epic | Must | Should | Could | Total |
|------|------|--------|-------|-------|
| 1 — Visualisation territoriale | 2 | 3 | 0 | 5 |
| 2 — Analyse temporelle | 0 | 4 | 1 | 5 |
| 3 — Analyse par type commerce | 0 | 4 | 1 | 5 |
| 4 — Corrélation socio-éco | 0 | 2 | 2 | 4 |
| 5 — Segmentation scoring | 4 | 1 | 1 | 6 |
| 6 — Dashboard interface | 1 | 3 | 2 | 6 |
| 7 — Fonctionnalités CA | 0 | 4 | 0 | 4 |
| 8 — Recommandations | 0 | 0 | 5 | 5 |
| 9 — Infrastructure data | 3 | 1 | 1 | 5 |
| **Total** | **10** | **22** | **13** | **45** |

---

## 🗺️ MAPPING PERSONAS × USER STORIES

| Persona | Must | Should | Could | Total US |
|---------|------|--------|-------|----------|
| P1 — Sophie (CCI) | 2 | 5 | 1 | 8 |
| P2 — Jean-Pierre (CCI) | 0 | 1 | 3 | 4 |
| P3 — Claire (CA) | 2 | 3 | 1 | 6 |
| P4 — Fatima (Élue) | 1 | 2 | 1 | 4 |
| P5 — Marc (Dev éco) | 1 | 4 | 0 | 5 |
| P6 — Julien (DGS CA) | 0 | 4 | 0 | 4 |
| P7 — Isabelle (Acquisitions) | 0 | 2 | 2 | 4 |
| P8 — Thomas (Foncier) | 0 | 2 | 0 | 2 |
| P9 — Amina (Créatrice) | 0 | 2 | 0 | 2 |
| P10 — Kevin (Boulanger) | 0 | 2 | 1 | 3 |
| Data analyste | 3 | 1 | 1 | 5 |

---

## 🔄 TRAÇABILITÉ PRODUCT BACKLOG

Toutes les user stories de ce document sont mappées sur les US du Product Backlog (fichier `PRODUCT_BACKLOG.md`). Le lien est indiqué dans chaque US sous la forme :

```
**Lien Product Backlog** : US-XXX
```

---

**📅 Document créé le** : 11/05/2026  
**✍️ Auteur** : Lucie Pintiaux  
**📊 Version** : 1.0  
**🔗 Repository** : `dashboard-commercial-nord59`
