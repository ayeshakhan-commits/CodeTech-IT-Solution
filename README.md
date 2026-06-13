# Customer Behavior Analytics & Churn Prediction

## 🚀 Project Overview
This project focuses on analyzing telecom customer behavior data to predict customer churn, segment customers based on value, and build a risk scoring system using Machine Learning.

## 📊 Key Insights & Implementation

### 1. Data Cleaning & Visualization
- Handled missing and incorrect values.
- Created visualizations to explore patterns between customer tenure, monthly charges, and churn.

### 2. Feature Engineering
- Created behavioral features: StreamingUser and ChargesPerMonthRatio.
- Handled categorical data using One-Hot Encoding for algorithms.

### 3. Machine Learning Models & Evaluation
We trained and evaluated two different models on 80% training data and 20% test data:
- *Logistic Regression Model:*
  - *Accuracy:* ~80%
  - *Precision (Churn):* 0.68
  - *Recall (Churn):* 0.45
- *Random Forest Model:*
  - *Accuracy:* ~77%
  - *Precision (Churn):* 0.59
  - *Recall (Churn):* 0.42

Decision: *Logistic Regression* performed better across all metrics and was selected as the final deployment model.

### 4. Customer Segmentation
Customers were divided into three value tiers based on tenure and spending:
- *Low Value Customers:* 3,152
- *High Value Customers:* 2,015
- *Medium Value Customers:* 1,876

### 5. Risk Scoring System
Using our final model, we generated direct churn probabilities and assigned a Risk Category to every customer:
- *Low Risk:* 4,649 customers
- *Medium Risk:* 1,632 customers
- *High Risk:* 762 customers (Action Required: These require immediate retention strategies).

## 🛠️ Tech Stack Used
- Python (Anaconda Distribution)
- Jupyter Notebook / VS Code
- Pandas & NumPy
- Scikit-Learn (ML Training)
- Matplotlib & Seaborn (Data Visualization)
