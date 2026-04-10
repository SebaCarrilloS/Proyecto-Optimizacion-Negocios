# 📧 Incremental Email Targeting with Uplift Modeling

## 1. Problema de negocio

En campañas de marketing, el objetivo no es predecir quién comprará, sino identificar a quién conviene intervenir.

Enviar emails a todos los clientes puede ser ineficiente, ya que:
- algunos comprarían igual (gasto innecesario)
- otros no responderán (sin impacto)
- algunos incluso pueden reaccionar negativamente

El verdadero objetivo es:

> Maximizar el impacto incremental de la campaña.

Este proyecto aborda el problema utilizando técnicas de **uplift modeling / causal machine learning**, estimando el efecto del email sobre cada cliente para optimizar decisiones de targeting.

---

## 2. Dataset

Se utiliza el **Hillstrom Email Marketing Dataset**, que corresponde a un experimento real de marketing.

- ~64.000 clientes
- 3 grupos:
  - `Mens E-Mail`
  - `Womens E-Mail`
  - `No E-Mail`
- Variables:
  - comportamiento histórico del cliente
  - canal de adquisición
  - recencia
  - gasto histórico
- Outcomes:
  - `visit`
  - `conversion`
  - `spend`

Este dataset permite estimar **efectos causales** gracias a su diseño experimental.

---

## 3. Enfoque metodológico

El proyecto se desarrolla en tres etapas:

### 3.1 Baseline (modelo tradicional)

Se entrena un modelo de clasificación para predecir conversión.

Objetivo:
- demostrar que predecir propensión **no es suficiente** para optimizar campañas

---

### 3.2 Uplift Modeling

Se implementa un modelo tipo **T-Learner**:

- modelo 1 → clientes tratados
- modelo 2 → clientes control

El uplift se estima como:

    uplift = P(conversión | tratamiento) - P(conversión | control)

Esto permite identificar clientes:
- persuadables
- sure things
- lost causes
- do-not-disturb

---

### 3.3 Evaluación

Se utilizan métricas específicas de uplift:

- **Uplift Curve**
- **Qini Coefficient**
- análisis por deciles

Estas métricas evalúan la capacidad del modelo para priorizar clientes según impacto incremental.

---

## 4. Resultados clave

El modelo permite:

- identificar el subconjunto de clientes con mayor impacto incremental
- evitar envíos innecesarios
- mejorar eficiencia de la campaña

Hallazgo principal:

> No todos los clientes deben recibir email; el targeting selectivo genera mayor retorno.

---

## 5. Impacto de negocio

Se simulan distintas estrategias de targeting:

- campaña masiva
- targeting top 50%
- targeting top 20%
- targeting top 10%

Para cada caso se estima:

- conversiones incrementales
- ingresos incrementales
- ROI esperado

Esto permite transformar el modelo en una **herramienta de decisión real**.

---

## 6. Estructura del proyecto


├── data/
├── notebooks/
├── src/
├── reports/
└── README.md



Los notebooks siguen el flujo:

1. EDA
2. Baseline
3. Uplift modeling
4. Evaluación
5. Simulación de negocio

---

## 7. Tecnologías utilizadas

- Python
- pandas / numpy
- scikit-learn
- LightGBM
- scikit-uplift
- matplotlib / plotly

---

## 8. Principales aprendizajes

- Diferencia entre predicción y causalidad
- Importancia del uplift en decisiones de marketing
- Uso de métricas adecuadas para evaluación incremental
- Traducción de modelos a impacto económico

---

## 9. Cómo ejecutar el proyecto

1. Descargar dataset
2. Instalar dependencias:

pip install -r requirements.txt


3. Ejecutar notebooks en orden

---

## 10. Próximos pasos

- incorporar X-Learner / causal forest
- optimización bajo restricciones de presupuesto
- extensión a múltiples tratamientos (`Mens` vs `Womens`)
- integración con dashboard en Power BI

---

## 11. Autor

Sebastián Carrillo  S.
Data Analyst / Data Scientist
