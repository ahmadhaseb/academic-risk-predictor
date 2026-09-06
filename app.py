import os
import joblib
import pandas as pd
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel

app = FastAPI(title="Student Academic AI Risk Prediction System")

# Automatic Absolute Path Resolution
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "Static")

# Static files mounting
app.mount("/Static", StaticFiles(directory=STATIC_DIR), name="Static")

# Load ML Model
MODEL_PATH = os.path.join(BASE_DIR, "AI_Student_Impact.pkl")
model = joblib.load(MODEL_PATH)

class StudentData(BaseModel):
    Age: float
    Gender: str
    Education_Level: str
    Daily_Social_Media_Hours: float
    Daily_AI_Tool_Usage_Hours: float
    Sleep_Hours: float
    Physical_Activity_Hours: float
    Mental_Health_Score: float
    Physical_Health_Score: float
    Social_Isolation_Score: float
    Burnout_Level: str
    Academic_Performance_Score: float

@app.get("/")
def home():
    return FileResponse(os.path.join(STATIC_DIR, "index.html"))

@app.post("/predict")
def predict_risk(data: StudentData):
    try:
        input_dict = data.dict()
        if input_dict.get("Gender") == "Non-Binary":
            input_dict["Gender"] = "Female"

        input_df = pd.DataFrame([input_dict])

        prediction_val = int(model.predict(input_df)[0])
        prob_val = float(model.predict_proba(input_df)[0][1]) if hasattr(model, "predict_proba") else float(prediction_val)

        return {
            "academic_failure_risk": prediction_val,
            "risk_probability": round(prob_val * 100, 2),
            "status": "High Risk" if prediction_val == 1 else "Safe/Low Risk"
        }
    except Exception as e:
        return {"error": str(e), "status_code": 500}