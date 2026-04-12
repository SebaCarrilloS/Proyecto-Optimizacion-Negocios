import pandas as pd


def evaluar_estrategia(df, score, p, costo, ingreso):

    n = int(len(df) * p)
    top = df.sort_values(score, ascending=False).head(n)

    conv_t = top[top["tratamiento"] == 1]["target"].mean()
    conv_c = top[top["tratamiento"] == 0]["target"].mean()

    uplift = conv_t - conv_c

    conv_inc = uplift * n
    ingreso_total = conv_inc * ingreso
    costo_total = n * costo
    utilidad = ingreso_total - costo_total
    roi = utilidad / costo_total if costo_total > 0 else 0

    return round(utilidad, 2), round(roi, 2)