import geopandas as gpd

gdf = gpd.read_file("data/tl_2024_us_county.shp")

cornbelt_states = ['19', '17', '31', '20', '18', '27']  # FIPS codes for IA, IL, NE, KS, IN, MN
gdf = gdf[gdf['STATEFP'].isin(cornbelt_states)]

print(gdf[['GEOID', 'NAME', 'STATEFP', 'geometry']].head()
)