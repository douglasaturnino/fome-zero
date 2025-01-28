import plotly.express as px

def restaurante_avalia(df, countries, top_n):
    lines = (df["country"].isin(countries))
    df_aux = (df.loc[lines, ["restaurant_name", "votes"]].groupby("restaurant_name")
    .max()
    .sort_values("votes", ascending=False)
    .reset_index()
    .head(top_n)
    )

    fig = px.bar(
        df_aux,
        x = "restaurant_name",
        y = "votes",
        text = "votes",
        text_auto=".2f", 
        title = "Os Restaurantes que possuem mais Avaliações",
        labels = {"restaurant_name": "Restaurantes",
                 "votes": "Avaliações Cadastradas"}
    )

    return fig

def restaurante_entrega_online(df):
    df_aux = (df.loc[:, ["restaurant_name", "has_online_delivery"]].groupby("has_online_delivery")
    .count()
    .sort_values("restaurant_name", ascending=False)
    .reset_index()
    )

    fig = px.pie(df_aux, values='restaurant_name', 
                 names={'0': 'Não aceita pedido', '1': 'Aceita pedido'}, 
                 title='Restaurante possui serviços de pedido on-line')
    fig.update_traces(textposition='inside', textinfo='percent+label')
    return fig

def restaurante_aceitam_reservas(df):
    df_aux = (df.loc[:, ["restaurant_name", "has_table_booking"]]
        .groupby("has_table_booking")
        .count()
        .sort_values("restaurant_name", ascending=False)
        .reset_index()
        )

    fig = px.pie(df_aux, values='restaurant_name', 
                 names={'0': 'Não aceita reserva', '1': 'Aceita reserva'}, 
                 title='Restaurante possui serviços de reserva')
    fig.update_traces(textposition='inside', textinfo='percent+label')
    return fig

def restaurante_faz_entregas(df):
    df_aux = (df.loc[:, ["restaurant_name", "is_delivering_now"]]
        .groupby("is_delivering_now")
        .count()
        .sort_values("restaurant_name", ascending=False)
        .reset_index()
        )

    fig = px.pie(df_aux, values='restaurant_name', 
                 names={'0': 'Não faz entregas', '1': 'Faz entregas'}, 
                 title='Restaurante que faz serviço de entregas')
    fig.update_traces(textposition='inside', textinfo='percent+label')
    return fig
