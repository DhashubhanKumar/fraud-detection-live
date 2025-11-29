import pandas as pd
import joblib
import os
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from xgboost import XGBClassifier

# 1. Define the simple pipeline (matches your new preprocessing_pipeline.py)
def create_final_pipeline():
    return Pipeline([
        ("scaler", StandardScaler()),  # Just scaling, no PCA
        ("clf", XGBClassifier(
            n_estimators=100,       # Enough trees to be accurate
            max_depth=4,            # Not too deep (prevents overfitting)
            learning_rate=0.1,      # Standard speed
            scale_pos_weight=580,   # CRITICAL: Handles the imbalance (Fraud is rare)
            n_jobs=-1,              # Uses all your CPU cores to train fast
            random_state=42
        ))
    ])

if __name__ == "__main__":
    print("⏳ Loading Data...")
    # Adjust path if needed. Assuming you run this from the root folder.
    df = pd.read_csv("data/creditcard.csv")

    # 2. Prepare Data
    X = df.drop("Class", axis=1)
    y = df["Class"]

    # 3. Train
    print("🚀 Training the Final XGBoost Model (this takes ~1-3 mins)...")
    model = create_final_pipeline()
    model.fit(X, y)

    # 4. Save
    print("💾 Saving Model...")
    os.makedirs("saved_models", exist_ok=True) # Creates folder if missing
    joblib.dump(model, "saved_models/XGBoost_best.pkl")
    
    print("✅ SUCCESS! New model saved to: saved_models/XGBoost_best.pkl")