# 📧 Modelado de Uplift para Optimización de Campañas de Email

## 1. Problema de negocio

En campañas de marketing, el objetivo no es simplemente predecir quién comprará, sino determinar a qué clientes conviene intervenir.

Enviar emails de forma masiva puede ser ineficiente, ya que:

* algunos clientes comprarían igual (gasto innecesario)
* otros no responderán (sin impacto)
* algunos incluso pueden reaccionar negativamente

El verdadero desafío es:

**maximizar el impacto incremental de la campaña.**

Este proyecto utiliza técnicas de **uplift modeling (machine learning causal)** para estimar el efecto del email sobre cada cliente y optimizar decisiones de targeting.

---

## 2. Dataset

Se utiliza el **Hillstrom Email Marketing Dataset**, correspondiente a un experimento real de marketing.

Características principales:

* ~64.000 clientes
* 3 grupos:

  * `Mens E-Mail`
  * `Womens E-Mail`
  * `No E-Mail`
* Variables:

  * comportamiento histórico
  * canal de adquisición
  * recencia
  * gasto histórico
* Resultados observados:

  * `visit`
  * `conversion`
  * `spend`

Gracias a su diseño experimental, el dataset permite estimar efectos causales.

---

## 3. Enfoque del proyecto

El desarrollo se estructura en tres etapas principales:

### 3.1 Modelo base (clasificación tradicional)

Se entrena un modelo para predecir la probabilidad de conversión.

Objetivo:

* demostrar que la predicción de propensión no es suficiente para optimizar campañas

---

### 3.2 Modelado de uplift

Se implementa un modelo tipo **T-Learner**, entrenando:

* un modelo para clientes tratados
* un modelo para clientes no tratados

El uplift se define como:

diferencia entre la probabilidad de conversión con tratamiento y sin tratamiento.

Esto permite identificar distintos tipos de clientes:

* **persuadables**: convierten gracias al email
* **sure things**: convierten de todas formas
* **lost causes**: no convierten
* **do not disturb**: pueden reaccionar negativamente

---

### 3.3 Evaluación

Se utilizan métricas específicas de uplift:

* curva de uplift
* coeficiente Qini
* análisis por deciles

Estas métricas permiten evaluar la capacidad del modelo para priorizar clientes según impacto incremental.

---

## 4. Resultados principales

El modelo permite:

* identificar clientes con mayor impacto incremental
* evitar envíos innecesarios
* mejorar la eficiencia de la campaña

Hallazgo clave:

**no todos los clientes deben ser contactados; el targeting selectivo genera mayor valor.**

---

## 5. Impacto de negocio

Se simulan distintas estrategias de targeting:

* envío masivo
* targeting top 50%
* targeting top 20%
* targeting top 10%

Para cada estrategia se estima:

* conversiones incrementales
* ingresos incrementales
* retorno sobre la inversión (ROI)

Esto permite transformar el modelo en una herramienta de decisión.

---

## 6. Estructura del proyecto

```
datos/
notebooks/
README.md
```

Flujo de trabajo:

1. entendimiento del problema y EDA
2. modelo base de clasificación
3. modelo de uplift
4. evaluación con métricas adecuadas
5. simulación de impacto de negocio

---

## 7. Tecnologías utilizadas

* Python
* pandas
* numpy
* scikit-learn
* LightGBM
* scikit-uplift
* matplotlib / plotly

---

## 8. Principales aprendizajes

* diferencia entre predicción y causalidad
* importancia del impacto incremental en marketing
* uso de métricas específicas de uplift
* traducción de modelos a resultados económicos

---

## 9. Cómo ejecutar el proyecto

1. descargar el dataset
2. ubicarlo en la carpeta `datos/`
3. instalar dependencias:

```
pip install -r requirements.txt
```

4. ejecutar los notebooks en orden

---

## 10. Próximos pasos

* comparar distintos modelos de uplift
* optimización bajo restricciones de presupuesto
* extensión a múltiples tratamientos
* integración con Power BI

---

## 11. Autor

Sebastián Carrillo
Data Scientist / Data Analyst
