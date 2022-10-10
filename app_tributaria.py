import pandas as pd
import streamlit as st

uploaded_file = st.file_uploader("Arrastra o escoge un archivo")


st.markdown("TITULO")

st.sidebar.markdown("ARCHIVO")

if uploaded_file is not None:

    dataframe = pd.read_excel(uploaded_file)
    st.write(dataframe)