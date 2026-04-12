import pandas as pd
from sklift.metrics import uplift_auc_score, qini_auc_score


def evaluar_modelos(df_uplift, df_baseline):

    df = df_uplift.merge(
        df_baseline[["id_cliente", "probabilidad"]],
        on="id_cliente",
        how="inner"
    )

    y = df["target"].values
    w = df["tratamiento"].values

    uplift = df["uplift_estimado"].values
    base = df["probabilidad"].values

    return pd.DataFrame({
        "modelo": ["baseline", "uplift"],
        "uplift_auc": [
            round(uplift_auc_score(y, base, w), 2),
            round(uplift_auc_score(y, uplift, w), 2)
        ],
        "qini_auc": [
            round(qini_auc_score(y, base, w), 2),
            round(qini_auc_score(y, uplift, w), 2)
        ]
    })