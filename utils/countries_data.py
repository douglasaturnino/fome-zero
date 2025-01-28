import plotly.express as px

def countries_restaurants(countries, df):
    df_aux = (df.loc[df["country"].isin(countries), ["country", "restaurant_name"]]
    .groupby("country")
    .nunique()
    .sort_values("restaurant_name", ascending=False)
    .reset_index()
    )

    fig = px.bar(
        df_aux,
        x = "country",
        y = "restaurant_name",
        text = "restaurant_name",
        title = "Quantidade de Restaurantes Registrados por País",
        labels = {"country": "Paises",
                 "restaurant_name": "Quantidade de Restaurantes"}
    )

    return fig

def countries_cities(countries, df):
    df_aux = (df.loc[df["country"].isin(countries), 
                     ["country", "city"]]
    .groupby("country")
    .nunique()
    .sort_values("city", ascending=False)
    .reset_index()
    )

    fig = px.bar(
        df_aux,
        x = "country",
        y = "city",
        text = "city",
        title = "Quantidade de Cidades Registradas por País",
        labels = {"country": "Paises",
                 "city": "Quantidade de Cidade"}
    )

    return fig

def countries_votes(countries, df):
    df_aux = (df.loc[df["country"].isin(countries), 
                     ["country", "votes"]]
    .groupby("country")
    .mean()
    .sort_values("votes", ascending=False)
    .reset_index()
    )

    fig = px.bar(
        df_aux,
        x = "country",
        y = "votes",
        text = "votes",
        text_auto=".2f", 
        title = "Média de Avaliações Registradas por País",
        labels = {"country": "Paises",
                 "votes": "Avaliações Cadastradas"}
    )

    return fig

def countries_average_for_two(countries, df):
    df_aux = (df.loc[df["country"].isin(countries),
                     ["country", "average_cost_for_two"]]
    .groupby("country")
    .mean()
    .sort_values("average_cost_for_two", ascending=False)
    .reset_index()
    )

    fig = px.bar(
        df_aux,
        x = "country",
        y = "average_cost_for_two",
        text = "average_cost_for_two",
        text_auto=".2f", 
        title = "Média de um prato para 2 pessoas por País",
        labels = {"country": "Paises",
                 "average_cost_for_two": "Média de um prato para duas pessoas"}
    )

    return fig

