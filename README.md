# Proyecto_4

## A/B Testing Vanguard – Optimización de la nueva interfaz

## Objetivo del proyecto

Este proyecto analiza un test A/B realizado para evaluar el impacto del nuevo diseño de interfaz sobre la tasa de finalización de usuarios. El objetivo principal es determinar si el nuevo diseño:
- Incrementa significativamente la tasa de finalización.
- Supera el umbral mínimo de mejora del 5% definido por la empresa.
- Presenta diferencias en comportamiento según segmentos demográficos.

## Contexto del negocio

Vanguard implementó un nuevo diseño web para optimizar la experiencia de los usuarios. El desafío es decidir si el nuevo diseño debe implementarse de forma definitiva, considerando:
- Impacto en la tasa de finalización del proceso.
- Costo-Efectividad: la mejora debe ser al menos +5%.
- Comportamiento del usuario durante los pasos: tiempo entre paso y paso y retrocesos (errores) entre cada uno de estos.
- Diferencias por segmento demográfico (ej. edad).

## Dataset

Para este proyecto se han utilizados tres datasets (df_final_web_data, final_final_experiment_clients y df_final_demo).  

Variables principales:
- client_id: identificador de usuario
- Variation: grupo del experimento (Control/ Test)
- process_step: pasos del proceso en línea. (start, step_1, step_2, step_3, confirm)
- duracion: tiempo entre un paso y el siguiente (procesado como segundos)
- check_error: indicador de retroceso a un paso anterior
- age_category: segmento etario (ej. Young Adult, Senior)


## Notas de calidad del dato**

- El dataset contiene la información básica de la experiencia del usuario, por lo que fue necesario calcular métricas.
- Se revisaron posibles inconsistencias de tracking (usuarios con múltiples eventos por paso o reintentos).
- Para la medición del tiempo, se transformo los tiempos a segundos.

## Preguntas clave

1. ¿El nuevo diseño mejora la tasa de finalización respecto al anterior?
2. ¿La mejora observada supera la tasa control en un %5 para justificar el costo del rediseño?
3. ¿Existe una mayor tasa de finalización en jovenes adultos que en seniors dentro del grupo test?
4. Los clientes con mayor antigüedad en Vanguard (categoría "Veteran") presentan una mayor tasa de finalización en el diseño antiguo (Control) que en el nuevo (Test).
5. Los clientes con balances altos presentan una tasa de finalización menor en el grupo Test que en el grupo Control.

## Proceso de análisis

1. EDA: distribución de eventos por paso, comportamiento por variación, revisión de duplicados por usuario.
2. Limpieza y preparación:
   - Conversión de fechas.
   - Cálculo de duracion entre pasos (a nivel de evento).
   - Creación de columna completed para comparar tasa de finalización. 
3. KPIs calculados:
   - Tasa de finalización: proporción de usuarios que llegan a confirm.
   - Tiempo promedio por paso: promedio de duración hasta el siguiente paso.
   - Tasa de error: retrocesos a pasos anteriores.

## Resultados / Insights
Tasa de finalización (Control vs Test):
- Control: 13.12%
- Test: 16.70%
- Resultado: diferencia estadísticamente significativa (p ≪ 0.05).

Umbral de costo-efectividad (+5%):
- El Test supera el umbral de manera estadísticamente significativa (p ≪ 0.05).

Segmentación por edad:
- Se observan diferencias por segmento: Seniors > Young Adults.

Segmentación por antiguedad: 
- La tasa de finalización de los veteranos es mayor en el Test. 

Segmentación por dinero en cartera:
- La tasa de finalización de los "vip" es mayor en el Test. 


## Recomendaciones de negocio
1. Implementar el nuevo diseño: mejora la finalización y supera el umbral del +5%.
2. Optimizar pasos con mayor "error_step": priorizar los pasos donde se concentran más retrocesos y mayor tiempo promedio.
3. Posibilidad de personalización de UX: dado que Seniors presenta mejor finalización que Young Adults, explorar ajustes para mejorar el desempeño.
4. Proponer un seguimiento post-lanzamiento con métricas de calidad (tiempo, errores, feedback) para validar estabilidad de la nueva interfaz. 

## Limitaciones
- Dataset "web_data" requiere agregaciones a nivel usuario para evitar sesgos.
- La métrica “duración” puede verse afectada por pausas/reanudación (sesiones abiertas, abandonos y retornos).

## Próximos pasos
- Analizar el comportamiento de los usuarios según el tipo de dispotivo.
- Evaluar métricas adicionales: abandono por paso, tiempo total del proceso, usuarios con múltiples intentos.


## Cómo replicar el proyecto
1. Ejecutar notebooks de limpieza y análisis
2. Visualización en Tableau
3. (Opcional) Streamlit


