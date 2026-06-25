# 🛍️ Retail Sales Analytics & Interactive BI Dashboard

An end-to-end Data Analytics pipeline built to simulate, preprocess, clean, and visualize a high-volume retail transaction market dataset. This project leverages data science workflows to transform raw commercial inputs into real-time business insights.

## 📌 Project Overview
The workflow replicates standard enterprise analytical protocols:
* *Programmatic Data Generation:* 1,200 transactional logs distributed dynamically across metropolitan cities in Pakistan.
* *Schema Verification & Data Cleaning:* Reconstructing structural calculated values ($Total\ Amount = Quantity \times Unit\ Price$) using dependency handling logic.
* *Exploratory Data Analysis (EDA):* Uncovering monthly performance trends, payment method share, and category performance rankings.
* *Interactive Web App Deployment:* Constructing a responsive dashboard using Python Streamlit for immediate metric filtering.

## 📊 Core Features
1. *Dynamic Metrics Core:* Live rendering of corporate KPIs (Total Revenue, Volume Sold, Order Volume, and Average Order Value).
2. *Multi-Select Filter Control:* Sidebar navigation to slice and dice performance metrics by Location and Category.
3. *Data Quality Guard:* Programmatic removal of missing values prior to aggregation layers.

## 🛠️ Technology Stack
* *Language:* Python
* *Libraries:* Pandas, NumPy, Matplotlib, Seaborn, Plotly
* *Framework:* Streamlit (Web Dashboard App)

## 📁 Repository Structure
* DA-Task-2_Retail_Sales_Analysis.ipynb: Main Jupyter Notebook for backend preprocessing, simulation, and EDA plotting.
* app.py: Production-ready Streamlit source code file for the BI application dashboard.
* Retail_Store_Sales_Dataset.csv: Preprocessed dataset containing transaction inputs.
* Retail_Sales_Analysis_Report.docx: Deep corporate analytics report containing complete documentation.

## 🚀 How to Run the Dashboard App
Ensure dependencies are satisfied:
```bash
pip install streamlit pandas plotly
streamlit run app.py
