import pandas as pd
import streamlit as st

def qtd_restaurant(df):
    return df.shape[0]

def qtd_countries(df):
    return df["country"].nunique() # ->> return df["country"].nunique() ou utilizar ->> df.loc[:, "country"].nunique()

def qtd_cities(df):
    return df["city"].nunique()

def qtd_ratings(df):
    return df["votes"].sum()

def qtd_cuisines(df):
    return df["cuisines"].nunique()


@st.cache_data
def read_processed_data():
    return pd.read_csv("data/processed_data.csv")