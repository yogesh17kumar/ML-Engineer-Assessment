
import numpy as np
import pandas as pd

def clean_data(df):
    cols_with_zero = [
        "Glucose", "BloodPressure",
        "SkinThickness", "Insulin", "BMI"
    ]
    df[cols_with_zero] = df[cols_with_zero].replace(0, np.nan)
    df = df.fillna(df.median(numeric_only=True))
    df = df.drop_duplicates()
    return df
