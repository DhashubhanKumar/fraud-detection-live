from xgboost import XGBClassifier
from sklearn.pipeline import Pipeline
from src.preprocessing.preprocessing_pipeline import create_preprocessing_pipeline

def create_xgboost_pipeline():
    return Pipeline([
        ("preprocessing", create_preprocessing_pipeline()),
        ("classifier", XGBClassifier(
            n_estimators=300,
        max_depth=5,
        learning_rate=0.05,
        subsample=0.8,
        colsample_bytree=0.8,
        objective="binary:logistic",

        tree_method="hist",        # CPU FAST method
        device="cpu",              # force CPU
        n_jobs=-1,                 # use all CPU cores

        eval_metric="logloss"            # << forces CPU, avoids CUDA warnings
        ))
    ])
