import streamlit as st
import pandas as pd
import folium # para fazer mapa

from folium.plugins import MarkerCluster # para juntar os pontos do folium
from streamlit_folium import folium_static # para utilizar o folium no streamlit

from utils.sidebar import create_sidebar # aqui ta importando só a função
from utils import geral_data as gd # aqui ta importando o arquivo

def create_map(df):
    f = folium.Figure(width=1920, height=1080) # tamanho do mapa
    mapa = folium.Map(max_bounds=True).add_to(f)
    marker_cluster = MarkerCluster().add_to(mapa) # agrupamento do cluster
    for _, line in df.iterrows(): #iterrows recebe index e line, o comando underline quer dizer que nao recebe o index
        name = line["restaurant_name"]
        price_for_two = line["average_cost_for_two"]
        cuisine = line["cuisines"]
        currency = line["currency"]
        rating = line["aggregate_rating"]
        color = f'{line["color_name"]}'

        html = "<p><strong>{}</strong></p>"
        html += "<p>Price: ({}) {},00  para dois"
        html += "<br />Type: {}"
        html += "<br />Aggregate Rating: {}/5.0"
        html = html.format(name, currency, price_for_two, cuisine, rating)

        popup = folium.Popup(
            folium.Html(html, script=True),
            max_width=500,
        )

        folium.Marker(
            [line["latitude"], line["longitude"]],
            popup=popup,
            icon=folium.Icon(color=color, icon="home", prefix="fa"),
        ).add_to(marker_cluster)

    folium_static(mapa, width=1024, height=768) # função com parametros do mapa

def main(): # criar funcao para melhor organização!

    st.set_page_config(page_title="VISÃO GERAL", page_icon="⚙️", layout="wide")
    
    df = gd.read_processed_data()

    selected_countries = create_sidebar(df) # é uma variavel do retorno do create_sidebar 

    st.markdown("# FOME ZERO")   

    st.markdown("## O melhor restaurante")

    st.markdown("### Temos as seguintes marcas dentro da nossa plataforma:")

    restaurants, countries, cities, ratings, cuisines = st.columns(5)

    restaurants.metric(label = "Restaurante Cadastrado",
                    value = f"{gd.qtd_restaurant(df):,}".replace(",", ".")
    )

    countries.metric(label = "Países Cadastrados",
                 value = gd.qtd_countries(df)
                 )

    cities.metric(label = "Cidades Cadastradas",
              value = gd.qtd_cities(df)
              )

    ratings.metric(label = "Avaliações Realizadas",
               value = f"{gd.qtd_ratings(df):,}".replace(",",".")
               )
    cuisines.metric(label = "Culinárias Cadastradas",
                value =  gd.qtd_cuisines(df)
                )

    map_df = df.loc[df["country"].isin(selected_countries), :] # isin filtra os paises selecionados

    create_map(map_df) # primeiro aparece as metricas acima no streamlit e depois aparece o mapa!


if __name__ == "__main__": # se o arquivo principal "Home.py" é igual ao arquivo atual "Geral.py"
    main()