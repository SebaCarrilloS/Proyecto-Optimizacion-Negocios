# 📧 Optimización de Campañas de Email con Uplift Modeling (Machine Learning Causal)

## 🚀 Resumen ejecutivo

En campañas de marketing, el objetivo no es predecir quién comprará, sino identificar a quién conviene contactar para generar impacto incremental.

En este proyecto desarrollé un modelo de **uplift modeling** que permite estimar el efecto causal del envío de emails sobre cada cliente, optimizando decisiones de targeting.

Resultados principales:

* El modelo de uplift supera al baseline de clasificación en métricas de impacto incremental (Qini y uplift curve)
* Estrategias de targeting selectivo generan mayor utilidad que campañas masivas
* Se logra mejorar el retorno económico al priorizar clientes con mayor respuesta incremental

👉 Conclusión:
**ordenar clientes por uplift es más efectivo que ordenarlos por probabilidad de conversión**

---

## 🧠 Problema de negocio

Las campañas tradicionales presentan tres problemas:

* se contacta a clientes que comprarían igual (costo innecesario)
* se contacta a clientes que no responderán (sin impacto)
* se ignora la heterogeneidad en la respuesta al tratamiento

El problema real es:

> ¿A qué clientes conviene enviar un email para maximizar el impacto incremental?

---

## ⚙️ Enfoque

Se utilizó el **Hillstrom Email Marketing Dataset**, un experimento real con:

* ~64.000 clientes
* grupos tratados (`Mens`, `Womens`) y control (`No E-Mail`)
* variables de comportamiento histórico
* outcomes: `visit`, `conversion`, `spend`

El proyecto se estructuró en 5 etapas:

1. análisis exploratorio y validación del experimento
2. modelo base de clasificación
3. modelo de uplift (T-Learner)
4. evaluación con métricas causales
5. simulación de impacto de negocio

---

## 🤖 Modelos

### Modelo base (clasificación)

* Regresión logística
* objetivo: predecir probabilidad de conversión

### Modelo de uplift

* T-Learner con LightGBM
* dos modelos:

  * clientes tratados
  * clientes control
* uplift estimado:

  diferencia entre probabilidad con tratamiento y sin tratamiento

---

## 📊 Evaluación

Se utilizaron métricas específicas de uplift:

* curva de uplift
* curva Qini
* uplift AUC
* Qini AUC
* uplift observado por segmentos

Resultados:

* el modelo de uplift logra priorizar mejor a los clientes con mayor impacto incremental
* el baseline identifica clientes con alta probabilidad de compra, pero no necesariamente con alto uplift

---

## 💰 Impacto de negocio

Se simularon distintas estrategias de targeting:

* campaña masiva
* targeting basado en clasificación
* targeting basado en uplift

Para cada estrategia se estimó:

* conversiones incrementales
* ingresos incrementales
* costo de campaña
* utilidad
* ROI

### Hallazgos clave

* el targeting selectivo supera a la campaña masiva en términos de utilidad
* el modelo de uplift mejora el ROI frente al baseline
* existe un punto óptimo de contacto (no es 100% de clientes)

👉 Insight principal:

**el valor no está en contactar más clientes, sino en contactar a los correctos**

---

## 📈 Ejemplo de decisión

El modelo permite responder preguntas como:

* ¿conviene contactar al top 10%, 20% o 50%?
* ¿cuánto ingreso incremental genera cada estrategia?
* ¿cuál es el ROI esperado?

Esto transforma el modelo en una herramienta de decisión real.

---

## 🧩 Estructura del proyecto

```text
notebooks/
│
├── 01_entendimiento_negocio_y_eda.ipynb
├── 02_modelo_base_clasificacion.ipynb
├── 03_modelo_uplift_t_learner.ipynb
├── 04_evaluacion_uplift_y_qini.ipynb
└── 05_simulacion_impacto_negocio.ipynb
```

---

## 🛠️ Tecnologías utilizadas

* Python
* pandas / numpy
* scikit-learn
* LightGBM
* scikit-uplift
* matplotlib

---

## 🧠 Principales aprendizajes

* diferencia entre predicción y causalidad
* importancia del impacto incremental en marketing
* uso de métricas adecuadas para uplift
* traducción de modelos a decisiones de negocio

---

## 🔍 Cómo ejecutar

1. descargar dataset Hillstrom
2. ubicar en carpeta local
3. instalar dependencias:

```
pip install -r requirements.txt
```

4. ejecutar notebooks en orden

---

## 📌 Próximos pasos

* comparar con X-Learner / Causal Forest
* optimización bajo restricciones de presupuesto
* extensión a múltiples tratamientos
* integración con dashboard (Power BI)

---

## 👤 Autor

Sebastián Carrillo
Data Scientist / Data Analyst
