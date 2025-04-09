import geopandas as gpd
from shapely.geometry import Point
import pandas as pd
import streamlit as st


def ndvi_csv_to_geodf(ndvi_df):
    geometry = [Point(xy) for xy in zip(ndvi_df.longitude, ndvi_df.latitude)]
    return gpd.GeoDataFrame(ndvi_df, geometry=geometry, crs="EPSG:4326")

@st.cache_data
def map_ndvi_to_counties(ndvi_gdf, counties_gdf):
    ndvi_gdf = ndvi_gdf.to_crs(counties_gdf.crs)
    joined = gpd.sjoin(ndvi_gdf, counties_gdf, how="inner", predicate="within")
    grouped = joined.groupby("GEOID")["value"].mean().reset_index()
    grouped.rename(columns={"value": "NDVI"}, inplace=True)
    return counties_gdf.merge(grouped, on="GEOID", how="left")