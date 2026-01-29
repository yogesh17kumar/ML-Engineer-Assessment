
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

from config import SEED, TEST_SIZE
from data_preprocessing import clean_data
from feature_engineering import create_features

def train_model(data_path):
    df = pd.read_csv(data_path, sep="\t")

    # Fix column names
    df.columns = [
        "Pregnancies", "Glucose", "BloodPressure",
        "SkinThickness", "Insulin", "BMI",
        "DiabetesPedigreeFunction", "Age", "Outcome"
    ]

    df = clean_data(df)
    df = create_features(df)

    X = df.drop("Outcome", axis=1)
    y = df["Outcome"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=TEST_SIZE,
        random_state=SEED,
        stratify=y
    )

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    model = LogisticRegression(max_iter=1000, random_state=SEED)
    model.fit(X_train, y_train)

    joblib.dump(model, "models/diabetes_model.pkl")
    joblib.dump(scaler, "models/scaler.pkl")

    return X_test, y_test
