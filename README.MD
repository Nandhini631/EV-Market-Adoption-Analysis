# EV Market & Adoption Analysis

## 📊 Project Overview

EV Market & Adoption Analysis is a practical Data Analytics project that explores the electric vehicle population registered in Washington State.

The project uses a real-world public dataset to analyze EV adoption trends, vehicle types, manufacturers, geographic distribution, and electric-range patterns using Python and Tableau.

The objective is to transform raw registration data into meaningful business insights through data cleaning, numerical analysis, visualization, and dashboard development.

---

## 🎯 Business Questions

- How has EV adoption changed across model years?
- What is the distribution between Battery Electric Vehicles (BEVs) and Plug-in Hybrid Electric Vehicles (PHEVs)?
- Which manufacturers have the highest number of registered EVs?
- Which counties have the highest EV concentration?
- How are EVs distributed across electric-range bands?

---

## 📂 Dataset

**Dataset:** Electric Vehicle Population Data  
**Source:** Washington State Open Data

The dataset contains information about electric vehicles registered through the Washington State Department of Licensing.

### Key Fields Used

- County
- City
- State
- Postal Code
- Model Year
- Make
- Model
- Electric Vehicle Type
- Clean Alternative Fuel Vehicle (CAFV) Eligibility
- Electric Range

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|---|---|
| Python | Data inspection and preprocessing |
| Pandas | Data loading and cleaning |
| NumPy | Numerical analysis |
| Matplotlib | Data visualization |
| Tableau | Interactive dashboard |
| Git & GitHub | Version control and project sharing |

---

## 🔄 Project Workflow

```text
Raw EV Dataset
      ↓
Data Inspection
      ↓
Data Cleaning
      ↓
Numeric Data Preparation
      ↓
NumPy Analysis
      ↓
Matplotlib Visualizations
      ↓
Tableau Analysis
      ↓
Interactive Dashboard
      ↓
Business Insights
```

---

## 🐍 Python Analysis

### `01_data_inspection.py`

Inspects the raw dataset before analysis.

Checks include:

- Dataset shape
- Column names
- Data types
- Missing values
- Duplicate rows
- Sample records

### `02_data_cleaning.py`

Cleans and prepares the dataset by:

- Selecting relevant fields
- Handling missing and invalid values
- Preparing fields for analysis
- Exporting the cleaned dataset

**Output:**

```text
data/ev_population_cleaned.csv
```

### `03_numpy_analysis.py`

Uses NumPy for numerical analysis, including:

- Total EV population
- Manufacturer analysis
- EV type distribution
- Electric-range analysis
- Model-year analysis

### `04_visualization.py`

Creates Matplotlib visualizations for:

- Electric Range Distribution
- EV Type Distribution
- Top 10 Manufacturers

---

## 📈 Tableau Dashboard

The Tableau dashboard combines the analysis into a single interactive view.

### Dashboard Components

**KPI Cards**
- Total EV Population
- Top Manufacturer

**Trend Analysis**
- EVs by Model Year

**Manufacturer Analysis**
- Top 10 Manufacturers

**EV Type Analysis**
- BEV vs PHEV Distribution

**Geographic Analysis**
- EVs by County

**Range Analysis**
- Electric Range Distribution

---

## 🔎 Key Observations

Based on the analyzed dataset:

- The cleaned dataset contains **299,694 EV records**.
- Tesla has the highest number of recorded EVs in the dataset, with **122,975 vehicles**.
- Battery Electric Vehicles (BEVs) represent the larger share of the analyzed EV population compared with PHEVs.
- King County has the highest EV count among the counties shown in the dashboard.
- EV registrations increase substantially across newer model years.
- Electric-range values are concentrated heavily in the lower range band, with fewer vehicles appearing in higher range bands.

These observations are descriptive findings from the dataset and are not future predictions.

---

## 📊 Visualizations

### Python Charts

- `electric_range_distribution.png`
- `ev_type_distribution.png`
- `top_10_manufacturers.png`

### Tableau Dashboard

The dashboard includes:

- KPI cards
- Model-year trend analysis
- Manufacturer comparison
- EV type distribution
- County analysis
- Electric-range distribution

---

## 📁 Project Structure

```text
EV-Market-Adoption-Analysis/
│
├── charts/
│   ├── electric_range_distribution.png
│   ├── ev_type_distribution.png
│   └── top_10_manufacturers.png
│
├── data/
│   ├── ev_population.csv
│   └── ev_population_cleaned.csv
│
├── python/
│   ├── 01_data_inspection.py
│   ├── 02_data_cleaning.py
│   ├── 03_numpy_analysis.py
│   └── 04_visualization.py
│
├── tableau/
│   └── EV market & adoption analysis.twb
│
└── README.MD
```

---

## 💡 Skills Demonstrated

- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Missing-value handling
- Data transformation
- Numerical analysis with NumPy
- Data visualization with Matplotlib
- Tableau dashboard development
- KPI design
- Trend analysis
- Categorical analysis
- Geographic analysis
- Business-focused data storytelling
- Git/GitHub workflow

---

## 🚀 Project Outcome

This project demonstrates an end-to-end Data Analyst workflow:

```text
Raw Data
   ↓
Cleaning
   ↓
Analysis
   ↓
Visualization
   ↓
Dashboard
   ↓
Business Insights
```

The project focuses on practical descriptive analytics and business storytelling rather than machine learning or prediction.

---

## 👩‍💻 Author

**Nandhini.G**

Data Analytics Portfolio Project

**Tools:** Python | Pandas | NumPy | Matplotlib | Tableau | GitHub
