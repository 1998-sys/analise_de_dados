import streamlit as st
import pandas as pd

caminho_arquivo = 'Datasets/compras.csv'

df_compras = pd.read_csv(caminho_arquivo, sep = ';', decimal=',', index_col=0)

#print(df_compras)

colunas = list(df_compras.columns)

# Filtro de colunas no sidebar
colunas_selecionadas = st.sidebar.multiselect('Selcione as colunas', colunas, colunas)

# Filtrar linhas
col1, col2 = st.sidebar.columns(2)
col_filtro = col1.selectbox('Selecione a coluna',
               [c for c in colunas if c not in['id compra']])

valor_filtro = col2.selectbox('Selecione o valor',
               list(df_compras[col_filtro].unique()))

st_filtrar = col1.button('Filtar')
st_limpar = col2.button('Limpar')

if st_filtrar:
    st.dataframe(df_compras.loc[df_compras[col_filtro]== valor_filtro, colunas_selecionadas])
elif st_limpar:
    st.dataframe(df_compras[colunas_selecionadas])
else:
    st.dataframe(df_compras[colunas_selecionadas])


