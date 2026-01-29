## Fraud Detection ML System Design

### Problem Statement
Design a real-time machine learning system to detect fraudulent transactions.

### System Architecture
User Transaction → Data Ingestion → Feature Engineering → ML Model →
Fraud Score → Decision Engine

### Data Sources
Transaction details, user behavior, device and location data.

### Feature Engineering
Transaction frequency, amount deviation, device and location mismatch.

### Model Selection
Logistic Regression for baseline and XGBoost for final deployment.

### Evaluation Metrics
Precision, Recall, F1-score, ROC-AUC.
Recall is prioritized to minimize missed fraud cases.

### Deployment
Model deployed as a REST API for real-time inference.

### Monitoring
Continuous monitoring for data drift and periodic retraining.
