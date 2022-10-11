import pandas as pd
from datetime import datetime


def count_days(df):
    in_out = df['In/Out'].tolist()

    list_in_out = [in_out[i + 1] - in_out[i] for i in range(len(in_out) - 1) if
                   in_out[i + 1] - in_out[i] != 0]
    list_index = [index for index, i in enumerate(range(len(in_out) - 1)) if
                  in_out[i + 1] - in_out[i] != 0]

    tmp = df.iloc[list_index].Fecha.tolist()

    tmp.insert(0, df.Fecha.iloc[0])
    tmp.insert(len(tmp), pd.to_datetime(df.Fecha.iloc[-1]))

    values = [(tmp[i + 1] - tmp[i]).days for i in range(len(tmp) - 1)]

    list_in_out.insert(0, df['In/Out'].iloc[0])

    list_in = [index for index, _ in enumerate(list_in_out) if _ == 1]
    list_out = [index for index, _ in enumerate(list_in_out) if _ == -1]

    values_in = [value for index, value in enumerate(values) if
                 index in list_in]
    values_out = [value for index, value in enumerate(values) if
                  index in list_out]

    days_in = sum(values_in) + 1
    days_out = sum(values_out)

    return days_in, days_out
