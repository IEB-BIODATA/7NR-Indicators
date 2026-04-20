import os
from pyproj import Geod
from sqlalchemy import create_engine
from dotenv import load_dotenv
import geopandas as gpd
import pandas as pd
import tqdm

CRS = "EPSG:4326"


def process(name, conn, geod, progress_bar):
    progress_bar.set_description(f"Working with {name}")
    progress_bar.set_postfix_str("Reading")
    raw_data = gpd.read_file(f"zip://data/efg/EFG {name}.zip")
    raw_data = raw_data.to_crs(CRS)
    progress_bar.set_postfix_str("Dissolving")
    processed = raw_data.dissolve(by="Group_", as_index=False)
    progress_bar.set_postfix_str("Processing")
    processed.drop(columns=processed.columns.difference(["Group_", "geometry"]), inplace=True)
    processed.rename(columns={"Group_": "group"}, inplace=True)
    progress_bar.set_postfix_str("Saving")
    processed["superf_ha"] = abs(processed.geometry.apply(
        lambda x:geod.geometry_area_perimeter(x)[0]
    ) / 10000)
    processed.to_postgis(f"efg_{name}", conn, if_exists="replace", schema="processed")
    progress_bar.update(1)


if __name__ == '__main__':
    load_dotenv("../local.env")

    connection_string = "postgresql://{user}:{password}@localhost:5432/{dbname}".format(
        dbname=os.environ.get("SEVENNR_DB_NAME"),
        user=os.environ.get("SEVENNR_DB_USER"),
        password=os.environ.get("SEVENNR_DB_PASSWORD"),
    )

    engine = create_engine(connection_string)

    continental = gpd.read_file("zip://data/efg/EFG continental.zip")
    marino = gpd.read_file("zip://data/efg/EFG marino.zip")
    progress = tqdm.tqdm(total=2)

    geod = Geod(ellps="WGS84")

    with engine.connect() as conn:
        process("continental", conn, geod, progress)
        process("marino", conn, geod, progress)

    progress.close()
