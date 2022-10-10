def clean_file(df):

    df = df.dropna(subset=['In/Out'])
    df = df.replace({'In/Out': {'In': 1, 'Out': 0}})

    return df

