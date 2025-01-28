import streamlit as st
import pandas as pd

from utils import restaurants_data as rd
from utils.sidebar import create_sidebar, create_filtros_restaurants
from utils import geral_data as gd # aqui ta importando o arquivo

def main(): # cria a função

    st.set_page_config(page_title="RESTAURANTES", page_icon="🛎️", layout="wide")

    df = gd.read_processed_data()

    countries = create_sidebar(df) #chama a função

    top_n = create_filtros_restaurants(df) #chama a função

    st.markdown("# VISÃO RESTAURANTES") 

    figura_restaurante = rd.restaurante_avalia(df, countries, top_n)

    st.plotly_chart(figura_restaurante, use_container_width=True)

    fig = rd.restaurante_entrega_online(df)

    st.plotly_chart(fig, use_container_width=True)

    cols1, cols2 = st.columns(2)
    with cols1:

        fig = rd.restaurante_aceitam_reservas(df)

        st.plotly_chart(fig, use_container_width=True)
    
    with cols2:

        fig = rd.restaurante_faz_entregas(df)

        st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__": # se o arquivo principal "Home.py" é igual ao arquivo atual "Geral.py"
    main() 



