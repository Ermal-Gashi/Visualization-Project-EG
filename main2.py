# Insert Cleaned Data

import pandas as pd

# Define file paths
gdp_path = r"C:\Users\ermal\Desktop\VIzualiztion project\GDP\cleaned_gdp_2023.csv"
cpi_path = r"C:\Users\ermal\Desktop\VIzualiztion project\CPI\cleaned_cpi_2023.csv"
fdi_path = r"C:\Users\ermal\Desktop\VIzualiztion project\FDI\cleaned_fdi_2023.csv"
unemployment_path = r"C:\Users\ermal\Desktop\VIzualiztion project\Unemployment\cleaned_unemployment_2023.csv"

# Load datasets
gdp_data = pd.read_csv(gdp_path)
cpi_data = pd.read_csv(cpi_path)
fdi_data = pd.read_csv(fdi_path)
unemployment_data = pd.read_csv(unemployment_path)

# Merge datasets using an outer join
combined_data = (
    gdp_data.merge(cpi_data, on="Country", how="outer")
            .merge(fdi_data, on="Country", how="outer")
            .merge(unemployment_data, on="Country", how="outer")
)

# Save the combined dataset to a CSV file
combined_output_path = r"C:\Users\ermal\Desktop\VIzualiztion project\combined_data.csv"
combined_data.to_csv(combined_output_path, index=False)

print(f"Combined dataset saved at: {combined_output_path}")
