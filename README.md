
# Blood Cell Anomaly Detection App


**Machine Learning Classification Project + Streamlit Web App**

An interactive **Streamlit** app that predicts whether a blood cell is Normal or Anomalous based on a set of biological and lab features, plus a full Jupyter Notebook documenting the entire project lifecycle — from data analysis to training and comparing 9 different classification models.

🔗 **Live Demo:** [mycleanapp.streamlit.app](https://mycleanapp-cwfiw7gku84py84fhjsappx.streamlit.app/)

---

## 📋 Project Overview

The goal of this project is to classify blood cells into:

| Value | Class |
|---|---|
| `0` | Normal |
| `1` | Abnormal / Anomaly |

The notebook covers the full workflow:

1. Import libraries and load the dataset
2. Data quality checks (missing values / duplicates)
3. Target distribution analysis (`anomaly_label`)
4. Feature selection and data cleaning (dropping columns that would cause data leakage)
5. Encoding categorical features
6. Outlier inspection (without removal)
7. Correlation analysis
8. Train/test split with stratification to preserve class balance
9. Feature scaling (`StandardScaler` fit only on training data)
10. Training and evaluating 9 different classification models
11. Model comparison and selection of the best performer

---

## 📁 Project Structure

```
.
├── appp.py                                       # Interactive Streamlit app
├── Blood_Cell_Anomaly_Detection_Cleaned.ipynb    # Notebook: analysis, training, evaluation
├── best_model.pkl                                # Final trained model (XGBoost)
├── scaler.pkl                                    # StandardScaler used during training
├── requirements.txt                              # Project dependencies
└── README.md                                     # This file
```

---

## 🧬 Features Used for Prediction

The model relies on **26 features**, grouped as follows:

**Cell morphology features:**
`cell_diameter_um`, `nucleus_area_pct`, `chromatin_density`, `cytoplasm_ratio`, `circularity`, `eccentricity`, `granularity_score`, `lobularity_score`, `membrane_smoothness`, `cell_area_px`, `perimeter_px`

**Color / staining features:**
`mean_r`, `mean_g`, `mean_b`, `stain_intensity`

**Lab blood test values:**
`wbc_count_per_ul`, `rbc_count_millions_per_ul`, `hemoglobin_g_dl`, `hematocrit_pct`, `platelet_count_per_ul`, `mcv_fl`, `mchc_g_dl`

**Imaging settings:**
`magnification_x`, `image_resolution_px`

**Patient data:**
`patient_age_group` (0: Young, 1: Adult, 2: Elderly), `patient_sex` (0: Female, 1: Male)

> ⚠️ The following columns were excluded from training to avoid target leakage or because they are metadata only: `cell_id`, `disease_category`, `cell_type`, `dataset_source`, `staining_protocol`, `microscope_model`, `cytodiffusion_anomaly_score`, `cytodiffusion_classification_confidence`, `labeller_confidence_score`.

---

## 🤖 Model Comparison

Nine classification algorithms were trained and evaluated on the same train/test split. Results on the test set:

| Model | Accuracy | Precision | Recall | F1 Score |
|---|---|---|---|---|
| **XGBoost** ⭐ | **0.9787** | 0.9861 | 0.9468 | 0.9661 |
| Random Forest | 0.9694 | 0.9885 | 0.9149 | 0.9503 |
| Gradient Boosting | 0.9677 | 0.9913 | 0.9069 | 0.9472 |
| Decision Tree | 0.9260 | 0.8753 | 0.8963 | 0.8857 |
| SVM | 0.9209 | 0.9965 | 0.7553 | 0.8593 |
| KNN | 0.9090 | 0.9590 | 0.7473 | 0.8401 |
| AdaBoost | 0.9005 | 0.9331 | 0.7420 | 0.8267 |
| Logistic Regression | 0.8444 | 0.8386 | 0.6356 | 0.7231 |
| Naive Bayes | 0.7789 | 0.7117 | 0.5186 | 0.6000 |

**Selected model for deployment:** `XGBoost`, with an overall accuracy of **97.87%**, saved in `best_model.pkl` along with `scaler.pkl` for feature scaling.

> Note: Model performance is specific to this dataset and test split, and should not be generalized as an absolute benchmark without further external validation.

---

## 💻 Streamlit App (`appp.py`)

The app has 3 sections navigable from the sidebar:

### 1. Live Prediction
- Manually input all 26 features from the sidebar
- Click **Predict Anomaly Status**
- View the result (✅ Normal / ⚠️ Anomaly) along with the model's confidence score

### 2. Model Comparison
- An interactive table comparing the performance of all 9 models (Accuracy, Precision, Recall, F1)

### 3. Visualizations
- A bar chart comparing model accuracies
- A distribution plot for a sample of the `cell_diameter_um` feature

---

## ⚙️ Installation & Local Setup

### Requirements

```
streamlit>=1.28.0
pandas>=2.0.0
numpy>=1.24.0
scikit-learn>=1.3.0
joblib>=1.3.0
matplotlib>=3.7.0
seaborn>=0.12.0
xgboost>=1.7.0
```

### Steps to Run

```bash
# 1) Clone the repo or download all files into one folder
git clone <repo-url>
cd <repo-folder>

# 2) Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

# 3) Install dependencies
pip install -r requirements.txt

# 4) Run the app
streamlit run appp.py
```

Once running, the app will open automatically in your browser at:
`http://localhost:8501`

> Make sure `best_model.pkl` and `scaler.pkl` are in the same folder as `appp.py`; otherwise the app will fall back to Demo Mode with default placeholder values instead of real predictions.

---

## 🚀 Deployment

The app is currently deployed via **Streamlit Community Cloud** at:

👉 https://mycleanapp-cwfiw7gku84py84fhjsappx.streamlit.app/

---

## 🛠️ Tech Stack

- **Python 3**
- **Pandas / NumPy** – data processing
- **Scikit-learn** – modeling and evaluation (Logistic Regression, Decision Tree, Random Forest, AdaBoost, Gradient Boosting, SVM, KNN, Naive Bayes)
- **XGBoost** – final deployed model
- **Matplotlib / Seaborn** – exploratory data analysis (EDA)
- **Streamlit** – interactive app interface
- **Joblib** – saving/loading the model and scaler

---

## 📌 Notes

- Outliers in the blood-test variables were inspected but not removed, since they may represent real observations.
- `StandardScaler` was fit only on the training data to avoid leaking information from the test set.
- The train/test split was stratified to preserve the class balance between training and testing sets.

---

## 📄 License

This project is for educational and demonstration purposes only. Model outputs should not be relied upon as an actual medical diagnostic tool.

