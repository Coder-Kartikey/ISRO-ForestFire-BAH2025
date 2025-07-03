# import geopandas as gpd

# # # Load the full district shapefile
# path = "C:/Users/user/OneDrive/Desktop/ISRO_ForestFire_Pipeline/ISRO-ForestFire-BAH2025/data/all_district_shapefile/2011_Dist.shp"
# gdf = gpd.read_file(path)

# # # Check available columns
# print(gdf.columns)

# # # Filter for Pauri Garhwal (case insensitive match)
# pauri_gdf = gdf[gdf['DISTRICT'].str.contains("Pauri", case=False)]

# # # Save only Pauri Garhwal as a new shapefile
# pauri_gdf.to_file("C:/Users/user/OneDrive/Desktop/ISRO_ForestFire_Pipeline/ISRO-ForestFire-BAH2025/data/all_district_shapefile/pauri_garhwal.shp")

# print("✅ Saved pauri_garhwal.shp")

# # pauri_gdf.plot()
# print(pauri_gdf.shape)
# print(pauri_gdf.geometry.head())

import geopandas as gpd

gdf = gpd.read_file("C:/Users/user/OneDrive/Desktop/ISRO_ForestFire_Pipeline/ISRO-ForestFire-BAH2025/data/all_district_shapefile/2011_Dist.shp")

# Filter rows where state name is 'Uttarakhand'
uk = gdf[gdf['ST_NM'].str.lower() == 'uttarakhand']

# Show all districts in Uttarakhand
print(uk['DISTRICT'].unique())

pauri = uk[uk['DISTRICT'] == 'Garhwal']
print(pauri.shape)
pauri.plot()

# Save if valid
if not pauri.empty:
    pauri.to_file("C:/Users/user/OneDrive/Desktop/ISRO_ForestFire_Pipeline/ISRO-ForestFire-BAH2025/data/all_district_shapefile/pauri_garhwal.shp")
    print("✅ Saved pauri_garhwal shapefile.")
else:
    print("❌ Error: Pauri Garhwal not found.")
