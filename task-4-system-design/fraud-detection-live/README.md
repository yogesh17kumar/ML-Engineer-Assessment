# Fraud Detection ML System Design

## Problem Statement
Design a **real-time machine learning system** to detect fraudulent financial transactions with high recall to minimize missed fraud cases.

The system is designed keeping **production ML engineering practices** in mind, including data ingestion, training pipelines, inference flow, monitoring, drift detection, and retraining strategy.

---

## System Architecture
![Fraud Detection System Architecture](live/diagram.png)

---

## Data Sources
The system consumes real-time transaction data from multiple sources:
- Transaction amount and timestamp
- User behavior patterns
- Device information
- Location and location-change signals

---

## Feature Engineering
Key engineered features include:
- Transaction frequency
- Amount deviation from user’s historical behavior
- Device change indicator
- Location mismatch
- Transaction hour (time-based behavior)

These features help capture abnormal patterns commonly associated with fraud.

---

## Model Selection
- **Baseline Model:** Logistic Regression  
  - Simple, interpretable, and fast for real-time inference
- **Advanced Model:** XGBoost (recommended for production)
  - Handles non-linearity and complex fraud patterns better

In this implementation, Logistic Regression is used for simplicity and explainability.

---

## Training Pipeline
1. Data preprocessing and cleaning
2. Feature scaling using StandardScaler
3. Train-test split
4. Model training
5. Evaluation using classification metrics
6. Model and scaler saved as `.pkl` files for deployment

---

## Evaluation Metrics
The following metrics are used:
- Precision
- Recall (**prioritized** to avoid missing fraud cases)
- F1-score
- ROC-AUC

---

## Inference Flow
- Incoming transaction is converted into features
- Features are scaled using the trained scaler
- Model outputs a fraud probability (fraud score)
- Threshold-based decision:
  - Fraudulent
  - Legitimate

---

## Deployment
- Model deployed as a **Streamlit-based web application**
- Acts as a real-time inference service
- Can be extended to REST API deployment using FastAPI or Flask
- Uses saved `.pkl` model and scaler files

---

## Monitoring & Drift Detection
- Continuous monitoring of:
  - Input feature distributions
  - Fraud prediction rates
  - Model confidence scores
- Data drift detected by comparing live data statistics with training data

---

## Retraining Strategy
- Periodic retraining (weekly or monthly)
- Automatic retraining triggered by detected data drift
- Model validation before redeployment
- Rollback support to previous stable models

---

## Live Demo
A live fraud detection prototype is deployed using **Streamlit Cloud**.

**Live Project Link:**  
https://ml-engineer-assessment-mt5l9ai3jmk82s2hqdndym.streamlit.app/

---

## Tech Stack
- Python
- Scikit-learn
- NumPy
- Joblib
- Streamlit

---

## Conclusion
This project demonstrates an end-to-end **production-ready ML system design** for fraud detection, covering model training, deployment, monitoring, and retraining strategies.  
It reflects real-world ML engineering workflows beyond simple model building.

---

## Author
**Yogesh Kumar**
