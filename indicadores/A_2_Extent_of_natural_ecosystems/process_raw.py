import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import geopandas as gpd
import pandas as pd
import tqdm
import traceback

load_dotenv("../local.env")

raw_files_done = list()

with open("raw_files_done.txt", "r", encoding="utf-8") as file:
    raw_files_done = file.read().split("\n")

columns_to_keep = [
    "ID", "ORIGINAL_ID", "ID_USO", "ID_SUBUSO",
    "CODREG", "CODPROV", "CODCOM",
    "USO_TIERRA", "USO", "SUBUSO",
    "ESTRUCTURA", "NOM_REG",
    "NOM_PROV", "NOM_COM",
    "ID_FILE", "FILE",
    "SUPERF_HA", "geometry"
]

columns_no_geometry = columns_to_keep.copy()
columns_no_geometry.remove("geometry")

csv_folder = "data/tables"
os.makedirs(csv_folder, exist_ok=True)

connection_string = "postgresql://{user}:{password}@localhost:5432/{dbname}".format(
    dbname=os.environ.get("SEVENNR_DB_NAME"),
    user=os.environ.get("SEVENNR_DB_USER"),
    password=os.environ.get("SEVENNR_DB_PASSWORD"),
)

engine = create_engine(connection_string)

def columns_to_lower(columns):
    return [col.lower() for col in columns]


def check_unique(unique_column):
    return len(unique_column) == len(unique_column.drop_duplicates())


def get_id_file(connection):
    result = connection.execute(text("""
        SELECT id_file
        FROM processed.conaf_terrestre
        ORDER BY id_file DESC
        LIMIT 1;
    """)).first()[0]
    if result is None:
        return 1
    else:
        return result + 1

def complete_codreg(codreg, region_name):
    missing = 999
    for i in range(0, 10):
        if f"0{i}" in region_name:
            missing = i
    for i in range(11, 17):
        if f"{i}" in region_name:
            missing = i
    if missing == 999:
        print(f"Not substitute for {region_name}")
    return codreg.fillna(missing)


id_file = 1
with engine.connect() as conn:
    id_file = get_id_file(conn)


for region in tqdm.tqdm(os.listdir("data/raw")):
    region_name, ext = os.path.splitext(region)
    if ext != ".zip":
        continue
    try:
        if region_name not in raw_files_done:
            region_name, _ = os.path.splitext(region)
            try:
                tmp = gpd.read_file(f"zip://data/raw/{region}", encoding="cp1252")
            except DataSourceError:
                tmp = gpd.read_file(f"zip://data/raw/{region}/{region_name}/{region_name}.shp", encoding="cp1252")    
            tmp = tmp[tmp.geometry.notna()]
            if "ID" in tmp.columns:
                tmp["ID"] = tmp["ID"].astype("int32")
                tmp["ORIGINAL_ID"] = tmp["ID"]
                if not check_unique(tmp["ID"]):
                    print(f"ID not unique on {region_name}")
                    tmp["ID"] = range(1, len(tmp) + 1)
            else:
                print(f"Adding ID to {region_name}")
                tmp["ORIGINAL_ID"] = 999
                tmp["ID"] = range(1, len(tmp) + 1)
            if not "CODCOM" in tmp.columns:
                print(f"Adding CODCOM to {region_name}")
                tmp["CODCOM"] = 999
            else:
                tmp["CODCOM"] = tmp["CODCOM"].fillna(999)
                tmp["CODCOM"] = tmp["CODCOM"].astype("int32")
            tmp["CODREG"] = complete_codreg(tmp["CODREG"], region_name)
            tmp["CODREG"] = tmp["CODREG"].astype("int32")
            tmp["ID_FILE"] = id_file
            tmp["FILE"] = region_name
            tmp = tmp.loc[:, columns_to_keep].copy().to_crs("EPSG:32719")
            tmp["geometry"] = tmp["geometry"].force_2d()
            outdir = f"data/shp/{region_name}"
            os.makedirs(outdir, exist_ok=True)
            tmp.to_file(f"{outdir}/{region_name}.shp")
            pd.DataFrame(tmp[columns_no_geometry]).to_csv(f"{csv_folder}/{region_name}.csv", header=True, index=False)
            tmp.columns = columns_to_lower(tmp.columns)
            tmp.drop(columns=["nom_reg"], inplace=True)
            tmp.to_postgis("conaf_terrestre", engine, schema="processed", if_exists="append")
            del tmp
            raw_files_done.append(region_name)
            id_file += 1
        else:
            print(f"'{region_name}' already saved")
    except Exception as e:
        print(region)
        print(traceback.format_exc())
        break

with open("raw_files_done.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(raw_files_done))
