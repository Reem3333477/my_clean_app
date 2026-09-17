from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI(title="Blood Cell Anomaly Detection API", version="1.0")

# تحميل الموديل والـ Scaler
model = joblib.load('best_model.pkl')
scaler = joblib.load('scaler.pkl')

# تعريف كلاس يستقبل مصفوفة/لستة من الـ Features (مهما كان عددها)
class BloodSample(BaseModel):
    features: list[float]

@app.post("/predict")
def predict_anomaly(sample: BloodSample):
    try:
        # التأكد إن الـ input عبارة عن مصفوفة ثنائية الأبعاد بالشكل الصحيح
        input_data = np.array([sample.features])
        
        # توحيد مقياس البيانات بالـ Scaler (هياخد الـ 26 ميزة مظبوط)
        scaled_data = scaler.transform(input_data)
        
        # التنبؤ بالموديل
        prediction = model.predict(scaled_data)
        
        result = "Anomaly Detected" if prediction[0] == 1 else "Normal Cell"
        return {
            "status": "success",
            "prediction_code": int(prediction[0]),
            "result": result
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}