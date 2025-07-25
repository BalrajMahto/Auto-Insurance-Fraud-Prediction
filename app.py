# app.py
import streamlit as st
import pandas as pd
import joblib
from Preprocess import preprocess_input
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report

st.set_page_config(page_title="Fraud Detection App", layout="centered")
st.title(" Auto Insurance Fraud Prediction")

# Load trained model
model = joblib.load("model.pkl")

# File uploader
uploaded_file = st.file_uploader("Upload claims CSV file", type="csv")

if uploaded_file is not None:
    try:
        raw_df = pd.read_csv(uploaded_file)
        st.write("### 🔍 Preview of Uploaded Data", raw_df.head())

        # Preprocess input
        X_test = preprocess_input(raw_df.copy())

        # Predict
        preds = model.predict(X_test)
        raw_df["Fraud_Predicted"] = preds
        st.success("✅ Prediction complete!")

        # Show results
        st.write("### 📊 Prediction Results")
        st.dataframe(raw_df[["Claim_ID", "Fraud_Predicted"]])

        # Download button
        csv = raw_df.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="📥 Download Full Results as CSV",
            data=csv,
            file_name="fraud_predictions.csv",
            mime="text/csv"
        )

        # === Static Feature Importance Plot (matplotlib) ===
        st.write("### 📉 Model Feature Importance")
        feature_names = X_test.columns
        importances = model.feature_importances_
        indices = np.argsort(importances)[::-1]

        top_n = 15
        top_indices = indices[:top_n]

        fig, ax = plt.subplots(figsize=(10, 6))
        ax.bar(range(top_n), importances[top_indices], align="center", color="skyblue")
        ax.set_xticks(range(top_n))
        ax.set_xticklabels(feature_names[top_indices], rotation=90)
        ax.set_title("Top Features Used by Model")
        ax.set_ylabel("Importance")
        st.pyplot(fig)

        # === Interactive Feature Importance Plot (Plotly) ===
        st.write("### 📌 Feature Importance (Interactive)")
        feat_df = pd.DataFrame({
            'Feature': feature_names,
            'Importance': importances
        }).sort_values(by='Importance', ascending=False)

        fig_plotly = px.bar(feat_df.head(15), x='Importance', y='Feature',
                            orientation='h', title='Top 15 Features by Importance',
                            color='Importance', color_continuous_scale='Blues')
        st.plotly_chart(fig_plotly)

        # === Confusion Matrix and Report ===
        if 'Fraud_Ind' in raw_df.columns:
            y_true = raw_df['Fraud_Ind'].map({'Y': 1, 'N': 0})
            y_pred = raw_df['Fraud_Predicted']

            st.write("### 🔍 Confusion Matrix")
            cm = confusion_matrix(y_true, y_pred)
            fig_cm, ax_cm = plt.subplots()
            disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['Not Fraud', 'Fraud'])
            disp.plot(ax=ax_cm, cmap='Blues')
            st.pyplot(fig_cm)

            # Classification report
            st.write("### 🧾 Classification Report")
            report = classification_report(y_true, y_pred)
            st.code(report)

    except Exception as e:
        st.error(f"❌ Error processing file: {e}")
