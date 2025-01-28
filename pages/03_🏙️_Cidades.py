import streamlit as st
import pandas as pd

from utils import cities_data as cd
from utils.sidebar import create_sidebar 
from utils import geral_data as gd

def main(): 

    st.set_page_config(page_title="PAÍSES", page_icon="🏙️", layout="wide")
    
    df = gd.read_processed_data()

    selected_countries = create_sidebar(df)

    st.markdown("# VISÃO CIDADES")

    figura_top10 = cd.cities_restaurant_10(selected_countries, df)

    st.plotly_chart(figura_top10, use_container_width=True)

    cols1, cols2 = st.columns(2)

    with cols1: 

        figura_top7_4 = cd.cities_restaurant_4(selected_countries, df)

        st.plotly_chart(figura_top7_4, use_container_width=True)

    with cols2:

        figura_top7_2_5 = cd.cities_restaurant_2_5(selected_countries, df)

        st.plotly_chart(figura_top7_2_5, use_container_width=True)
    
    figura_top10_cuisine = cd.cities_cuisine_10(selected_countries, df)

    st.plotly_chart(figura_top10_cuisine, use_container_width=True)

if __name__ == "__main__":
    main() 