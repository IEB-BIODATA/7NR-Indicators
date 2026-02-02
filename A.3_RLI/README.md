---
# === Indicador(s) ===
indicator:
  code: "<codigo>"                              # ej: IND-01
  name: "<nombre indicador>"
  objective: "<qué mide y por qué importa>"
  unit: "<unidad>"                              # ej: %, ha, km2, n°
  formula_summary: "Resumen legible de la fórmula (sin detalles excesivos)."
  methodology_ref: "<doc_url o nombre doc>"     # referencia a metodología formal
  assumptions:
    - "<supuesto 1>"
    - "<supuesto 2>"
  limitations:
    - "<limitación 1>"

# === Entradas de datos ===
inputs:
  sources:
    - name: "<fuente>"
      type: "wms/wfs/api/csv/shp/geopackage/db"
      uri: "<url/tabla/ruta>"
      owner: "<institución>"
      license: "<licencia>"
      access: "public"                          # public | internal | restricted
      refresh: "mensual"
      expected_schema: "<link o descripción>"
  temporal_coverage:
    start: "YYYY-MM-DD"
    end: "YYYY-MM-DD"
  spatial_coverage:
    crs: "EPSG:4326"
    extent: "<bbox o descripción>"
  preprocessing:
    - "Validación geometrías (make_valid)"
    - "Filtro por atributo X"

# === Fechas clave ===
dates:
  created_at: "2026-01-31"
  last_modified_at: "2026-01-31"
  last_run_at: "2026-01-31 09:00"               # última ejecución completa exitosa
  last_result_published_at: "YYYY-MM-DD"        # si se publica a dashboard/reporte

# === Responsables y revisión ===
people:
  developer:
    name: "Daniel Ortiz"
    role: "Desarrollador"
    org: "IEB"
    contact: "daniel.ortiz@ieb-chile.cl"
  technical_reviewer:
    name: "Nicole Burger"
    role: "Investigadora revisora del cálculo"
    org: "nburger@ieb-chile.cl"

# === Salidas / productos ===
outputs:
  datasets:
    - name: "<nombre tabla o archivo>"
      type: "postgis-table"                     # postgis-table | parquet | geojson | csv | report
      uri: "<schema.tabla / ruta / url>"
      schema_ref: "<link o notas>"
  artifacts:
    - type: "figure"
      uri: "<ruta/figura.png>"
    - type: "report"
      uri: "<ruta/reporte.pdf>"
  publication:
    dashboard: "<url/opcional>"
    last_published_version: "<vX.Y>"

## Ejecución rápida
- **Cómo correr:** `python script.py --param ...` o “Run All” en notebook
- **Tiempo estimado:** <opcional>
- **Salida principal:** `<uri output principal>`

## Notas
Cualquier observación operacional: credenciales, endpoints inestables, límites de API, etc.
