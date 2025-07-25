# preprocess.py
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.impute import SimpleImputer

def preprocess_input(df):
    drop_cols = ['Claim_ID', 'Policy_Num', 'Vehicle_Registration',
                 'Bind_Date1', 'Policy_Start_Date', 'Policy_Expiry_Date',
                 'Accident_Date', 'DL_Expiry_Date', 'Claims_Date']
    
    df = df.drop(columns=drop_cols, errors='ignore')

    cat_cols = df.select_dtypes(include='object').columns
    num_cols = df.select_dtypes(include=['int64', 'float64']).columns

    df[cat_cols] = SimpleImputer(strategy='most_frequent').fit_transform(df[cat_cols])
    df[num_cols] = SimpleImputer(strategy='mean').fit_transform(df[num_cols])

    for col in cat_cols:
        df[col] = LabelEncoder().fit_transform(df[col].astype(str))

    df[num_cols] = StandardScaler().fit_transform(df[num_cols])

    return df
