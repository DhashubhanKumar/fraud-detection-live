from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

# Removed 'n_components' argument because we are not using PCA anymore
def create_preprocessing_pipeline():
    return Pipeline([
        ("scaler", StandardScaler()) 
    ])