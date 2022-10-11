import pandas as pd
import streamlit as st

from src.utils.calculate_date import count_days
from src.utils.transform import clean_file

st.markdown("TITULO")

st.sidebar.markdown("ARCHIVO")

uploaded_file = st.sidebar.file_uploader("Arrastra o escoge un archivo")

if uploaded_file is not None:

    df = pd.read_excel(uploaded_file)
    df = clean_file(df)
    days_in, days_out = count_days(df)
    st.sidebar.write(df)

    st.markdown(f"fechas in {days_in}")
    st.markdown(f"fechas out {days_out}")
