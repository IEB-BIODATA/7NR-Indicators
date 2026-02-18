# Metadata — Indicador y Cálculo

---

## 1) Indicador

| Campo | Valor |
|---|---|
| **Código** | D.1.ipynbit status
 |
| **Nombre** | D.1 International public funding, including official development assistance (ODA), for conservation and sustainable use of biodiversity, and ecosystems |
| **Objetivo** | Mide el aporte oficial internacional etiquetado como financiamiento para el desarrollos sostenible metas 14 y 15 y/o con las palabras "Biodiversity" y/o "Biosphere protection" en la descripción.|
| **Unidad** | US$ |
| **Resumen de fórmula** | Es la suma de los gastos oficiales reembolsados a Chile en las plataformas OCDE y TOSSD. Los valores TOSSD tienen una ponderación de *1 cuando se selecciona por cumplir con objetivos ODS y 0.4 si se selecciona por palabras claves en la descripción. |
| **Referencia metodología** | `https://www.cbd.int/doc/c/80af/1256/4f0e7bc3a3263b61bc9c5093/cop-16-inf-03-en.pdf` |

**Supuestos**
- Los datos han sido reportados a TOSSD

**Limitaciones**
- La plataforma OCDE no registra datos para Chile posterior a 2015
- La plataforma TOSSD sólo registra datos para 2021-2022.2023

---

## 2) Entradas de datos

### 2.1 Fuentes

| Fuente | Tipo | URI / Tabla / Ruta | Dueño | Licencia | Acceso | Refresh | Esquema esperado |
|---|---|---|---|---|---|---|---|
| TOSSD | Planilla filtrada | `https://tossd.online/app` | TOSSD | `<licencia>` | `public` | Anual | `<link o descripción>` |

### 2.2 Cobertura

| Campo | Valor |
|---|---|
| **Cobertura temporal (inicio)** | `2021-01-01` |
| **Cobertura temporal (fin)** | `2023-12-31` |
| **Cobertura espacial (CRS)** | `EPSG:4326` |
| **Extensión** | `<bbox o descripción>` |

### 2.3 Preprocesamiento

- Validación geometrías (`make_valid`)
- Filtro por atributo Objetivo Desarrollo sostenible y Descripción

---

## 3) Fechas clave

| Campo | Valor |
|---|---|
| **Creación** | `2026-02-02` |
| **Última modificación** | `2026-002-02` |
| **Última ejecución exitosa** | `2026-02-02 09:00` |
| **Última publicación de resultados** | `YYYY-MM-DD` |

---

## 4) Responsables y revisión

| Rol | Nombre | Organización | Contacto |
|---|---|---|---|
| **Revisión técnica (cálculo)** | Ricardo Segovia | IEB | rsegovia@ieb-chile.cl |

---

## 5) Salidas / productos

### 5.1 Datasets

| Nombre | Tipo | URI / Ubicación | Referencia de esquema |
|---|---|---|---|
| data_biodiversity.csv | tabla filtrada | `./D_1_international_public_funding/data_biodiversity.csv` | `<link o notas>` |

### 5.2 Artefactos

| Tipo | URI |
|---|---|
| `figure` | `<ruta/figura.png>` |
| `report` | `<ruta/reporte.pdf>` |

### 5.3 Publicación

| Campo | Valor |
|---|---|
| **Dashboard** | `<url/opcional>` |
| **Versión publicada** | `<vX.Y>` |

---

## 6) Ejecución rápida

- **Cómo correr:** `python script.py --param ...` o “Run All” en notebook
- **Tiempo estimado:** `<opcional>`
- **Salida principal:** `<uri output principal>`

---

## 7) Notas

Cualquier observación operacional: credenciales, endpoints inestables, límites de API, etc.
