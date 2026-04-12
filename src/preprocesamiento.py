from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

def crear_preprocesador(X):
    categoricas = X.select_dtypes(include=["object"]).columns.tolist()
    numericas = X.select_dtypes(exclude=["object"]).columns.tolist()

    return ColumnTransformer(
        transformers=[
            ("cat", OneHotEncoder(handle_unknown="ignore"), categoricas),
            ("num", "passthrough", numericas),
        ]
    )