# EV Market & Adoption Analysis

## 📊 Project Overview

**EV Market & Adoption Analysis** is a practical Data Analytics project
that explores the electric vehicle population registered in Washington
State.

The project uses a real-world public dataset to analyze EV adoption
trends, vehicle types, manufacturers, geographic concentration, and
electric-range distribution using **Python, NumPy, Pandas, Matplotlib,
and Tableau Public**.

The objective is to transform raw registration data into clear,
business-focused insights through data cleaning, exploratory analysis,
visualization, and dashboard development.

------------------------------------------------------------------------

## 🎯 Business Questions

-   How has EV adoption changed across model years?
-   What is the distribution between **Battery Electric Vehicles
    (BEVs)** and **Plug-in Hybrid Electric Vehicles (PHEVs)**?
-   Which manufacturers have the highest number of registered EVs?
-   Which counties have the highest EV concentration?
-   How are EVs distributed across electric-range bands?
-   Which manufacturers and EV types contribute most to the registered
    EV population?

------------------------------------------------------------------------

## 📂 Dataset

**Dataset:** Electric Vehicle Population Data\
**Source:** Washington State Open Data

The dataset contains information about electric vehicles registered
through the Washington State Department of Licensing.

### Key fields used

-   County
-   City
-   State
-   Postal Code
-   Model Year
-   Make
-   Model
-   Electric Vehicle Type
-   Clean Alternative Fuel Vehicle Eligibility
-   Electric Range
-   Vehicle Location
-   Electric Utility

------------------------------------------------------------------------

## 🛠️ Tools & Technologies

  Tool             Purpose
  ---------------- ----------------------------------------
  Python           Data inspection, cleaning and analysis
  Pandas           Data loading and preprocessing
  NumPy            Numerical analysis
  Matplotlib       Python visualizations
  Tableau Public   Interactive dashboard
  Git & GitHub     Version control

------------------------------------------------------------------------

## 🔄 Project Workflow

``` text
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

------------------------------------------------------------------------

## 🐍 Python Analysis

### `01_data_inspection.py`

Inspects the raw dataset before analysis.

Checks include:

-   Dataset shape
-   Column names
-   First few records
-   Data types
-   Missing values
-   Duplicate rows

### `02_data_cleaning.py`

Cleans and prepares the dataset by:

-   Selecting relevant fields
-   Handling missing and invalid values
-   Preparing fields for analysis
-   Exporting the cleaned dataset

Output:

``` text
data/ev_population_cleaned.csv
```

### `03_numpy_analysis.py`

Uses NumPy for numerical analysis, including:

-   EV population counts
-   Manufacturer analysis
-   EV type distribution
-   Electric-range analysis
-   Model-year analysis

### `04_visualization.py`

Creates Matplotlib charts for:

-   Electric Range Distribution
-   EV Type Distribution
-   Top 10 Manufacturers

------------------------------------------------------------------------

## 📈 Tableau Dashboard

The Tableau dashboard presents the analysis in a single interactive
view.

### Dashboard components

**KPI Cards** - Total EV Population - Top Manufacturer

**Trend Analysis** - EVs by Model Year

**Manufacturer Analysis** - Top 10 Manufacturers

**EV Type Analysis** - Battery Electric Vehicle (BEV) - Plug-in Hybrid
Electric Vehicle (PHEV)

**Geographic Analysis** - Top 10 Counties

**Range Analysis** - Electric Range Distribution

------------------------------------------------------------------------

## 🔎 Key Observations

Based on the dataset used in the dashboard:

-   The analyzed dataset contains **299,694 EV records**.
-   **Tesla** is the leading manufacturer shown in the dashboard, with
    **122,975 recorded EVs**.
-   Battery Electric Vehicles represent the larger share of the EV
    population compared with Plug-in Hybrid Electric Vehicles.
-   **King County** has the highest EV count among the counties shown in
    the Top 10 Counties analysis.
-   EV registrations increase substantially across newer model years.
-   The electric-range distribution is concentrated heavily in the
    **0--49 range band**, with smaller counts across higher range bands.

These are descriptive observations from the analyzed dataset, not future
forecasts.

------------------------------------------------------------------------

## 📊 Visualizations

### Python Charts

-   `electric_range_distribution.png`
-   `ev_type_distribution.png`
-   `top_10_manufacturers.png`

### Tableau Dashboard

The dashboard combines:

-   KPI cards
-   Line chart
-   Bar charts
-   EV type comparison
-   County analysis
-   Electric-range distribution

------------------------------------------------------------------------

## 📁 Project Structure

``` text
EV Market & Adoption Analysis/
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
│   └── EV Market & Adoption Analysis.twbx
│
└── README.md
```

------------------------------------------------------------------------

## 💡 Skills Demonstrated

-   Data cleaning and preprocessing
-   Exploratory Data Analysis (EDA)
-   Missing-value handling
-   Data transformation
-   Numerical analysis with NumPy
-   Data visualization with Matplotlib
-   Tableau dashboard development
-   KPI design
-   Trend analysis
-   Categorical comparison
-   Geographic analysis
-   Business-focused data storytelling
-   Git/GitHub workflow

------------------------------------------------------------------------

## 🚀 Project Outcome

This project demonstrates an end-to-end **Data Analyst workflow**:

**Raw Data → Cleaning → Analysis → Visualization → Dashboard →
Insights**

The project focuses on practical descriptive analytics and business
storytelling rather than machine learning or prediction.

------------------------------------------------------------------------

## 👩‍💻 Author

**Nandhini.G**

Data Analytics Portfolio Project

**Tools:** Python \| Pandas \| NumPy \| Matplotlib \| Tableau Public \|
GitHub
