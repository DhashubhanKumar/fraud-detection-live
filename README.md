# 🛡️ FraudGuard AI: Real-Time Credit Card Fraud Detection

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://fraud-detection-live.streamlit.app)
![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![XGBoost](https://img.shields.io/badge/Model-XGBoost-orange.svg)
![Docker](https://img.shields.io/badge/Container-Docker-blue)

**FraudGuard AI** is an end-to-end Machine Learning application designed to detect fraudulent credit card transactions in real-time. It addresses the challenge of extreme class imbalance (only 0.17% fraud cases) using a robust **XGBoost** classifier and provides a user-friendly interface via **Streamlit**.

---

## 🚀 Live Demo
**[Click here to use the Live App](https://fraud-detection-live.streamlit.app)**

---

## 🧠 Key Features
*   **High-Performance Model:** Built using **XGBoost** (Extreme Gradient Boosting), optimized for tabular data.
*   **Imbalance Handling:** Utilizes `scale_pos_weight` to mathematically penalize missing fraud cases, achieving high Recall.
*   **Real-Time Inference:** Instant predictions with a probability risk score.
*   **Production Ready:** Modular code structure, pipeline-based preprocessing, and containerized with **Docker**.
*   **Interactive UI:** A dark-mode dashboard to simulate transaction scenarios and visualize risk factors.

---

## 🛠️ Tech Stack
*   **Language:** Python 3.11
*   **Machine Learning:** Scikit-Learn, XGBoost, Joblib
*   **Data Processing:** Pandas, NumPy
*   **Deployment:** Streamlit Cloud, Docker

---

## 💻 How to Run Locally

You can run this project on your local machine using Python or Docker.

### Option 1: Using Python (Recommended)

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/DhashubhanKumar/fraud-detection-live.git
    cd fraud-detection-live
    ```

2.  **Create a virtual environment:**
    *It is recommended to use Python 3.11 to avoid compatibility issues.*
    ```bash
    # Windows
    py -3.11 -m venv venv
    .\venv\Scripts\Activate

    # Mac/Linux
    python3.11 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the App:**
    ```bash
    streamlit run app.py
    ```
    The app will open in your browser at `http://localhost:8501`.

### Option 2: Using Docker 🐳
If you have Docker installed, you can run the app in a container without installing Python libraries.

1.  **Build the Image:**
    ```bash
    docker build -t fraud-app .
    ```

2.  **Run the Container:**
    ```bash
    docker run -p 8501:8501 fraud-app
    ```
    Access the app at `http://localhost:8501`.

---

## 🧪 How to Simulate Fraud
The model is trained on real patterns. To see the model flag a transaction as **FRAUD** in the UI, set the sliders to the following values (which mimic a typical mathematical fraud signature):

1.  **V14:** Set to **Negative** (e.g., -5.0)
2.  **V4:** Set to **Positive** (e.g., 5.0)
3.  **V11:** Set to **Positive** (e.g., 4.0)

Click **"Analyze Transaction"** and watch the alert turn RED. 🚨

---

## 📊 Model Metrics
The model was evaluated on the unseen test set of the Kaggle Credit Card Fraud Dataset.

| Metric | Score | Description |
| :--- | :--- | :--- |
| **ROC-AUC** | **0.97+** | Excellent ability to distinguish between Fraud and Safe. |
| **Recall** | **High** | Prioritizes catching thieves over avoiding false alarms. |

---

## 👨‍💻 Author
**Dhashubhan Kumar**  
*Aspiring GenAI Engineer*  

---
*Note: The dataset features (V1-V28) are PCA-transformed for privacy. This project simulates the backend processing of a banking security module.*
