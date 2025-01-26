import matplotlib
matplotlib.use("TkAgg")  # Set the backend for Matplotlib
import os  # Ensure 'os' is imported
import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd

# Correct path to the GeoJSON file
geojson_path = r"C:\Users\ermal\Desktop\VIzualiztion project\countries.geojson"
combined_data_path = r"C:\Users\ermal\Desktop\VIzualiztion project\combined_data.csv"

# Verify if the GeoJSON file exists
if not os.path.exists(geojson_path):
    print("GeoJSON file not found at:", geojson_path)
else:
    print("GeoJSON file found, proceeding to load.")

    # Load the GeoJSON data
    countries = gpd.read_file(geojson_path)

    # Print the first few rows to verify the data
    print("GeoJSON Data Sample:")
    print(countries.head())

    # Plot the data to verify polygons
    countries.plot(figsize=(15, 10), edgecolor="black", color="lightblue")
    plt.title("World Country Polygons", fontsize=16)
    plt.show()

    # Load the combined macroeconomic dataset
    if not os.path.exists(combined_data_path):
        print("Combined data file not found at:", combined_data_path)
    else:
        combined_data = pd.read_csv(combined_data_path)
        print("Combined Data Sample:")
        print(combined_data.head())

        # Merge the datasets
        merged_geo_data = countries.merge(combined_data, how='left', left_on='ADMIN', right_on='Country')

        # Save the merged dataset
        merged_output_path = r"C:\Users\ermal\Desktop\VIzualiztion project\merged_data.geojson"
        merged_geo_data.to_file(merged_output_path, driver='GeoJSON')

        print(f"Merged GeoDataFrame saved at: {merged_output_path}")
