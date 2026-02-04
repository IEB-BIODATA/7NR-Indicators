# Metadata — Indicador y Cálculo

---

## 1) Indicador

| Campo | Valor |
|---|---|
| **Código** | D.2 |
| **Nombre** | Domestic public funding on conservation and
sustainable use of biodiversity and ecosystems |
| **Objetivo** | Gasto público en biodiversidad |
| **Unidad** | Miles de millones de pesos (anualizados) |
| **Resumen de fórmula** | Suma de los gastos sectoriales en partidas que tengan relación validada con biodiversidad. |
| **Referencia metodología** | `<doc_url o nombre doc>` |

**Supuestos**
- `<supuesto 1>`
- `<supuesto 2>`

**Limitaciones**
- Diferencias con consultoría previa. El cálculo actual consulta vía API a Dipres, lo que le da robustez y reproducibilidad. Revisar hoja de glosas con autoridad competente.

---

## 2) Entradas de datos

### 2.1 Fuentes

| Fuente | Tipo | URI / Tabla / Ruta | Dueño | Licencia | Acceso | Refresh | Esquema esperado |
|---|---|---|---|---|---|---|---|
| API Dipres y plataforma BIP de MIDESO | `wms/wfs/api/csv/shp/geopackage/db` | `<url/tabla/ruta>` | `<institución>` | `<licencia>` | `public` | `mensual` | `<link o descripción>` |

### 2.2 Cobertura

| Campo | Valor |
|---|---|
| **Cobertura temporal (inicio)** | 2020 |
| **Cobertura temporal (fin)** | 2025 |
| **Cobertura espacial (CRS)** | `EPSG:4326` |
| **Extensión** | `<bbox o descripción>` |

### 2.3 Preprocesamiento

- Revisar flujo,md

---

## 3) Fechas clave

| Campo | Valor |
|---|---|
| **Creación** | `2026-02-02` |
| **Última modificación** | `2026-02-02` |
| **Última ejecución exitosa** | `2026-02-02` |
| **Última publicación de resultados** | `YYYY-MM-DD` |

---

## 4) Responsables y revisión

| Rol | Nombre | Organización | Contacto |
|---|---|---|---|
| **Desarrollador** | Julián Caro | IEB | julian.caro@ieb-chile.cl |
| **Revisión técnica (cálculo)** | Ricardo Segovia | IEB | rsegovia@ieb-chile.cl |

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

2026_02_02 revisar diferencias con Tepual