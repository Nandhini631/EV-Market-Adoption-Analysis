import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("data/ev_population_cleaned.csv")

# Treat zero range as missing
df["Electric Range"] = df["Electric Range"].replace(0, np.nan)

# Create charts folder if needed
import os
os.makedirs("charts", exist_ok=True)


# 1. EV Type Distribution
ev_types = df["Electric Vehicle Type"].value_counts()

plt.figure(figsize=(8, 5))
ev_types.plot(kind="bar")
plt.title("Electric Vehicle Type Distribution")
plt.xlabel("EV Type")
plt.ylabel("Number of Vehicles")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("charts/ev_type_distribution.png")
plt.close()


# 2. Top 10 Manufacturers
manufacturers = df["Make"].value_counts().head(10)

plt.figure(figsize=(10, 5))
manufacturers.plot(kind="bar")
plt.title("Top 10 EV Manufacturers")
plt.xlabel("Manufacturer")
plt.ylabel("Number of Vehicles")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("charts/top_10_manufacturers.png")
plt.close()


# 3. Electric Range Distribution
plt.figure(figsize=(10, 5))
plt.hist(df["Electric Range"].dropna(), bins=30)
plt.title("Electric Range Distribution")
plt.xlabel("Electric Range")
plt.ylabel("Number of Vehicles")
plt.tight_layout()
plt.savefig("charts/electric_range_distribution.png")
plt.close()


print("All charts saved successfully.")