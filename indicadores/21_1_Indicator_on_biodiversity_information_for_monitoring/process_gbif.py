import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
import geopandas as gpd
import pandas as pd
from shapely.geometry import Point


if __name__ == "__main__":
    load_dotenv("../local.env")
    connection_string = "postgresql://{user}:{password}@localhost:5432/{dbname}".format(
        dbname=os.environ.get("SEVENNR_DB_NAME"),
        user=os.environ.get("SEVENNR_DB_USER"),
        password=os.environ.get("SEVENNR_DB_PASSWORD"),
    )
    engine = create_engine(connection_string)

    read_data = list()
    columns = [0, 21, 97, 98, 140, 141]
    with open("data/0032037-260208012135463/occurrence.txt", "r", encoding="utf-8") as file:
        header_line = file.readline().strip("\n")
        column_names = [header_line.split("\t")[i] for i in columns]
        line = file.readline().strip("\n")
        j = 1
        while line != "":
            if j % 100 == 0:
                print(j, end="\r")
            cells = line.split("\t")
            read_data.append([cells[i] for i in columns])
            j += 1
            line = file.readline().strip("\n")
        print(j)
    data = pd.DataFrame(read_data, columns=column_names)
    geometry = [Point(xy) for xy in zip(data['decimalLongitude'], data['decimalLatitude'])]
    gdf = gpd.GeoDataFrame(data, geometry=geometry, crs="EPSG:4326") # WGS84
    gdf = gdf.to_crs("EPSG:32719")
    gdf.to_postgis("gbif_occurrences", engine, schema="processed", if_exists="append")
