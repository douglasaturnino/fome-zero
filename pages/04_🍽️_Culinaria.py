import streamlit as st
import pandas as pd

from utils.sidebar import create_sidebar, create_filtros_restaurants, create_filtros_cuisines
from utils.cuisines_data import tabela_cuisines, write_metrics, top_cuisines_melhores, top_cuisines_piores
from utils import geral_data as gd # aqui ta importando o arquivo

def main(): # cria a função

    st.set_page_config(page_title="CULINÁRIAS", page_icon="🍽️", layout="wide")

    df = gd.read_processed_data()

    countries = create_sidebar(df) #chama a função

    restaurants = create_filtros_restaurants(df) #chama a função

    cuisines = create_filtros_cuisines(df) #chama a função

    st.markdown("# VISÃO CULINÁRIA")

    st.markdown(f"## Melhores Restaurantes dos Principais tipos Culinários")

    write_metrics(df)

    st.markdown(f"## Top {restaurants}: Restaurantes ")

    df_restaurants = tabela_cuisines(df, countries, restaurants, cuisines)

    st.dataframe(df_restaurants)

    cols1, cols2 = st.columns(2)
    with cols1:
        fig = top_cuisines_melhores(df, countries, restaurants)
        st.plotly_chart(fig, use_container_width=True)

    with cols2:
        fig = top_cuisines_piores(df, countries, restaurants)
        st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__": # se o arquivo principal "Home.py" é igual ao arquivo atual "Geral.py"
    main() 

