# Explainable Deep Learning Framework for Hereditary Obesity Risk Prediction Using Genomic Data

## Project Overview

This research project aims to develop an Explainable Artificial Intelligence (XAI) framework for predicting hereditary obesity risk using Genome-Wide Association Study (GWAS) data.

The proposed system utilizes genomic features such as SNP information, chromosome positions, mapped genes, risk allele frequencies, and genetic effect sizes to predict obesity susceptibility. SHAP explainability is integrated to provide transparent and interpretable predictions.

---

## Research Objectives

1. Predict hereditary obesity risk using genomic data.
2. Improve prediction performance through genomic feature engineering.
3. Address class imbalance using SMOTE.
4. Provide explainable predictions using SHAP.
5. Generate personalized dietary recommendations based on predicted obesity risk.

---

## System Components

### Component 1 – Obesity Risk Prediction

Purpose : Predicting hereditary obesity risk using genomic features and an optimized MLP model.

Technologies:
- Python
- Scikit-Learn
- MLP Classifier
- SMOTE

---
## Dataset

### GWAS Obesity Dataset

Features used:
- CHR_ID
- CHR_POS
- REPORTED GENE(S)
- MAPPED_GENE
- RISK ALLELE FREQUENCY
- OR or BETA
- STRONGEST SNP-RISK ALLELE
- SNPS
- CONTEXT
- INTERGENIC
- UPSTREAM_GENE_DISTANCE
- DOWNSTREAM_GENE_DISTANCE

Source:
GWAS Catalog

---

### Component 2 – Personalized Dietary Recommendation System

Purpose: Generate personalized dietary recommendations based on:

- Predicted obesity risk
- Age
- Lifestyle
- Food preferences
- Health profile

Output:

- Recommended foods
- Foods to avoid
- Daily calorie intake
- Personalized diet plan

Technologies:

- Recommendation algorithms
- Nutrition datasets
- Python

Dataset:

- Keggle Food & Nutrition Dataset

---

### Component 3 – Early Warning & Health Monitoring System

Purpose: Continuously monitor user health indicators and provide early warnings for obesity-related risks.

Inputs:

- BMI
- Weight trends
- Physical activity
- Sleep patterns
- Calorie intake
- Historical risk predictions

Outputs:

- Risk alerts
- Health trend analysis
- Early warning notifications
- Preventive health recommendations

Technologies:

- Health monitoring module
- Notification system
- Data analytics

---

## Methodology

Dataset Collection
↓
Data Preprocessing
↓
Feature Engineering
↓
Feature Encoding
↓
Feature Scaling
↓
SMOTE Balancing
↓
Optimized MLP Training
↓
Obesity Risk Prediction
↓
SHAP Explainability
↓
Personalized Dietary Recommendation
↓
Early Warnings & Health Monitering System

---

## Technologies Used

- Python
- NumPy
- Pandas
- Scikit-learn
- SHAP
- Jupyter Notebook
- Git
- GitHub

---

## Current Progress

### Component 1 – Genomic Obesity Risk Prediction

#### Completed
- Literature Review
- GWAS Dataset Collection
- Data Preprocessing
- Feature Engineering
- Class Imbalance Handling (SMOTE)
- Logistic Regression Implementation
- Random Forest Implementation
- Support Vector Machine (SVM) Implementation
- Multilayer Perceptron (MLP) Implementation
- XGBoost Implementation
- SHAP Explainability Analysis
- Optimized MLP Pipeline Development
- Model Evaluation using Accuracy, Precision, Recall, F1-Score and ROC-AUC
- Model Saving and Reusable Pipeline Creation

#### In Progress
- Model Deployment Preparation
- Backend API Integration

---

### Component 2 – Personalized Dietary Recommendation System

#### Completed
- Requirement Analysis
- Literature Review
- Dataset Identification
- Recommendation Methodology Design
- Recommendation Pipeline Design

#### In Progress
- Nutrition Dataset Collection
- Recommendation Model Development
- Food Categorization Framework

#### Planned
- Personalized Diet Plan Generation
- Calorie Requirement Calculation
- Food Recommendation Engine

---

### Component 3 – Early Warning & Health Monitoring System

#### Completed
- Requirement Analysis
- Literature Review
- Health Monitoring Framework Design
- Early Warning Mechanism Design

#### In Progress
- Health Indicator Selection
- Monitoring Workflow Development

#### Planned
- Alert Generation Module
- Health Trend Analysis Module
- Risk Notification System
- Dashboard Development

---

## Repository Structure

Obesity_Project/
│
├── README.md
│
├── Component_1_Genomic_Risk_Prediction/
│   │
│   ├── data/
│   ├── notebooks/
│   │   ├── Experiment_1.ipynb
│   │   ├── Experiment_2.ipynb
│   │   ├── Experiment_3.ipynb
│   │   └── Experiment_4.ipynb
│   │
│   ├── models/
│   │   └── optimized_mlp.pkl
│   │
│   ├── results/
│   │   └── evaluation_metrics.csv
│   │
│   └── docs/
│       └── methodology_notes.md
│
├── Component_2_Dietary_Recommendation_System/
│   │
│   ├── data/
│   │
│   ├── notebooks/
│   │
│   ├── results/
│   │
│   └── .DS_Store      
│
├── Component_3_Early_Warning_Health_Monitoring/
│   │
│   ├── data/
│   │   └── health_logs.csv
│   │
│   ├── notebooks/
│   │   └── monitoring_system.ipynb
│   │
│   ├── models/
│   │   └── risk_trend_model.pkl (optional)
│   │
│   ├── results/
│   │   └── alerts_output.csv
│   │
│   └── docs/
│       └── monitoring_system_design.md

---

## Authors

Haarun Chandramohan - IT22268662
Dineshkumar Sivapalan - IT22056016
Farshad Inayadulla - IT22182500

SLIIT
Final Year Research Project
