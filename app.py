import streamlit as st
import folium
from streamlit_folium import st_folium

from utils.data_loader import load_county_data, load_ndvi_csv
from utils.ndvi_mapper import ndvi_csv_to_geodf, map_ndvi_to_counties

# Load data
counties = load_county_data("data/cornbelt_counties.shp")
ndvi_df = load_ndvi_csv("data/ndvi_sample.csv")
ndvi_points = ndvi_csv_to_geodf(ndvi_df)
gdf = map_ndvi_to_counties(ndvi_points, counties)

# Create map
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
    legend_name="NDVI"
).add_to(m)

# Display map
st.title("Corn Belt NDVI Map")
st_data = st_folium(m, width=700, height=500)