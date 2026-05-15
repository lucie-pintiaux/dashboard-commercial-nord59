"""
Fonctions de chargement des données
"""

import config
import pandas as pd
import streamlit as st


@st.cache_data
def load_communes_avec_gps():
    """Charge communes avec coordonnées GPS"""
    try:
        df = pd.read_csv(config.COMMUNES_FILE, sep=",", encoding="utf-8")
        return df
    except Exception as e:
        st.error(f"Erreur chargement communes GPS: {e}")
        return None


@st.cache_data
def load_communes_categorisees():
    """Charge communes catégorisées (fallback sans GPS)"""
    try:
        df = pd.read_csv(config.COMMUNES_FILE, sep=",", encoding="utf-8")
        return df
    except Exception as e:
        st.error(f"Erreur chargement communes: {e}")
        return None


@st.cache_data
def load_commerces_manquants():
    """Charge commerces manquants par commune"""
    try:
        df = pd.read_csv(config.COMMERCES_MANQUANTS_FILE, sep=",", encoding="utf-8")
        return df
    except Exception as e:
        st.error(f"Erreur chargement commerces manquants: {e}")
        return None


@st.cache_data
def load_secteurs_vulnerables():
    """Charge secteurs NAF vulnérables"""
    try:
        df = pd.read_csv(config.SECTEURS_VULNERABLES_FILE, sep=",", encoding="utf-8")
        return df
    except Exception as e:
        st.error(f"Erreur chargement secteurs vulnérables: {e}")
        return None


@st.cache_data
def load_etablissements(nrows=None):
    """Charge établissements enrichis avec GPS"""
    try:
        df = pd.read_csv(
            config.ETABLISSEMENTS_FILE, sep=",", encoding="utf-8", nrows=nrows
        )
        return df
    except Exception as e:
        st.error(f"Erreur chargement établissements: {e}")
        return None


def get_kpis_globaux(df_communes):
    """Calcule KPI globaux"""
    return {
        "nb_communes": len(df_communes),
        "nb_actifs": int(df_communes["nb_actifs"].sum()),
        "taux_mortalite_moyen": df_communes["taux_mortalite"].mean(),
        "nb_prioritaires": len(
            df_communes[
                df_communes["categorie_priorite"].isin(["Priorité A", "Priorité B"])
            ]
        ),
    }


@st.cache_data
def load_evolution_temporelle(df_etablissements):
    """Calcule évolution temporelle 2015-2024"""

    # Créations par année
    creations = (
        df_etablissements[df_etablissements["annee_creation"].between(2015, 2024)]
        .groupby("annee_creation")
        .size()
    )

    # Fermetures par année
    fermetures = (
        df_etablissements[df_etablissements["annee_fermeture"].between(2015, 2024)]
        .groupby("annee_fermeture")
        .size()
    )

    # Créer DataFrame avec toutes les années
    annees = range(2015, 2025)
    df_evolution = pd.DataFrame({"annee": annees})

    df_evolution["nb_creations"] = (
        df_evolution["annee"].map(creations).fillna(0).astype(int)
    )
    df_evolution["nb_fermetures"] = (
        df_evolution["annee"].map(fermetures).fillna(0).astype(int)
    )
    df_evolution["solde_net"] = (
        df_evolution["nb_creations"] - df_evolution["nb_fermetures"]
    )

    return df_evolution
