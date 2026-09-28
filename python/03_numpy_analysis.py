import pandas as pd
import numpy as np

df = pd.read_csv("data/ev_population_cleaned.csv")

# Treat zero electric range as missing
df["Electric Range"] = df["Electric Range"].replace(0, np.nan)

# Total EVs
total_evs = len(df)

# EV type count
ev_type_counts = df["Electric Vehicle Type"].value_counts()

# Top manufacturers
top_manufacturers = df["Make"].value_counts().head(10)

# Average electric range
average_range = np.nanmean(df["Electric Range"])

# Median electric range
median_range = np.nanmedian(df["Electric Range"])

# Minimum and maximum range
minimum_range = np.nanmin(df["Electric Range"])
maximum_range = np.nanmax(df["Electric Range"])

# Model year range
minimum_year = df["Model Year"].min()
maximum_year = df["Model Year"].max()

print("Total EVs:", total_evs)

print("\nEV Type Counts:")
print(ev_type_counts)

print("\nTop 10 Manufacturers:")
print(top_manufacturers)

print("\nElectric Range:")
print("Average:", round(average_range, 2))
print("Median:", median_range)
print("Minimum:", minimum_range)
print("Maximum:", maximum_range)

print("\nModel Year:")
print("Minimum Year:", minimum_year)
print("Maximum Year:", maximum_year)