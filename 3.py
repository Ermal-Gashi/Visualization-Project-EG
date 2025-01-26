import geopandas as gpd
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')  # Switch backend to TkAgg


import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# File paths
geojson_path = r"C:\Users\ermal\Desktop\VIzualiztion project\countries_fixed.geojson"
combined_data_path = r"C:\Users\ermal\Desktop\VIzualiztion project\combined_data.csv"
output_geojson_path = r"C:\Users\ermal\Desktop\VIzualiztion project\merged_data_final.geojson"

# Load data
geo_data = gpd.read_file(geojson_path)
combined_data = pd.read_csv(combined_data_path)

# Name mapping for mismatches
name_mapping = {
    "United States of America": "United States",
    "Russian Federation": "Russia",
    "Iran, Islamic Rep.": "Iran",
    "Yemen, Rep.": "Yemen",
    "Congo, Dem. Rep.": "Democratic Republic of the Congo",
    "Congo, Rep.": "Republic of Congo",
    "Viet Nam": "Vietnam",
    "Egypt, Arab Rep.": "Egypt",
    "Korea, Rep.": "South Korea",
    "Syrian Arab Republic": "Syria",
    "North Macedonia": "Macedonia",
    "Eswatini": "Swaziland",
    "Cote d'Ivoire": "Ivory Coast",
    "Bahamas, The": "The Bahamas",
    "Slovak Republic": "Slovakia",
    "Macao SAR, China": "Macao S.A.R",
    "Hong Kong SAR, China": "Hong Kong S.A.R.",
    "Kyrgyz Republic": "Kyrgyzstan",
    "St. Kitts and Nevis": "Saint Kitts and Nevis",
    "St. Lucia": "Saint Lucia",
    "St. Vincent and the Grenadines": "Saint Vincent and the Grenadines",
    "Timor-Leste": "East Timor",
    "Czechia": "Czech Republic",
    "Curacao": "Curaçao",
    "Guinea-Bissau": "Guinea Bissau",
    "Cabo Verde": "Cape Verde",
    "Turkey": "Turkiye",
    "Lao PDR": "Laos",
    "Korea, Dem. People's Rep.": "North Korea",
    "Micronesia, Fed. Sts.": "Federated States of Micronesia",
    "Venezuela, RB": "Venezuela",
    "West Bank and Gaza": "Palestine",
    "Serbia": "Republic of Serbia",
    "South Sudan": "South Sudan",
    "Somaliland": "Somaliland",
    "Greenland": "Greenland"
}

# Apply name mapping
combined_data['Country'] = combined_data['Country'].replace(name_mapping)

# Ensure all missing GDP values are filled with 0
combined_data['GDP'] = combined_data['GDP'].fillna(0)

# Merge GeoJSON with Combined Data
merged_geo_data = geo_data.merge(combined_data[['Country', 'GDP']], how='left', left_on='ADMIN', right_on='Country')

# Fill any remaining missing GDP values in the merged GeoJSON with 0
merged_geo_data['GDP'] = merged_geo_data['GDP'].fillna(0)

# Save the cleaned and merged GeoJSON
merged_geojson_path = r"C:\Users\ermal\Desktop\VIzualiztion project\merged_data_gdp.geojson"
merged_geo_data.to_file(merged_geojson_path, driver='GeoJSON')

print(f"Cleaned and merged GeoJSON with GDP saved to: {merged_geojson_path}")

# Visualize the map with GDP
merged_geo_data.plot(
    column="GDP",
    cmap="YlGnBu",
    figsize=(15, 10),
    edgecolor="black",
    legend=True
)
plt.title("World Map with GDP Visualization", fontsize=16)
plt.show()
