import pandas as pd
import streamlit as st

from src.utils.read_excel import read_file

st.markdown("TITULO")

st.sidebar.markdown("ARCHIVO")

uploaded_file = st.sidebar.file_uploader("Arrastra o escoge un archivo")

if uploaded_file is not None:

    df = read_file(uploaded_file)
    st.sidebar.write(df)
