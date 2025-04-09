import geopandas as gpd
import pandas as pd
import streamlit as st


@st.cache_data
def load_county_data(path):
    gdf = gpd.read_file(path)
    cornbelt_fips = ['19', '17', '31', '20', '18', '27']  # IA, IL, NE, KS, IN, MN
    return gdf[gdf['STATEFP'].isin(cornbelt_fips)]

@st.cache_data
def load_ndvi_csv(path):
    df = pd.read_csv(path, usecols=["County_FIPS", "Mean_NDVI"])  # no .geo!
    df = df.rename(columns={"County_FIPS": "GEOID", "Mean_NDVI": "NDVI"})
    df["GEOID"] = df["GEOID"].astype(str).str.zfill(5)
    return df