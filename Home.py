import streamlit as st

st.set_page_config(page_title="Home")

st.sidebar.image(image = "imagem/logo.jpg")

st.sidebar.markdown("# Fome Zero - Restaurantes")

st.sidebar.markdown("### Teste a melhor culinária do mundo")

st.sidebar.markdown('___')

st.sidebar.markdown('###### Powered by Fernanda Chuerubim')

st.header("Fome Zero - Dashboards")

st.subheader('Os melhores restaurantes do mundo em um só lugar')

st.markdown('___')

st.markdown('###### Este Dashboard foi elaborado para fornecer métricas de acompanhamento e crescimento solicitados pelo CEO da empresa.')

st.markdown('⚙️ VISÃO GERAL')
st.write('###### Descreve a quantidade de restaurantes e cidades por país, bem como a média de avaliações e a média de preço de um prato para duas pessoas.')

st.markdown('🌎 VISÃO PAÍSES')
st.write('###### Descreve a quantidade de restaurantes e cidades por país, bem como a média de avaliações e a média de preço de um prato para duas pessoas.')

st.markdown('🏙️ VISÃO CIDADES')
st.write('###### Análise das métricas classificadas por cidades, considerando avaliações dos restaurantes, tipos de culinárias disponíveis e os valores cobrados.')

st.markdown('🛎️ VISÃO RESTAURANTES')
st.write('###### Métricas gerais dos restaurantes, tais como: melhores restaurantes, restaurantes com mais avaliações e aqueles que reservam mesa e realizam entregas.')

st.markdown('🍽️ VISÃO CULINÁRIAS')
st.write('###### Análise das métricas relacionadas aos diversos tipos de culinárias, incluindo os melhores restaurantes por cada tipo de culinária.')

st.markdown('___')
st.markdown('### Contato do Cientista de Dados: Fernanda Chuerubim')
st.write('##### Time de Data Science no Discord: @fernanda.3458')
