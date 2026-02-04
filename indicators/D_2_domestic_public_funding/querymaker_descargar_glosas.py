#!/home/biodata-lab/Documents/7nr/gasto_publico/entregable_daniel/.venv/bin/python
import time
import json
import requests
import pandas as pd

# =============================
# CONFIG
# =============================

BASE_URL = "https://api.presupuestoabierto.gob.cl/api/v1/data/pagos.json"
years = range(2020, 2026)

MAX_RETRIES = 5
RETRY_SLEEP = 2

coord_cols = [
    "partida",
    "capitulo",
    "codigo_programa_presupuestario",
    "area",
    "subtitulo",
    "item",
    "asignacion",
]

final_criterios = [
    "codigo_programa_presupuestario",
    "nombre_programa_presupuestario",
    "periodo",
    "partida",
    "capitulo",
    "subtitulo",
    "item",
    "asignacion",
    "nombre_partida",
    "nombre_capitulo",
    "nombre_subtitulo",
    "nombre_item",
    "nombre_asignacion",
]

# =============================
# INPUT
# =============================

df = pd.read_csv("lookup_table_glosas_querybuild.csv")

# =============================
# SESSION
# =============================

s = requests.Session()

# =============================
# BUILD URL TASKS
# =============================

tasks = []

for _, row in df.iterrows():

    is_gc = str(row.get("String_name", "")).upper() == "GASTO CORRIENTE"

    # ---------- CASO A: GASTO CORRIENTE ----------
    if is_gc:
        base_cols = [
            "partida",
            "capitulo",
            "codigo_programa_presupuestario",
            "area",
        ]

        base = row[base_cols].dropna().to_dict()
        base = {k: int(v) for k, v in base.items()}

        for y in years:
            for st in (21, 22, 29):
                coord = base.copy()
                coord["periodo"] = y
                coord["subtitulo"] = st

                params = {
                    "where": json.dumps(coord),
                    "group-by": json.dumps(final_criterios),
                }

                req = requests.Request("GET", BASE_URL, params=params)
                prep = s.prepare_request(req)
                tasks.append(prep.url)

    # ---------- CASO B: NO GASTO CORRIENTE ----------
    else:
        base = row[coord_cols].dropna().to_dict()
        base = {k: int(v) for k, v in base.items()}

        for y in years:
            coord = base.copy()
            coord["periodo"] = y

            params = {
                "where": json.dumps(coord),
                "group-by": json.dumps(final_criterios),
            }

            req = requests.Request("GET", BASE_URL, params=params)
            prep = s.prepare_request(req)
            tasks.append(prep.url)

print(f"🧠 urls generadas: {len(tasks):,}")

# =============================
# EXECUTE
# =============================

dfs = []
failed = []

t_all = time.time()

for i, url in enumerate(tasks, 1):
    ok = False

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            t0 = time.time()
            r = s.get(url, timeout=120)
            r.raise_for_status()

            df_data = pd.DataFrame(r.json())
            if len(df_data.index) > 0:
                dfs.append(df_data)

            print(f"✅ {i}/{len(tasks)} intento {attempt} ({time.time()-t0:.1f}s)")
            ok = True
            break

        except Exception as e:
            print(f"⚠️ {i}/{len(tasks)} intento {attempt} falló: {e}")
            time.sleep(RETRY_SLEEP)

    if not ok:
        failed.append(url)

# =============================
# MERGE FINAL
# =============================

if dfs:
    pd.concat(dfs, ignore_index=True).to_csv("query_descargado_pagos_detallados.csv", index=False)

print(f"⏱ total {(time.time()-t_all)/60:.1f} min")
print(f"❌ fallidas {len(failed)}")

