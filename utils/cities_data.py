import plotly.express as px

def cities_restaurant_10(countries, df): 
    df_aux = (df.loc[df["country"].isin(countries), ["city","restaurant_name"]].groupby("city")
    .nunique()
    .sort_values("restaurant_name", ascending=False)
    .reset_index()
    ) 

    fig = px.bar(
        df_aux.head(10),
        x = "city",
        y = "restaurant_name",
        text = "restaurant_name",
        title = "Top 10 Cidades com mais Restaurantes",
        labels = {"city": "Cidades",
                 "restaurant_name": "Quantidade de Restaurantes"}
    )

    return fig

def cities_restaurant_4(countries, df): 
    df_aux = (df.loc[
                (df["aggregate_rating"] > 4) & (df["country"].isin(countries)), 
                ["city", "restaurant_name"]]
              .groupby("city")
              .count()
              .sort_values("restaurant_name", ascending=False)
              .reset_index())

    fig = px.bar(
        df_aux.head(7),
        x = "city",
        y = "restaurant_name",
        text = "restaurant_name",
        title = "Top 7 Cidades com Média de Avaliação acima de 4",
        labels = {"city": "Cidades",
                 "restaurant_name": "Quantidade de Restaurantes"}
    )

    return fig

def cities_restaurant_2_5(countries, df): 
    df_aux = (df.loc[
                (df["aggregate_rating"] < 2.5) & (df["country"].isin(countries)), 
                ["city", "restaurant_name"]]
              .groupby("city")
              .count()
              .sort_values("restaurant_name", ascending=False)
              .reset_index())

    fig = px.bar(
        df_aux.head(7),
        x = "city",
        y = "restaurant_name",
        text = "restaurant_name",
        title = "Top 7 Cidades com Média de Avaliação abaixo de 2.5",
        labels = {"city": "Cidades",
                 "restaurant_name": "Quantidade de Restaurantes"}
    )

    return fig

def cities_cuisine_10(countries, df): 
    df_aux = (df.loc[df["country"].isin(countries), ["city","cuisines"]].groupby("city")
    .nunique()
    .sort_values("cuisines", ascending=False)
    .reset_index()
    ) 

    fig = px.bar(
        df_aux.head(10),
        x = "city",
        y = "cuisines",
        text = "cuisines",
        title = "Top 10 Cidades com Restaurantes com Tipos de Culinárias Distintos",
        labels = {"city": "Cidades",
                 "cuisines": "Tipo de Culinárias"}
    )

    return fig





