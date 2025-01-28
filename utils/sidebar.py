from PIL import Image
import streamlit as st

def create_sidebar(df):
    image_path = 'imagem/logo.jpg'
    image = Image.open(image_path)

    col1, col2 = st.sidebar.columns([2, 2], gap="small")
    col1.image(image, width=120)
    col2.markdown("# Fome Zero")

    st.sidebar.markdown("## Filtro")

    countries = st.sidebar.multiselect(
        label= "Escolha os países que deseja visualizar os restaurantes",
        options= df["country"].unique().tolist(), # tolist transforma numa lista
        default= ["Brazil", "England", "Qatar", "South Africa", 
                  "Canada", "Australia"]
    )

    st.sidebar.markdown("### Dados Tratados")

    st.sidebar.download_button(
        label="Download",
        data=df.to_csv(index=False, sep=";"),
        file_name="data.csv",
        mime="text/csv",
    )

    return list(countries)

def create_filtros_restaurants(df):
    top_n = st.sidebar.slider(
        "Selecione a Quantidade de Restaurantes",
        min_value = 1, max_value = 20,
        value = 10
    )

    return top_n

def create_filtros_cuisines(df):

    cuisines = st.sidebar.multiselect(
        label = "Escolha o Tipo de Culinária",
        options = df["cuisines"].unique().tolist(),
        default=[
            "Home-made",
            "BBQ",
            "Japanese",
            "Brazilian",
            "Arabian",
            "American",
            "Italian",
        ]
    )

    return list(cuisines)