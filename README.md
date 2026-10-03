# 📊 Customer Churn Prediction

A simple machine learning application that predicts whether a customer is likely to churn.

The project uses customer information from the Telco Customer Churn dataset and a Logistic Regression model to make predictions.

## 🚀 Features

* Customer churn prediction
* Logistic Regression machine learning model
* Model accuracy display
* Simple Streamlit web interface
* Interactive customer input

## 🛠️ Technologies Used

* Python
* Pandas
* Scikit-learn
* Streamlit

## 🧠 How It Works

1. The customer dataset is loaded using Pandas.
2. Missing and non-numeric data is processed.
3. Categorical values are converted into numerical values.
4. The dataset is divided into training and testing data.
5. A Logistic Regression model is trained.
6. The model predicts whether a customer is likely to churn.
7. The prediction is displayed through the Streamlit application.

## 📂 Project Structure

```text
Customer-Churn-Prediction/
│
├── dataset/
│   └── WA_Fn-UseC_-Telco-Customer-Churn.csv
│
├── app.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation

Clone the repository:

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
```

Go into the project folder:

```bash
cd Customer-Churn-Prediction
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python -m streamlit run app.py
```

The application will open in your browser.

## 📊 Dataset

This project uses the Telco Customer Churn dataset.

The dataset contains customer information and a `Churn` column indicating whether a customer left the service.

## 🎯 Project Objective

The objective of this project is to demonstrate a basic machine learning classification system for predicting customer churn.

## 👨‍💻 Author

Tanmay Malewar
