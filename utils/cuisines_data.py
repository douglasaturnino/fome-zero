import streamlit as st
import pandas as pd
import plotly.express as px

def tabela_cuisines(df, countries, top_n, cuisines):
    cols = [
        "restaurant_id",
        "restaurant_name",
        "country",
        "city",
        "cuisines",
        "average_cost_for_two",
        "aggregate_rating",
        "votes",
    ]

    linha = (df["country"].isin(countries)) & (df["cuisines"].isin(cuisines))

    df_aux = (df.loc[linha, cols]
              .sort_values("aggregate_rating", ascending=False)
              .head(top_n))

    return df_aux

def top_cuisines(df):

    cuisines = {
        "Italian": "",
        "American": "",
        "Arabian": "",
        "Japanese": "",
        "Brazilian": "",
    }

    cols = [
        "restaurant_id",
        "restaurant_name",
        "country",
        "city",
        "cuisines",
        "average_cost_for_two",
        "currency",
        "aggregate_rating",
        "votes",
    ]

    for key in cuisines.keys(): # keys faz um iteração nas chaves do cuisines
        lines = df["cuisines"] == key # sinal == é comparação
        cuisines[key] = (
            df.loc[lines, cols]
            .sort_values(["aggregate_rating", "restaurant_id"], ascending=[False, True])
            .iloc[0, :] # o zero significa primeira linha e todas as colunas
            .to_dict() # to_dict serve pra transformar em dicionario
        )

    return cuisines

def write_metrics(df):
    cuisines = top_cuisines(df)

    italian, american, arabian, japonese, brazilian = st.columns(len(cuisines))

    with italian:
        st.metric( 
            label=f'Italiana: {cuisines["Italian"]["restaurant_name"]}',
            value=f'{cuisines["Italian"]["aggregate_rating"]}/5.0',
            help=f"""
            País: {cuisines["Italian"]['country']}\n
            Cidade: {cuisines["Italian"]['city']}\n
            Média Prato para dois: {cuisines["Italian"]['average_cost_for_two']} ({cuisines["Italian"]['currency']})
            """,
        )
    
    with american:
        st.metric( 
            label=f'Americana: {cuisines["American"]["restaurant_name"]}',
            value=f'{cuisines["American"]["aggregate_rating"]}/5.0',
            help=f"""
            País: {cuisines["American"]['country']}\n
            Cidade: {cuisines["American"]['city']}\n
            Média Prato para dois: {cuisines["American"]['average_cost_for_two']} ({cuisines["American"]['currency']})
            """,
        )

    with arabian:
        st.metric( 
            label=f'Árabe: {cuisines["Arabian"]["restaurant_name"]}',
            value=f'{cuisines["Arabian"]["aggregate_rating"]}/5.0',
            help=f"""
            País: {cuisines["Arabian"]['country']}\n
            Cidade: {cuisines["Arabian"]['city']}\n
            Média Prato para dois: {cuisines["Arabian"]['average_cost_for_two']} ({cuisines["Arabian"]['currency']})
            """,
        )

    with japonese:
        st.metric( 
            label=f'Japonesa: {cuisines["Japanese"]["restaurant_name"]}',
            value=f'{cuisines["Japanese"]["aggregate_rating"]}/5.0',
            help=f"""
            País: {cuisines["Japanese"]['country']}\n
            Cidade: {cuisines["Japanese"]['city']}\n
            Média Prato para dois: {cuisines["Japanese"]['average_cost_for_two']} ({cuisines["Japanese"]['currency']})
            """,
        )

    with brazilian:
        st.metric( 
            label=f'Brasileira: {cuisines["Brazilian"]["restaurant_name"]}',
            value=f'{cuisines["Brazilian"]["aggregate_rating"]}/5.0',
            help=f"""
            País: {cuisines["Brazilian"]['country']}\n 
            Cidade: {cuisines["Brazilian"]['city']}\n
            Média Prato para dois: {cuisines["Brazilian"]['average_cost_for_two']} ({cuisines["Brazilian"]['currency']})
            """,
        )

def top_cuisines_melhores(df, countries, top_n):
    lines = (df["country"].isin(countries))
    df_aux = (df.loc[ lines, ["aggregate_rating", "cuisines"]]
            .groupby(["cuisines"])
            .mean()
            .sort_values("aggregate_rating", ascending=False)
            .reset_index()
            .head(top_n)
            )

    fig = px.bar(
        df_aux,
        x = "cuisines",
        y = "aggregate_rating",
        text = "aggregate_rating",
        text_auto=".2f", # f de float
        title = f"Top {top_n} Melhores Tipos de Culinárias",
        labels = {"cuisines": "Tipos de Culinárias",
                 "aggregate_rating": "Nota Média"}
        #color_discrete_sequence=["green"] 
    )

    return fig

def top_cuisines_piores(df, countries, top_n):
    lines = (df["country"].isin(countries))
    df_aux = (df.loc[ lines, ["aggregate_rating", "cuisines"]]
            .groupby(["cuisines"])
            .mean()
            .sort_values("aggregate_rating", ascending=True)
            .reset_index()
            .head(top_n)
            )

    fig = px.bar(
        df_aux,
        x = "cuisines",
        y = "aggregate_rating",
        text = "aggregate_rating",
        text_auto=".2f", # f de float
        title = f"Top {top_n} Piores Tipos de Culinárias",
        labels = {"cuisines": "Tipos de Culinárias",
                 "aggregate_rating": "Nota Média"}
        #color_discrete_sequence=["green"] 
    )

    return fig

