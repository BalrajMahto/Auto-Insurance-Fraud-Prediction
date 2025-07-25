# 🚗 AI-Powered Fraud Detection in Auto Insurance  
**Team Name:** TriCache

---

## 📢 Learnathon Project Submission

This project was built and submitted as part of the **Learnathon Challenge**.  
🔗 **GitHub Repository Link**: [github.com/FraudSquad4/auto-fraud-detection](https://github.com/FraudSquad4/auto-fraud-detection)  
---

## 🧠 Project Overview

> AI-Powered Fraud Detection in Auto Insurance: Predictive Modeling for Smarter Claims Management

This project uses a machine learning model to predict fraudulent insurance claims from structured claim data. It includes a user-friendly Streamlit web app for uploading data, getting predictions, and visualizing model insights.


---

## 👥 Team Members – **TriCache**

- **Anishet Rajesh** – Data preprocessing
- **Aditya Narayan Dash** – Model creation & training
- **Balraj Mahto** – Streamlit frontend development,Visualizations

---
## 📦 Tech Stack

| Layer | Tools |
|-------|-------|
| ML Model | RandomForestClassifier (Scikit-learn) |
| Data Handling | Pandas, NumPy |
| Preprocessing | LabelEncoder, Imputer, StandardScaler |
| UI | Streamlit |
| Visualization | Matplotlib, Plotly |
| Deployment | Local Streamlit WebApp |

---

## 📊 Dataset Used

- Auto_Insurance_Fraud_Claims_File01.csv → Training
- Auto_Insurance_Fraud_Claims_File02.csv → Validation
- Auto_Insurance_Fraud_Claims_File03.csv → Test
- Data Dictionary provided for feature reference

---

## 🔍 Key Features of the App

- Upload test claim CSV
- Auto preprocessing
- Predict if claim is **Fraud** or **Not Fraud**
- Visualize:
  - Top Features (Matplotlib + Plotly)
  - Confusion Matrix
  - Classification Report
- Download CSV with predictions

---

## 💡 Highlights

- Full ML pipeline from raw data to real-time predictions
- Real-world problem, real-world UI
- Interactive visualizations for explainability
- Downloadable outputs
---

## 🧠 Model Info

- *Algorithm*: Random Forest Classifier
- *Trained on*: Auto Insurance Fraud Claims dataset
- *Training Accuracy*: ~99%
- *Validation Accuracy*: ~99%

Model saved as: model.pkl
---

## 📝 Files in Repository

```bash
├── app.py                         # Streamlit UI
├── preprocess.py                 # Preprocessing logic
├── model.pkl                     # Saved trained model
├── train_model.py                # Model training script
├── Auto_Insurance_Fraud_*.csv    # Input data files
└── README.md

## 🚀 How to Run the App Locally

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/fraud-detection-app.git
cd fraud-detection-app

##Install Dependencies:
pip install -r requirements.txt

Or manually:
pip install streamlit pandas scikit-learn matplotlib plotly joblib

Run the App:
streamlit run app.py 
