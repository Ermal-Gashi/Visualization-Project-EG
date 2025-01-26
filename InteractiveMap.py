import geopandas as gpd
import matplotlib.pyplot as plt
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')  # Switch backend to TkAgg
 
 
import geopandas as gpd
import folium
from folium import LayerControl
from folium.features import GeoJson, GeoJsonTooltip
import seaborn as sns

# File paths
geojson_with_clusters_path = r"C:\Users\ermal\Desktop\VIzualiztion project\geojson_with_property_clusters.geojson"
output_map_path = r"C:\Users\ermal\Desktop\VIzualiztion project\interactive_map_with_clusters_and_layers.html"

# Load GeoJSON with clusters
geo_data = gpd.read_file(geojson_with_clusters_path)

# Initialize Folium map
m = folium.Map(location=[20, 0], zoom_start=2, tiles="cartodbpositron")

# Function to add choropleth layers dynamically
def add_choropleth(map_obj, geo_data, column, name, fill_color):
    folium.Choropleth(
        geo_data=geo_data,
        name=name,
        data=geo_data,
        columns=["ADMIN", column],
        key_on="feature.properties.ADMIN",
        fill_color=fill_color,
        fill_opacity=0.7,
        line_opacity=0.4,
        legend_name=f"{name} (in respective units)"
    ).add_to(map_obj)

# Add choropleth layers for GDP, CPI, FDI, and Unemployment
add_choropleth(m, geo_data, "GDP", "GDP", "YlGnBu")
add_choropleth(m, geo_data, "CPI", "CPI", "OrRd")
add_choropleth(m, geo_data, "FDI", "FDI", "PuRd")
add_choropleth(m, geo_data, "Unemployment", "Unemployment", "YlOrBr")

# Add cluster layers dynamically with distinct colors
cluster_columns = ["GDP_Cluster", "CPI_Cluster", "FDI_Cluster", "Unemployment_Cluster"]
for cluster_col in cluster_columns:
    # Generate cluster colors dynamically
    num_clusters = geo_data[cluster_col].nunique()
    cluster_colors = sns.color_palette("Set2", n_colors=num_clusters).as_hex()

    # Add GeoJson layer for each cluster
    folium.GeoJson(
        geo_data,
        style_function=lambda feature, cluster_col=cluster_col: {
            "fillColor": cluster_colors[feature["properties"][cluster_col]],
            "color": "black",
            "weight": 1,
            "fillOpacity": 0.6,
        },
        tooltip=GeoJsonTooltip(
            fields=["ADMIN", cluster_col, "GDP", "CPI", "FDI", "Unemployment"],
            aliases=[
                "Country:",
                f"{cluster_col}:",
                "GDP:",
                "CPI:",
                "FDI:",
                "Unemployment:"
            ],
            localize=True
        ),
        name=f"{cluster_col} Clusters"
    ).add_to(m)

# Add layer control to toggle between metric layers and clusters
LayerControl().add_to(m)

# Save the map
m.save(output_map_path)
print(f"Interactive map with clusters and layers saved to: {output_map_path}")
