import geopandas as gpd
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')  # Switch backend to TkAgg

import pandas as pd

# File paths
api_gdp_file_path = r"C:\Users\ermal\Desktop\VIzualiztion project\API_NY.GDP.MKTP.CD_DS2_en_csv_v2_2.csv"
output_cleaned_gdp_file_path = r"C:\Users\ermal\Desktop\VIzualiztion project\cleaned_gdp_2023.csv"

# Load the API GDP data
api_gdp_data = pd.read_csv(api_gdp_file_path, skiprows=4)

# Filter only the necessary columns: Country Name and 2023
cleaned_gdp = api_gdp_data[['Country Name', '2023']].rename(
    columns={'Country Name': 'Country', '2023': 'GDP'}
)

# Drop rows where GDP is NaN
cleaned_gdp = cleaned_gdp.dropna(subset=['GDP'])

# Save to CSV in the required format
cleaned_gdp.to_csv(output_cleaned_gdp_file_path, index=False)

print(f"Cleaned GDP data for 2023 saved to: {output_cleaned_gdp_file_path}")
