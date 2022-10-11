import pandas as pd
import streamlit as st
from datetime import datetime
from dateutil.relativedelta import relativedelta

from src.utils.calculate_date import count_days
from src.utils.transform import clean_file

st.markdown("TITULO")

st.sidebar.markdown("ARCHIVO")

uploaded_file = st.sidebar.file_uploader("Arrastra o escoge un archivo")

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    df = clean_file(df)

    start_time = st.slider(
        "When do you start?",
        min_value=datetime.date(pd.to_datetime(df.Fecha.iloc[0])),
        max_value=datetime.date(datetime.today()),
        format="YYYY-MM-DD")

    date_range = pd.date_range(
        start_time,
        start_time + relativedelta(days=365)
    )

    st.write("Start time:", start_time)
    st.write("End time:", start_time + relativedelta(days=365))

    cond_dates = df.Fecha.isin(date_range)

    df = df[cond_dates]

    st.area_chart(data=df, x='Fecha', y='In/Out')
    days_in, days_out = count_days(df)

    st.markdown(f"fechas in {days_in}")
    st.markdown(f"fechas out {days_out}")

    st.table(df.head().append(df.tail()))


