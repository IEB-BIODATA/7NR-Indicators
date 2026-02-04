# Proyecto: Pipeline Analítico de Glosas, Gasto Público y MIDESO

Este proyecto implementa un **pipeline analítico rule-based** para analizar gasto público,
partiendo desde un **lookup table de reglas**, descargando datos vía API,
aplicando **ponderaciones sectoriales** y generando visualizaciones.

El enfoque es **determinístico y explícito**: no se usan modelos estadísticos ni ML.

---
## 🔹 1. Lookup Table (definición de reglas)

### 📄 `lookup_table_glosas_querybuild.csv`

Archivo **central del pipeline**.

Define las **reglas de matching** que se usarán para:
- construir queries a la API
- clasificar gasto descargado

Cada fila representa una regla con combinaciones de:
- partida
- capítulo
- código de programa presupuestario
- área
- subtítulo
- ítem
- asignación
- nombre lógico de glosa (`String_name`)


---

## 🔹 2. Generación y descarga de datos

### 🐍 `querymaker_descargar_glosas.py`

Script que:
- lee el `lookup_table`
- construye queries según las reglas definidas
- descarga gasto público **filtrado por glosa**

---

### 🐍 `querymaker_todos_los_programas_estatales.py`

Script que descarga:
- **todos los programas estatales disponibles**
- sin aplicar reglas del lookup

Se utiliza como:
- insumo base
- validación
- referencia comparativa

---

## 🔹 3. Datos descargados

### 📄 `query_descargado_pagos_detallados.csv`

Archivo que contiene:
- los datos descargados desde la API
- ya filtrados y estructurados según el `lookup_table`

Es el **contenedor de datos principal** para el análisis posterior.

---

## 🔹 4. Datos sectoriales y ponderaciones

### 📊 `BdD Sectoriales.xlsx`

Base de datos sectorial (MIDESO).

Contiene:
- clasificaciones sectoriales
- definiciones de áreas y subcategorías
- **ponderaciones** usadas para distribuir gasto entre categorías

---

### 📄 `programas_asignaciones_codigos.csv`

Archivo auxiliar con:
- todos los programas estatales, por ministerios de interes
- apoyo para normalización y cruces entre fuentes
- posibilidad de expandir lookup table.

---

## 📁 Eje MIDESO: Inversión en biodiversidad

`mideso/` contiene planillas anuales para estimar inversión en biodiversidad desde registros MIDESO. Se filtran iniciativas por sectores y palabras clave relevantes, se normalizan instituciones y partidas, y se ajustan montos (2020–2025) para análisis temporal reproducible.


---


## 🔹 5. Procesamiento y análisis final

### 📓 `calculo_glosa_final.ipynb`

Notebook final del pipeline.

Aquí se realiza:
- calculo de gastos mideso
- filtrado fino del gasto descargado
- matching con la BdD sectorial
- aplicación de **ponderaciones**
- cálculo de gasto ponderado
- generación de gráficos y resultados finales

Este notebook **consume todo lo anterior** y produce los graficos.

---

## 🔹 6. Scripts auxiliares y entorno

### 🛠️ `setup_venv.sh`

Script Bash que:
- crea un entorno virtual local (`.venv`)
- instala dependencias desde `requirements.txt`
- modifica automáticamente los **shebangs** de los scripts Python
  para usar el Python del entorno virtual

---

### 📦 `requirements.txt`
Lista de dependencias Python necesarias para:
- scripts de descarga
- procesamiento
- notebook de análisis

---

## 🔁 Resumen del pipeline analítico

1. Definición de reglas (`lookup_table`)
2. Construcción de queries y descarga de datos
3. Consolidación de gasto descargado
4. Integración de BdD sectorial (MIDESO)
5. Aplicación de ponderaciones
6. Análisis y visualización final

---

