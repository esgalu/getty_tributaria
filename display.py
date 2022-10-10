from io import StringIO
import pandas as pd

import streamlit as st

uploaded_file = st.file_uploader("Arrastra o escoge un archivo")

if uploaded_file is not None:

    dataframe = pd.read_excel(uploaded_file)
    st.write(dataframe)