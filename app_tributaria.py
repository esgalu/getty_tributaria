import pandas as pd
import streamlit as st
from datetime import datetime
from dateutil.relativedelta import relativedelta

from src.utils.calculate_date import count_days
from src.utils.transform import clean_file

st.title("Residencia Fiscal")

st.write("""

La residencia fiscal es un concepto que se aplica a todas las personas naturales
indiferente de su nacionalidad; este determina cómo se gravan los impuestos 
conforme al sistema tributario de cada país en particular. Esto dependerá del 
lugar donde una persona pase la mayor parte del año.""")
st.write("""
De acuerdo a la ley colombiana, una persona natural (sin importar su 
nacionalidad) se considerará residente fiscal colombiano cuando permanezca más 
de 183 días calendario en Colombia durante un periodo cualquiera de 365 
días calendario consecutivos. Y conforme a eso deberá reportar los ingresos que
 hayan generado dentro y fuera del país, y adicionalmente, los bienes que
  posean tanto en Colombia como en el exterior.""")

st.sidebar.header("Archivo")
st.sidebar.write("""
El archivo de excel debe tener dos columnas con los datos. Las columnas deben 
estar con los siguientes nombres: Fecha, In/Out""")

uploaded_file = st.sidebar.file_uploader("Arrastra o escoge un archivo")

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    df = clean_file(df)

    st.sidebar.subheader(f"Cantidad de registros en el archivo: {len(df)}")
    st.sidebar.table(df.head(3).append(df.tail(3)))

    start_time = st.slider(
        "Filtro de fecha inicial",
        min_value=datetime.date(pd.to_datetime(df.Fecha.iloc[0])),
        max_value=datetime.date(datetime.today()),
        format="YYYY-MM-DD")

    date_range = pd.date_range(
        start_time,
        start_time + relativedelta(days=365)
    )

    col1, col2 = st.columns(2)

    col1.subheader(f"Fecha de inicio {start_time}")

    col2.subheader(f"Fecha final {start_time + relativedelta(days=365)}")
    cond_dates = df.Fecha.isin(date_range)

    df = df[cond_dates]

    days_in, days_out = count_days(df)

    col1.subheader(f"Días en el país {days_in}")
    col2.subheader(f"Días fuera del país {days_out}")

    st.area_chart(data=df, x='Fecha', y='In/Out')