import pandas as pd
import streamlit as st



st.markdown("TITULO")

st.sidebar.markdown("ARCHIVO")

uploaded_file = st.sidebar.file_uploader("Arrastra o escoge un archivo")

if uploaded_file is not None:

    dataframe = pd.read_excel(uploaded_file)
    st.sidebar.write(dataframe)