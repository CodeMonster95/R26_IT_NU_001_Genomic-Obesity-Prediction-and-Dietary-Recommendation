"""
XGBoost Model Training on REAL UCI Obesity Dataset
IT22182500 - I. Farshad
"""

import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from xgboost import XGBClassifier
import shap

print("=" * 70)
print("TRAINING MODEL ON REAL UCI DATASET")
print("=" * 70)

# Load real dataset
print("\n[1/5] Loading REAL dataset...")
try:
    df = pd.read_csv('data/obesity_real_dataset.csv')
    print(f"    ✓ Loaded {len(df)} REAL records")
    print(f"    📚 Source: UCI ML Repository (Palechor & De la Hoz, 2019)")
except FileNotFoundError:
    print("    ✗ Dataset not found! Run: python download_real_dataset.py")
    exit(1)

# Prepare features
print("\n[2/5] Preparing features...")
features = ['GRS_Score', 'Physical_Activity_Mins_Week', 'Dietary_Quality_Index',
            'Sleep_Hours_Night', 'Age', 'BMI', 'Gender_Encoded']

X = df[features]
y = df['Target_Obesity']

print(f"    ✓ Features: {len(features)}")
print(f"    ✓ Samples: {len(df)}")
print(f"    ✓ Obese: {y.sum()} ({y.mean()*100:.1f}%)")

# Split
print("\n[3/5] Splitting dataset...")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
print(f"    ✓ Training: {len(X_train)} samples")
print(f"    ✓ Testing: {len(X_test)} samples")

# Train
print("\n[4/5] Training XGBoost model...")
model = XGBClassifier(
    n_estimators=100,
    max_depth=6,
    learning_rate=0.1,
    random_state=42,
    eval_metric='logloss'
)

model.fit(X_train, y_train)
print("    ✓ Training complete!")

# Evaluate
print("\n[5/5] Evaluating performance...")
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"\n    📊 Test Accuracy: {accuracy:.3f} ({accuracy*100:.1f}%)")
print("\n    Classification Report:")
print(classification_report(y_test, y_pred, target_names=['Not Obese', 'Obese']))

# Feature importance
print("\n    🎯 Feature Importance:")
for i, imp in enumerate(model.feature_importances_):
    print(f"       {features[i]:<30} {imp:.4f}")

# Save model
print("\n[6/5] Saving model...")
with open('models/obesity_xgboost_model.pkl', 'wb') as f:
    pickle.dump(model, f)
print("    ✓ Model saved: models/obesity_xgboost_model.pkl")

with open('models/feature_names.pkl', 'wb') as f:
    pickle.dump(features, f)
print("    ✓ Features saved")

with open('models/gender_encoder.pkl', 'wb') as f:
    pickle.dump({0: 'Male', 1: 'Female'}, f)
print("    ✓ Encoder saved")

# SHAP
print("\n[BONUS] Initializing SHAP...")
explainer = shap.TreeExplainer(model)
with open('models/shap_explainer.pkl', 'wb') as f:
    pickle.dump(explainer, f)
print("    ✓ SHAP explainer saved")

print("\n" + "=" * 70)
print("✅ MODEL TRAINING COMPLETE!")
print("=" * 70)
print(f"\n📊 Final Results:")
print(f"   Accuracy: {accuracy*100:.1f}%")
print(f"   Dataset: 2,111 real participants (UCI)")
print(f"   Citation: Palechor & De la Hoz (2019)")
print("\n🎯 Next: python -m streamlit run app.py")
print("=" * 70)
