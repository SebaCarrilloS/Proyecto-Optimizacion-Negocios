# 📧 Optimización de Campañas de Email con Uplift Modeling (Machine Learning Causal)

## 🚀 Resumen ejecutivo

En marketing, predecir quién comprará no es suficiente.
El verdadero desafío es identificar **a quién contactar para generar impacto incremental**.

En este proyecto desarrollé un sistema de **uplift modeling** que estima el efecto causal del envío de emails sobre cada cliente, permitiendo optimizar decisiones de targeting.

### Resultados clave

* El modelo de uplift supera al baseline de clasificación en métricas de impacto incremental (Qini y uplift curve)
* El targeting selectivo genera mayor utilidad que una campaña masiva
* El modelo permite identificar un subconjunto óptimo de clientes a contactar

👉 **Conclusión:**
Ordenar clientes por uplift estimado es más efectivo que ordenarlos por probabilidad de conversión.

---

## 🧠 Problema de negocio

Las campañas masivas presentan ineficiencias importantes:

* se contacta a clientes que comprarían igual (costo innecesario)
* se contacta a clientes que no responderán (sin impacto)
* no se considera la heterogeneidad en la respuesta

El problema real es:

> ¿Cómo maximizar el impacto incremental de una campaña con recursos limitados?

---

## ⚙️ Enfoque

Se utilizó el **Hillstrom Email Marketing Dataset**, basado en un experimento real con:

* ~64.000 clientes
* grupos tratados (`Mens`, `Womens`) y control (`No E-Mail`)
* variables de comportamiento histórico
* resultados observados (`visit`, `conversion`, `spend`)

El flujo del proyecto fue:

1. análisis exploratorio y validación experimental
2. construcción de baseline (clasificación)
3. modelado de uplift con T-Learner
4. evaluación con métricas causales
5. simulación de impacto económico

---

## 🤖 Modelos

### Modelo base (clasificación)

* Regresión logística
* objetivo: predecir probabilidad de conversión
* limitación: no captura impacto incremental

### Modelo de uplift (T-Learner)

* LightGBM
* dos modelos:

  * tratados
  * control
* uplift estimado:

**P(conversión | tratamiento) - P(conversión | control)**

---

## 📊 Evaluación

Se utilizaron métricas específicas para uplift:

* curva de uplift
* curva Qini
* uplift AUC
* Qini AUC
* uplift observado por deciles

### Hallazgos

* el modelo de uplift ordena correctamente a los clientes según impacto incremental
* el baseline prioriza clientes con alta probabilidad de compra, pero no necesariamente con alto uplift
* el uso de `id_cliente` permitió asegurar comparaciones consistentes entre modelos

---

## 💰 Impacto de negocio

Se simularon distintas estrategias de targeting:

* campaña masiva
* targeting basado en clasificación
* targeting basado en uplift

### Resultados

* el targeting selectivo mejora la utilidad frente a campañas masivas
* el modelo de uplift genera mayor ROI que el baseline
* existe un punto óptimo de contacto (no todos los clientes deben ser contactados)

👉 Insight principal:

**más contacto no implica más valor — el valor está en contactar a los clientes correctos**

---

## 📈 Decisión que habilita el modelo

El modelo permite responder:

* ¿qué proporción de clientes conviene contactar?
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

* la diferencia entre predicción y causalidad es clave en decisiones de negocio
* el uplift modeling permite optimizar intervenciones, no solo predecir resultados
* métricas tradicionales no son adecuadas para evaluar impacto incremental
* el valor de un modelo está en su capacidad de mejorar decisiones

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

* implementación de X-Learner o Causal Forest
* optimización bajo restricciones de presupuesto
* extensión a múltiples tratamientos
* integración con dashboard (Power BI)

---

## 👤 Autor

Sebastián Carrillo
Data Scientist / Data Analyst
