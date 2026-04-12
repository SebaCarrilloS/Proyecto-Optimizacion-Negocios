from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from lightgbm import LGBMClassifier


def entrenar_baseline(X_train, y_train, preprocesador):
    """
    Entrena un modelo base de clasificación tradicional.
    """
    modelo = Pipeline([
        ("preprocesamiento", preprocesador),
        ("modelo", LogisticRegression(max_iter=1000))
    ])

    modelo.fit(X_train, y_train)
    return modelo


def entrenar_t_learner(X_train, y_train, w_train, preprocesador):
    """
    Entrena un modelo T-Learner:
    - un modelo para tratados
    - un modelo para control
    """

    X_t = X_train[w_train == 1].copy()
    y_t = y_train[w_train == 1].copy()

    X_c = X_train[w_train == 0].copy()
    y_c = y_train[w_train == 0].copy()

    params = dict(
        n_estimators=300,
        learning_rate=0.05,
        max_depth=4,
        num_leaves=15,
        min_child_samples=50,
        min_split_gain=0.01,
        subsample=0.8,
        colsample_bytree=0.8,
        random_state=42,
        verbosity=-1
    )

    modelo_t = Pipeline([
        ("preprocesamiento", preprocesador),
        ("modelo", LGBMClassifier(**params))
    ])

    modelo_c = Pipeline([
        ("preprocesamiento", preprocesador),
        ("modelo", LGBMClassifier(**params))
    ])

    modelo_t.fit(X_t, y_t)
    modelo_c.fit(X_c, y_c)

    return modelo_t, modelo_c