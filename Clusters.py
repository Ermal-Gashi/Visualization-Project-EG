import geopandas as gpd
import matplotlib.pyplot as plt
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')  # Switch backend to TkAgg

import geopandas as gpd
 

import pandas as pd
import geopandas as gpd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
 
# File paths
geojson_path = r"C:\Users\ermal\Desktop\VIzualiztion project\updated_geojson_with_corrected_cpi.geojson"
output_geojson_path = r"C:\Users\ermal\Desktop\VIzualiztion project\geojson_with_property_clusters.geojson"

# Load GeoJSON data
geo_data = gpd.read_file(geojson_path)

# List of properties to cluster
properties = ["GDP", "CPI", "FDI", "Unemployment"]

# For each property, create clusters
for prop in properties:
    # Check if the property exists in the data
    if prop in geo_data.columns:
        # Normalize the property
        scaler = StandardScaler()
        normalized_values = scaler.fit_transform(geo_data[[prop]].fillna(0))  # Fill NaN with 0 for clustering

        # Apply KMeans clustering
        kmeans = KMeans(n_clusters=5, random_state=42)
        geo_data[f"{prop}_Cluster"] = kmeans.fit_predict(normalized_values)
    else:
        print(f"Property '{prop}' not found in the GeoJSON data.")

# Save the updated GeoJSON with cluster information
geo_data.to_file(output_geojson_path, driver="GeoJSON")
print(f"Clusters for each property added and saved to: {output_geojson_path}")
