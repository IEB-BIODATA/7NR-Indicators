#!/home/biodata-lab/Documents/7nr/gasto_publico/entregable_daniel/.venv/bin/python

import time
import json
import requests
import pandas as pd

min2partida = {
  "MINISTERIO DE DESARROLLO SOCIAL Y FAMILIA": 21,
  "MINISTERIO DE AGRICULTURA": 13,
  "MINISTERIO DE BIENES NACIONALES": 14,
  "MINISTERIO DE CIENCIAS Y TECNOLOGÍA": 30,
  "MINISTERIO DE CULTURA Y PATRIMONIO": 29,
  "MINISTERIO DE DEFENSA": 11,
  "MINISTERIO DE ECONOMÍA": 7,
  "MINISTERIO DE EDUCACIÓN": 9,
  "MINISTERIO DE ENERGÍA": 24,
  "MINISTERIO DEL MEDIO AMBIENTE": 25,
  "MINISTERIO DE MINERÍA": 17,
  "MINISTERIO DE OBRAS PÚBLICAS": 12,
  "MINISTERIO DE VIVIENDA Y URBANISMO": 18,
  "MINISTERIO DE RELACIONES EXTERIORES": 6,
  "MINISTERIO DEL INTERIOR Y SEGURIDAD PÚBLICA": 5
}
criterios = [
    "periodo",
    "partida",
    "capitulo",
    "area",
    "subtitulo",
    "item",
    "asignacion"
]

final_criterios = ["codigo_programa_presupuestario","nombre_programa_presupuestario"] +criterios + [f"nombre_{c}" for c in criterios if c != "periodo"]
years=range(2020, 2026)
partida_code=list(min2partida.values())
tasks = [(y, p) for y in years for p in partida_code]

BASE_URL = "https://api.presupuestoabierto.gob.cl/api/v1/data/pagos.json"
s = requests.Session()

t_all = time.time()
dfs = []
failed = []

MAX_RETRIES = 3
RETRY_SLEEP = 2  # segundos

for (y, p) in tasks:
    ok = False

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            t0 = time.time()

            params = {
                "where": json.dumps({
                    "periodo": int(y),
                    "partida": int(p),
                }),
                "group-by": json.dumps(final_criterios),
            }

            r = s.get(BASE_URL, params=params, timeout=120)
            r.raise_for_status()

            data = r.json()
            dfp = pd.DataFrame(data)

            if not dfp.empty:
                dfs.append(dfp)

            dt = time.time() - t0
            print(f"✅ {y} partida {p:02d} intento {attempt}: {len(dfp):,} filas ({dt:.1f}s)")
            ok = True
            break  # éxito → sal del retry loop

        except Exception as e:
            print(f"⚠️ {y} partida {p:02d} intento {attempt} falló: {type(e).__name__}: {e}")
            time.sleep(RETRY_SLEEP)

    if not ok:
        print(f"❌ {y} partida {p:02d}: falló tras {MAX_RETRIES} intentos")
        failed.append((y, p))



df = pd.concat(dfs, ignore_index=True)
df.to_csv("programas_asignaciones_codigos.csv")



