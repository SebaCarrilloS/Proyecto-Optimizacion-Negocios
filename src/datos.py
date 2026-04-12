import pandas as pd

def cargar_datos(ruta_csv):
    df = pd.read_csv(ruta_csv)
    df = df.reset_index().rename(columns={"index": "id_cliente"})
    return df


def preparar_datos(df):
    df = df.copy()

    df["tratamiento"] = df["segment"].apply(lambda x: 0 if x == "No E-Mail" else 1)
    df["target"] = df["conversion"]

    columnas_excluir = ["segment", "conversion", "visit", "spend", "target"]
    columnas_features = [col for col in df.columns if col not in columnas_excluir]

    X = df[columnas_features].copy()
    y = df["target"].copy()
    w = df["tratamiento"].copy()

    return df, X, y, w