import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib

# Use TkAgg backend for Matplotlib
matplotlib.use('TkAgg')



import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib

# Use TkAgg backend for Matplotlib
matplotlib.use('TkAgg')

# File path for the GeoJSON
geojson_path = r"C:\Users\ermal\Desktop\VIzualiztion project\updated_geojson_with_corrected_cpi.geojson"

# Load the GeoJSON file
geo_data = gpd.read_file(geojson_path)

# Function to plot a given property
def plot_property(geo_data, column, title, cmap="YlGnBu"):
    plt.figure(figsize=(15, 10))
    geo_data.plot(
        column=column,
        cmap=cmap,
        legend=True,
        edgecolor="black"
    )
    plt.title(title, fontsize=16)
    plt.axis('off')
    plt.show()

# Plot GDP
#plot_property(geo_data, "GDP", "World Map: GDP Visualization")

# Plot CPI
plot_property(geo_data, "CPI", "World Map: CPI Visualization")

# Plot FDI
plot_property(geo_data, "FDI", "World Map: FDI Visualization")

# Plot Unemployment
plot_property(geo_data, "Unemployment", "World Map: Unemployment Visualization")

