import pandas as pd


def preprocess(df):
    df = df.copy()
    
    # Correct Data Types
    cat_cols = [
        'gender', 'Partner', 'Dependents', 'PhoneService',
        'MultipleLines', 'InternetService', 'OnlineSecurity',
        'OnlineBackup', 'DeviceProtection', 'TechSupport',
        'StreamingTV', 'StreamingMovies', 'Contract',
        'PaperlessBilling', 'PaymentMethod', 'Churn'
    ]
    df[cat_cols] = df[cat_cols].astype('category')

    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

    # Handle Missing Values
    df.dropna(inplace=True)

    # Drop Irrelevant Columns
    df.drop(columns=['customerID'], inplace=True)

    return df