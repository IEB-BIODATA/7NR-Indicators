import os
from pyproj import Geod
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import geopandas as gpd
import pandas as pd
import tqdm
import traceback
import matplotlib.pyplot as plt
from psycopg2.errors import ProgramLimitExceeded


CRS = "EPSG:4326"
GEOM_LIMIT = 6000

geod = Geod(ellps="WGS84")


def savefig(geometry, uso, subuso):
    fig, ax = plt.subplots(figsize=(8,8))
    tmp = gpd.GeoDataFrame(geometry=[geometry])
    tmp.plot(ax=ax)
    fig.savefig(f"maps/{uso}-{subuso}.png")
    plt.close(fig)
    return


if __name__ == '__main__':
    load_dotenv("../local.env")

    connection_string = "postgresql://{user}:{password}@localhost:5432/{dbname}".format(
        dbname=os.environ.get("SEVENNR_DB_NAME"),
        user=os.environ.get("SEVENNR_DB_USER"),
        password=os.environ.get("SEVENNR_DB_PASSWORD"),
    )


    engine = create_engine(connection_string)

    # sql_query = """
    # SELECT ec."group", ec."geometry"
    # FROM processed.efg_continental ec
    #     FULL OUTER JOIN processed.efg_continental_included eci
    #         ON ec."group" = eci."group"
    # WHERE eci."group" IS NULL;
    # """

    sql_query = """
    SELECT ec."group", ec."geometry"
    FROM processed.efg_continental ec;
    """

    efg_continental = gpd.read_postgis(sql_query, engine, geom_col="geometry", crs=CRS)
    efg_continental = efg_continental.to_crs(CRS)

    progress = tqdm.tqdm(total=len(efg_continental) + 1)
    progress.set_description("Reading not included")

    not_included = gpd.read_postgis("""
        SELECT ct.*
        FROM processed.conaf_terrestre ct
            JOIN processed.uso_subuso us
                ON ct.id_uso = us.id_uso AND ct.id_subuso = us.id_subuso
        WHERE NOT us.incluir
    """, engine, geom_col="geometry")
    not_included = not_included.to_crs(CRS)

    progress.set_postfix_str("Joining not included")

    not_include_geometry = not_included.geometry.union_all()
    progress.update(1)

    progress.set_postfix_str("Reading EFG")

    for idx, row in efg_continental.iterrows():
        group = row["group"]
        progress.set_description(f"EFG: {group}")
        current_geom = row.geometry
        new_geom = current_geom.difference(not_include_geometry)
        efg_continental.loc[idx, "geometry"] = new_geom
        efg_continental.loc[idx, "superf_ha"] = abs(geod.geometry_area_perimeter(efg_continental.loc[idx, ].geometry)[0] / 10000)
        del current_geom, new_geom
        progress.set_postfix_str(f"Saving")
        try:
            if efg_continental.loc[idx, ].geometry.length > GEOM_LIMIT:
                print("Limit exceeded, saving without geometry")
                tmp = pd.DataFrame([efg_continental.loc[idx, ]])
                tmp.loc[idx, "geometry"] = None
                tmp.to_sql("efg_continental_included", engine, if_exists="append", schema="processed", index=False)
                del tmp
            else:
                gpd.GeoDataFrame(
                    [efg_continental.loc[idx, ]], geometry="geometry", crs=CRS
                ).to_postgis("efg_continental_included", engine, if_exists="append", schema="processed")
        except Exception as e:
            print(f"{row['group']}:")
            print(traceback.format_exc())
        progress.update(1)
    efg_continental.to_file("data/shp/efg_continental_included/efg_continental_included.shp")
    progress.close()
