import geopandas as gpd

# Step 1: Load your full shapefile
gdf = gpd.read_file("data/tl_2024_us_county.shp")

# Step 2: Filter to Corn Belt states
cornbelt_states = ['17', '18', '19', '20', '27', '31']  # IL, IN, IA, KS, MN, NE
cornbelt_gdf = gdf[gdf["STATEFP"].isin(cornbelt_states)]

# Step 3: Save to a new shapefile
cornbelt_gdf.to_file("data/cornbelt_counties.shp")