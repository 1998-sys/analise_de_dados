import streamlit as st
import pandas as pd

caminho_compras = 'Datasets/compras.csv'

df_compras = pd.read_csv(caminho_compras, sep=';', decimal = ',')
print(df_compras)

st.dataframe(df_compras)