import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
st.title('SOLO TERECUERDO QUE ELLA NO TE AMA')
st.markdown('---')
st.markdown('## Que es y para que sirve')
st.sidebar.markdown('Introduccion a los usos de streamlit')
if st.checkbox('has click para ver tu futuro'):
    st.write('ella no te ama')
# Definimos las columnas que nos interesan
fields = ['country', 'points','price', 'variety']

# Cargamos el DataFrame solo con esas columnas
wine_reviews = pd.read_csv('wine_reviews.csv', usecols = fields)
wine_reviews.dropna(inplace = True)

if st.checkbox('mostrar df'):
    st.dataframe(wine_reviews)

if st.checkbox('vista de datos head y tail'):
    if st.button('Mostrar head'):
        st.dataframe(wine_reviews.head())
    if st.button('Mostrar tail'):
        st.dataframe(wine_reviews.tail())

dim = st.radio('selecciona una opcion', ('filas', 'columnas'))
if dim == 'filas':
    st.write(wine_reviews.shape[0])
else:
    st.write(wine_reviews.shape[1])

precio_limite=st.slider('selecciona un valor', min_value = 0, max_value = 4000, value = 250)
fig = plt.figure(figsize = (6, 4))
sns.scatterplot(x = 'price', y = 'points', data = wine_reviews[wine_reviews['price']<precio_limite])
st.pyplot(fig)

countries_list = wine_reviews['country'].unique().tolist()
countries=st.multiselect('selecione los paises a analizar',countries_list,default=['Australia','New Zealand','Canada'])
wine_reviews_filtradas = wine_reviews[wine_reviews['country'].isin(countries)]
fig = plt.figure(figsize = (6, 4))
sns.scatterplot(x="price", y="points", hue='country', data=wine_reviews_filtradas)
st.pyplot(fig)

#creando las colunas
col1,col2=st.columns(2)
with col1:
    fig=plt.figure(figsize=(6,4))
    sns.scatterplot(x="price", y="points", 
                    hue="country",
                    data=wine_reviews[wine_reviews['country']=='Argentina'])
    plt.title('Argentina')
    plt.show()
    st.pyplot(fig)
with col2:
    fig=plt.figure(figsize=(6,4))
    sns.scatterplot(x="price", y="points", 
                    hue="country", 
                    data=wine_reviews[wine_reviews['country']=='Chile'])
    plt.title('chile')
    plt.show()
    st.pyplot(fig)