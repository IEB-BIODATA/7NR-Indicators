# Metadata — Indicador y Cálculo

---

## 1) Indicador

| Campo | Valor |
|---|---|
| **Código** | `<codigo>` *(ej: IND-01)* |
| **Nombre** | `<nombre indicador>` |
| **Objetivo** | `<qué mide y por qué importa>` |
| **Unidad** | `<unidad>` *(ej: %, ha, km², n°)* |
| **Resumen de fórmula** | Resumen legible de la fórmula (sin detalles excesivos). |
| **Referencia metodología** | `<doc_url o nombre doc>` |

**Supuestos**
- `<supuesto 1>`
- `<supuesto 2>`

**Limitaciones**
- `<limitación 1>`

---

## 2) Entradas de datos

### 2.1 Fuentes

| Fuente | Tipo | URI / Tabla / Ruta | Dueño | Licencia | Acceso | Refresh | Esquema esperado |
|---|---|---|---|---|---|---|---|
| `<fuente>` | `wms/wfs/api/csv/shp/geopackage/db` | `<url/tabla/ruta>` | `<institución>` | `<licencia>` | `public` | `mensual` | `<link o descripción>` |

### 2.2 Cobertura

| Campo | Valor |
|---|---|
| **Cobertura temporal (inicio)** | `YYYY-MM-DD` |
| **Cobertura temporal (fin)** | `YYYY-MM-DD` |
| **Cobertura espacial (CRS)** | `EPSG:4326` |
| **Extensión** | `<bbox o descripción>` |

### 2.3 Preprocesamiento

- Validación geometrías (`make_valid`)
- Filtro por atributo X

---

## 3) Fechas clave

| Campo | Valor |
|---|---|
| **Creación** | `2026-01-31` |
| **Última modificación** | `2026-01-31` |
| **Última ejecución exitosa** | `2026-01-31 09:00` |
| **Última publicación de resultados** | `YYYY-MM-DD` |

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
