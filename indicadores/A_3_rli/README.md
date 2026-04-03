# Metadata — Indicador y Cálculo

---

## 1) Indicador

| Campo | Valor |
|---|---|
| **Código** | `A_3` *(ej: IND-01)* |
| **Nombre** | `A.3 Red List Index` |
| **Objetivo** | `El Red List Index mide el riesgo promedio de extinción de un conjunto de especies a partir de sus categorías UICN. Se basa en asignar un puntaje a cada categoría y calcular un índice agregado para un año dado.` |
| **Unidad** | `Index (0-1)` *(ej: %, ha, km², n°)* |
| **Resumen de fórmula** | RLIt=1−Rt/Rmax​, Rmax=N×5 Rt=∑Wi,t​ |
| **Referencia metodología** | `<doc_url o nombre doc>` |

**Supuestos**
- `La fórmula requiere que todos los años tengan el mismo número de especies para un cálculo estable de Rmax=N×5. Se sugieren 2 alternativas para evaluar. 1. Calcular con N = todas las especies de la lista (aunque su primer registro no sea el primer año) 2. Calcular con N = todas las especies de catálogo (aunque aún no tengan categoría).`
- `Las especies sin datos entran como DD = Data Deficient.`

**Limitaciones**
- `Catálogo de especies`

---

## 2) Entradas de datos

### 2.1 Fuentes

| Fuente | Tipo | URI / Tabla / Ruta | Dueño | Licencia | Acceso |
|---|---|---|---|---|---|---|---|
| `Listado de Especies Clasificadas desde el 1º al 19º Proceso de Clasificación RCE (actualizado a junio de 2025)` | `Excel` | `https://clasificacionespecies.mma.gob.cl/` | `MMA – Ministerio del Medio Ambiente` | `<licencia>` | `Público` |

### 2.2 Cobertura

| Campo | Valor |
|---|---|
| **Cobertura temporal (inicio)** | `1997-01-01` |
| **Cobertura temporal (fin)** | `2026-01-01` |
| **Cobertura espacial (CRS)** | `N/A` |
| **Extensión** | `N/A` |

### 2.3 Preprocesamiento

- 

---

## 3) Fechas clave

| Campo | Valor |
|---|---|
| **Creación** | `2026-01-31` |
| **Última modificación** | `2026-01-31` |
| **Última ejecución exitosa** | `2026-01-31` |
| **Última publicación de resultados** | `2026-02-28` |

---

## 4) Responsables y revisión

| Rol | Nombre | Organización | Contacto |
|---|---|---|---|
| **Desarrollador** | Daniel Ortiz | IEB | daniel.ortiz@ieb-chile.cl |
| **Revisión técnica (cálculo)** | Nicole Burger | IEB | nburger@ieb-chile.cl |

---

## 5) Salidas / productos

### 5.1 Datasets

| Nombre | Tipo | URI / Ubicación | Referencia de esquema |
|---|---|---|---|
| `<nombre tabla o archivo>` | `postgis-table` | `<schema.tabla / ruta / url>` | `<link o notas>` |

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
