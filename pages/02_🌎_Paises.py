import streamlit as st
import pandas as pd

from utils import countries_data as cd
from utils.sidebar import create_sidebar # aqui ta importando só a função
from utils import geral_data as gd # aqui ta importando o arquivo

def main(): # cria a função

    st.set_page_config(page_title="PAÍSES", page_icon="🌎", layout="wide")
    
    df = gd.read_processed_data()

    selected_countries = create_sidebar(df)

    st.markdown("# VISÃO PAÍSES") 

    figura_restaurante = cd.countries_restaurants(selected_countries, df)

    st.plotly_chart(figura_restaurante, use_container_width=True)

    figura_cidade = cd.countries_cities(selected_countries, df)

    st.plotly_chart(figura_cidade, use_container_width=True)

    cols1, cols2 = st.columns(2)

    with cols1: 

        figura_avaliacao = cd.countries_votes(selected_countries, df)

        st.plotly_chart(figura_avaliacao, use_container_width=True)

    with cols2: 

        figura_prato = cd.countries_average_for_two(selected_countries, df)

        st.plotly_chart(figura_prato, use_container_width=True)

if __name__ == "__main__": # se o arquivo principal "Home.py" é igual ao arquivo atual "Geral.py"
    main() 