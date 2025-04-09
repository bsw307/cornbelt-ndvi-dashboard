import streamlit as st
import folium
from streamlit_folium import st_folium

from utils.data_loader import load_county_data, load_ndvi_csv

# Hide Streamlit UI
st.markdown("""
    <style>
    #MainMenu, header, footer, .stDeployButton, .st-emotion-cache-1avcm0n {
        display: none !important;
    }
    .block-container {
        padding: 0 !important;
    }
    body {
        overflow: hidden;
    }
    </style>
""", unsafe_allow_html=True)

# Load shapefile and NDVI CSV from Google Earth Engine
counties = load_county_data("data/cornbelt_counties.shp")
ndvi_df = load_ndvi_csv("data/CornBelt_S2_NDVI_FebMar2025.csv")

# Merge NDVI values directly with county polygons using GEOID
gdf = counties.merge(ndvi_df, on="GEOID", how="left")

# Create Folium map
m = folium.Map(location=[41.5, -93.5], zoom_start=5)

folium.Choropleth(
    geo_data=gdf,
    data=gdf,
    columns=["GEOID", "NDVI"],
    key_on="feature.properties.GEOID",
    fill_color="YlGn",
    fill_opacity=0.9,
    line_opacity=0.3,
    line_color='white',
    legend_name="NDVI (March 2025)"
).add_to(m)

# Optional: Add hover tooltips
folium.GeoJson(
    gdf,
    tooltip=folium.GeoJsonTooltip(
        fields=["NAME", "NDVI"],
        aliases=["County", "NDVI"],
        localize=True
    )
).add_to(m)

# Display map
st_folium(m, width=700, height=500)