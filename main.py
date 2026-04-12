import sys
from pathlib import Path
import warnings

warnings.filterwarnings("ignore")

# Para asegurar imports de src
sys.path.append(str(Path(__file__).parent))

import pandas as pd
from sklearn.model_selection import train_test_split

from src.datos import cargar_datos, preparar_datos
from src.preprocesamiento import crear_preprocesador
from src.modelos import entrenar_baseline, entrenar_t_learner
from src.evaluacion import evaluar_modelos


# =========================
# RUTAS
# =========================
RUTA_DATOS = Path(r"C:\Users\sebas\OneDrive\Desktop\Proyecto Chatbot\Opti-Correos\hillstrom.csv")

RUTA_BASELINE = Path("baseline_resultados_test.csv")
RUTA_UPLIFT = Path("uplift_resultados_test.csv")
RUTA_METRICAS = Path("resumen_metricas_modelos.csv")


# =========================
# MAIN
# =========================
def main():

    print("Cargando datos...")
    df = cargar_datos(RUTA_DATOS)

    print("Preparando datos...")
    df, X, y, w = preparar_datos(df)

    print("Dividiendo train/test...")
    X_train, X_test, y_train, y_test, w_train, w_test = train_test_split(
        X, y, w,
        test_size=0.3,
        random_state=42
    )

    print("Creando preprocesador...")
    preprocesador = crear_preprocesador(X)

    # =========================
    # MODELO BASELINE
    # =========================
    print("Entrenando baseline...")
    baseline = entrenar_baseline(X_train, y_train, preprocesador)

    y_prob = baseline.predict_proba(X_test)[:, 1]

    df_baseline = X_test.copy()
    df_baseline["id_cliente"] = df.loc[X_test.index, "id_cliente"].values
    df_baseline["target"] = y_test.values
    df_baseline["tratamiento"] = w_test.values
    df_baseline["probabilidad"] = y_prob

    # =========================
    # MODELO UPLIFT (T-LEARNER)
    # =========================
    print("Entrenando modelo uplift...")
    modelo_t, modelo_c = entrenar_t_learner(X_train, y_train, w_train, preprocesador)

    prob_tratado = modelo_t.predict_proba(X_test)[:, 1]
    prob_control = modelo_c.predict_proba(X_test)[:, 1]

    df_uplift = X_test.copy()
    df_uplift["id_cliente"] = df.loc[X_test.index, "id_cliente"].values
    df_uplift["target"] = y_test.values
    df_uplift["tratamiento"] = w_test.values
    df_uplift["uplift_estimado"] = prob_tratado - prob_control

    # =========================
    # EVALUACIÓN
    # =========================
    print("Evaluando modelos...")
    resumen = evaluar_modelos(df_uplift, df_baseline)

    print("\n===== RESULTADOS =====")
    print(resumen)

    # =========================
    # EXPORTAR RESULTADOS
    # =========================
    print("\nGuardando resultados...")

    df_baseline.to_csv(RUTA_BASELINE, index=False)
    df_uplift.to_csv(RUTA_UPLIFT, index=False)
    resumen.to_csv(RUTA_METRICAS, index=False)

    print("Archivos generados:")
    print(f"- {RUTA_BASELINE}")
    print(f"- {RUTA_UPLIFT}")
    print(f"- {RUTA_METRICAS}")

    print("\nPipeline ejecutado correctamente.")


# =========================
# EJECUCIÓN
# =========================
if __name__ == "__main__":
    main()