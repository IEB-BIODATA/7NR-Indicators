import io
import os
import tqdm
import requests
import zipfile
import geopandas as gpd
import pandas as pd
from sqlalchemy import create_engine
from pyproj import Geod


CRS = "EPSG:32719"

connection_string = "postgresql://{user}:{password}@localhost:5432/{dbname}".format(
    dbname=os.environ.get("SEVENNR_DB_NAME"),
    user=os.environ.get("SEVENNR_DB_USER"),
    password=os.environ.get("SEVENNR_DB_PASSWORD"),
)

ECOSISTEMAS_MARINOS_URL = 'https://lineasdebasepublicas.mma.gob.cl/datos_abiertos/dataset/c144e690-f266-49a9-bb74-a85214a95164/resource/99283f8c-3d6b-4b14-aa82-4d859ad1fece/download/ecosistemas-marinos_geojson.zip'
DOWNLOAD_DIR = "data/ecoistemas_marinos"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

response = requests.get(ECOSISTEMAS_MARINOS_URL)
response.raise_for_status()

eco_mar_zip = zipfile.ZipFile(io.BytesIO(response.content))
eco_mar_zip.extractall(DOWNLOAD_DIR)
eco_mar_zip.close()

geo_file = ""
for file in os.listdir(DOWNLOAD_DIR):
    name, ext = os.path.splitext(file)
    if ext == ".geojson":
        geo_file = file
if geo_file == "": print("No geojson in download")

mar_raw = gpd.read_file(os.path.join(DOWNLOAD_DIR, geo_file))
mar = mar_raw.to_crs(CRS)
del mar_raw

mar_union = mar.geometry.union_all()
print(f"Original area {mar_union.area / 10000:.2f}")

for region in tqdm.tqdm(os.listdir("data/shp")):
    if region == ".DS_Store":
        continue
    try:
        tmp_raw = gpd.read_file(f"data/shp/{region}")
        tmp = tmp_raw.to_crs(mar.crs)
        del tmp_raw
        tmp_union = tmp.geometry.union_all()
        if tmp_union.intersects(mar_union):
            print(f"Intersection with {region} exists")
            result = mar_union.difference(tmp_union)
            print(f"New area {result.area / 10000:.2f}")
            del mar_union
            mar_union = result
            del result
        else:
            print(f"No intersection with {region} exists")
        del tmp_union, tmp
    except Exception as e:
        raise e

geod = Geod(ellps="WGS84")

marine_gdf = gdf.GeoDataFrame(geometry=[mar_union], crs=CRS)

marine_gdf["superf_ha"] = mar_union.area / 10000
marine_gdf["geod_superf_ha"] = geod.geometry_area_perimeter(mar_union) / 10000

engine = create_engine(connection_string)

marine_gdf.to_postgis("marino", engine, if_exists="replace", schema="processed")
