import pandas as pd
import streamlit as st
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊"
)

st.title("📊 Customer Churn Prediction")
st.write("Predict whether a customer is likely to churn.")


# Load dataset
BASE_DIR = Path(__file__).resolve().parent

data = pd.read_csv(
    BASE_DIR / "dataset" / "WA_Fn-UseC_-Telco-Customer-Churn.csv"
)


# Remove customer ID
data = data.drop("customerID", axis=1)


# Convert TotalCharges to numeric
data["TotalCharges"] = pd.to_numeric(
    data["TotalCharges"],
    errors="coerce"
)

data = data.dropna()


# Convert categorical columns into numbers
categorical_columns = data.select_dtypes(
    include=["object"]
).columns

for column in categorical_columns:
    encoder = LabelEncoder()
    data[column] = encoder.fit_transform(data[column])


# Split data
X = data.drop("Churn", axis=1)
y = data["Churn"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Train model
model = LogisticRegression(
    max_iter=1000
)

model.fit(X_train, y_train)


# Accuracy
predictions = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    predictions
)

st.write(
    f"### Model Accuracy: {accuracy * 100:.2f}%"
)


# Prediction section
st.subheader("🔍 Customer Prediction")

tenure = st.number_input(
    "Tenure (months)",
    min_value=0,
    max_value=100,
    value=12
)

monthly_charges = st.number_input(
    "Monthly Charges",
    min_value=0.0,
    value=70.0
)

total_charges = st.number_input(
    "Total Charges",
    min_value=0.0,
    value=840.0
)


if st.button("Predict Churn"):

    customer = X.mean().to_frame().T

    customer["tenure"] = tenure
    customer["MonthlyCharges"] = monthly_charges
    customer["TotalCharges"] = total_charges

    prediction = model.predict(customer)[0]

    if prediction == 1:
        st.error("⚠️ Customer is likely to churn.")
    else:
        st.success("✅ Customer is unlikely to churn.")