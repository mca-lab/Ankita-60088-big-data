## Project Overview
Build a Big Data project using Python, PySpark and Docker. The workflow includes:

1. Data ingestion from multiple sources
2. Data cleaning and integration
3. Analysis and visualization
4. Reproducible Docker-based setup for data collection and processing

pick **2 or more datasets**, define a **research question or hypothesis** and implement the pipeline.

---

## Project Workflow

### Module 1. Data Collection & Ingestion
**Objective:** Automate downloading datasets and storing them for processing.

**Tasks:**
- Choose 2+ public datasets (Kaggle, Data.gov, WHO, World Bank, UCI, etc.)
- Write Python script to fetch datasets dynamically (URLs, APIs, Kaggle datasets)
- Store raw datasets in `data/raw/`
- Optional: convert datasets to Parquet for efficient storage
- Docker container ensures uniform data collection environment

**Deliverables:**
- `Dockerfile` + `requirements.txt`
- Scripts in `src/` (e.g., `fetch_data.py`)
- `data/raw/` populated when container runs

---

### Module 2. Data Cleaning & Integration
**Objective:** Prepare raw data for analysis using PySpark.

**Tasks:**
- Load raw datasets into PySpark
- Handle missing values, inconsistent formats, duplicates
- Merge, join or aggregate datasets as required
- Store processed data in `data/processed/`
- Docker container ensures reproducible cleaning pipeline

**Deliverables:**
- `Dockerfile` + `requirements.txt` for cleaning
- Scripts in `src/` (e.g., `clean_data.py`)
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

## Technologies
- Python
- PySpark
- Matplotlib, Seaborn, Plotly
- Docker

---

## Notes
- Module 1 and Module 2 require Docker for reproducibility
- Module 3 is executed in Jupyter Notebook (no Docker required)
- End goal: automated pipeline from data fetching → cleaning → analysis → insights




