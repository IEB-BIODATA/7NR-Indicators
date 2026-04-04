import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import geopandas as gpd
import pandas as pd
import tqdm
import traceback


def save_layer(filename, tablename, conn):
    print(f"Reading {filename}")
    data = gpd.read_file(f"zip://data/{filename}.zip")
    print(f"Saving")
    data.to_postgis(
        tablename, conn, schema="processed", if_exists="append"
    )


if __name__ == "__main__":
    load_dotenv("../local.env")

    connection_string = "postgresql://{user}:{password}@localhost:5432/{dbname}".format(
        dbname=os.environ.get("SEVENNR_DB_NAME"),
        user=os.environ.get("SEVENNR_DB_USER"),
        password=os.environ.get("SEVENNR_DB_PASSWORD"),
    )

    engine = create_engine(connection_string)

    for file_name, table_name in [
        ("EcosistemasMarinos_shapefile_202405250421", "ecorregiones"),
        ("PisosPotenciales2017_shapefile_202410180400", "pisos_vegetacionales")
    ]:
        save_layer(file_name, table_name, engine)
