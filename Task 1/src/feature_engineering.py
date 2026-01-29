
def create_features(df):
    df["glucose_bmi_ratio"] = df["Glucose"] / (df["BMI"] + 1)
    df["age_bucket"] = df["Age"] // 10
    df["high_glucose"] = (df["Glucose"] > 140).astype(int)
    df["bmi_squared"] = df["BMI"] ** 2
    return df
