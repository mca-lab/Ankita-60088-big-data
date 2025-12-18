#### **Project Title : Global CO₂ Emissions and Population Growth Analysis Using PySpark and Docker**

## Project Overview

This project implements an end-to-end Big Data analytics pipeline using Python, PySpark, Docker, and Jupyter Notebook to analyze the relationship between global population growth and CO₂ emissions over time. The pipeline automates data ingestion, cleaning, integration, analysis, and visualization with an emphasis on reproducibility and scalability.

The pipeline automates:
- Data ingestion from public online sources
- Data cleaning and integration using PySpark
- Exploratory data analysis and visualization
- Reproducible execution using Docker containers

The goal is to transform raw global datasets into actionable insights about environmental impact and demographic trends.
**End goal**: an automated workflow from data fetching → cleaning → analysis → insights.

## Research Question & Hypothesis

**Research Question:**

Is there a measurable relationship between global population growth and CO₂ emissions over time?

**Hypothesis:**

As global population increases, total CO₂ emissions also increase, indicating a positive correlation between population size and carbon emissions.

--- 

## Datasets Used

The project uses two publicly available global datasets fetched dynamically via URLs defined in src/fetch_data.py.

**1) Global Population Dataset**

**Source:** DataHub (compiled from UN & World Bank sources)

**URL:** https://raw.githubusercontent.com/datasets/population/master/data/population.csv

**Description:** Country-wise population figures by year, representing global population trends.

**Key Columns:** Country Name, Country Code, Year, Value (Population)


**2) Global CO₂ Emissions Dataset**

**Source:** DataHub (Global Carbon Project)

**URL:** https://raw.githubusercontent.com/datasets/co2-fossil-global/master/global.csv

**Description:** Yearly global CO₂ emissions from fossil fuel combustion and industrial processes.

**Key Columns:** Year, Total, Gas Fuel, Liquid Fuel, Solid Fuel, Cement, Gas Flaring

Why these datasets? They are authoritative, open-source, time-series friendly, and suitable for correlation and trend analysis.

---

## Project Structure
-Project_Name/

-├── data/

    -│   ├── raw/
    
    -│   └── processed/

-├── notebooks/

    -│   └── Module3_Analysis.ipynb

-├── src/

    -│   ├── fetch_data.py

    -│   └── clean_data.py

-├── Dockerfile

-├── requirements.txt

-└── README.md

---

## Project Workflow

### Module 1. Data Collection & Ingestion
**Objective:** Automate dataset downloading and ensure reproducible ingestion.

**Tasks:**
-Select two public datasets related to population and CO₂ emissions
-Fetch datasets dynamically using Python
-Store raw files in data/raw/
-Convert datasets to Parquet for efficient storage
-Execute ingestion inside a Docker container

**Deliverables:**
- Dockerfile, requirements.txt
- src/fetch_data.py
- data/raw/ populated at runtime

---

### Module 2. Data Cleaning & Integration
**Objective:** Prepare raw data for analysis using PySpark.

**Tasks:**
- Load raw datasets into PySpark DataFrames
- Handle missing values and inconsistent formats
- Aggregate population data to global yearly totals
- Join population and CO₂ datasets on the Year column
- Store cleaned datasets in data/processed/
- Docker container ensures reproducible cleaning pipeline

**Deliverables:**
- `Dockerfile` + `requirements.txt` for cleaning
- Scripts in `src/clean.py` 
- `data/processed/` ready for analysis

---

### Module 3. Data Analysis & Visualization
**Objective:** To explore and analyze cleaned datasets in order to identify trends, relationships, and insights related to CO₂ emissions and population.

**Tasks:**
- Loaded processed datasets into Jupyter Notebook
- Performed descriptive statistics and aggregation
- Conducted correlation analysis
- Created visualizations using Matplotlib and Seaborn
- Documented findings and interpretations

**Deliverables:**
- Jupyter Notebook: `notebooks/Module3_Analysis.ipynb`
- Plots illustrating trends and relationships
- Statistical analysis and conclusions
---

## Results & Key Findings
- Global population shows a **consistent upward trend** over the observed years.
- CO₂ emissions increase over time with periods of acceleration and stabilization.
- A positive correlation is observed between global population and total CO₂ emissions.
- The relationship suggests that population growth is a contributing factor to rising emissions, though not the sole driver.
  
---

## Conclusion

This project demonstrates how a Big Data pipeline can be built using PySpark and Docker to analyze large, real-world datasets. The analysis supports the hypothesis that population growth is positively correlated with CO₂ emissions. However, emissions are also influenced by industrialization, energy sources, and policy decisions, indicating the need for multi-factor environmental analysis.

---

## Technologies
- Python
- PySpark
- Matplotlib, Seaborn, Plotly
- Docker
- Jupyter Notebook

---

## Notes
- Module 1 and Module 2 run inside Docker containers for reproducibility.
- Module 3 is executed in Jupyter Notebook (no Docker required)
- Dataset URLs are centrally managed in fetch_data.py for dynamic ingestion.

---

## Future Improvements
- Add country-level analysis
- Include GDP or energy consumption datasets
- Apply regression or time-series forecasting models
- Deploy the pipeline using Airflow or cloud services


