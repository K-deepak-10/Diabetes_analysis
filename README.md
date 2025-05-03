# 🩺 Diabetes Risk Factor Analysis Dashboard

This project is a comprehensive analysis of diabetes-related health indicators using Power BI, Python, and CSV datasets. The goal is to understand how factors such as glucose levels, BMI, and age contribute to diabetes risk.

## 📌 Problem Statement

Diabetes is a global health issue with increasing prevalence. Early detection and visualization of risk factors can help healthcare professionals and patients make informed decisions. This project aims to build an interactive dashboard that visualizes key metrics and relationships among variables contributing to diabetes.

## 🎯 Objectives

- Analyze patient data to identify trends in glucose, BMI, and age.
- Compare diabetic and non-diabetic individuals using visuals.
- Provide summary statistics like average, median, and standard deviation.
- Allow users to filter the data based on age, BMI, and outcome.
- Present the findings in an easy-to-understand Power BI dashboard.

## 📂 Project Structure
📁 diabetes-dashboard/
│
├── diabetes.csv # Raw dataset (Pima Indian Diabetes Dataset)
├── data_cleaning.py # Python script for preprocessing the dataset
├── diabetes_dashboard.pbix # Power BI dashboard file
├── README.md # Project overview and documentation

## 🧪 Tools & Technologies

- **Power BI** – for interactive dashboard design and visualizations
- **Python (Pandas, NumPy)** – for data cleaning and preprocessing
- **CSV Dataset** – containing health-related attributes and outcome labels

## 📊 Key Features of Dashboard

- **KPI Cards**: Average Glucose, Average BMI, Median Age, Diabetic/Non-Diabetic counts
- **Visuals**:
  - Bar Chart (Summary Stats: Mean, Median, Std Dev of BMI & Glucose)
  - Scatter Plots (Glucose vs Age, Glucose vs BMI)
  - Histogram (BMI vs Glucose)
  - Pie Chart (Diabetes Outcome Distribution)
  - Horizontal Bar (Sum of Age by Outcome)
- **Slicers**: Age, BMI, and Outcome filters for dynamic analysis

## 📈 Insights Gained

- The dashboard highlights strong correlations between high glucose levels and diabetes.
- Provides a demographic distribution of diabetic vs non-diabetic individuals.
- Helps in identifying target risk groups based on age and BMI.

  📜 Dataset Reference
This dataset is based on the Pima Indians Diabetes Database.

🤝 Contributions
Feel free to fork this repo, improve the dashboard or Python code, and raise a pull request!
