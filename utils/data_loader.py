import geopandas as gpd
import pandas as pd

def load_county_data(path):
    gdf = gpd.read_file(path)
    cornbelt_fips = ['19', '17', '31', '20', '18', '27']  # IA, IL, NE, KS, IN, MN
    return gdf[gdf['STATEFP'].isin(cornbelt_fips)]

def load_ndvi_csv(path):
    df = pd.read_csv(path)
    df = df[df["value"] < 9999]  # remove fill values
    if df["value"].max() > 1.0:
        df["value"] = df["value"] / 1000  # scale if necessary
    return df