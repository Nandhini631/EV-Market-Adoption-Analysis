import pandas as pd

# Load dataset
df = pd.read_csv("data/ev_population.csv")

print("Original Shape:", df.shape)

# Keep required columns
columns_to_keep = [
    "County",
    "City",
    "State",
    "Postal Code",
    "Model Year",
    "Make",
    "Model",
    "Electric Vehicle Type",
    "Clean Alternative Fuel Vehicle (CAFV) Eligibility",
    "Electric Range"
]

df = df[columns_to_keep].copy()

# Remove rows missing important location information
df = df.dropna(subset=["County", "City"])

# Save cleaned dataset
df.to_csv("data/ev_population_cleaned.csv", index=False)

print("Cleaned Shape:", df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nCleaned dataset saved successfully.")