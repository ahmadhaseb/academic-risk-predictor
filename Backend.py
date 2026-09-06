from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd



app = FastAPI(title="Student Academic AI Risk Prediction API")


#Load Trained Pipeline
model = joblib.load("AI_Student_Impact.pkl")

#Input Schema Validation
class StudentData(BaseModel):
    Age: float
    Gender:str
    Education_Level:str
    Daily_Social_Media_Hours:float
    Daily_AI_Tool_Usage_Hours:float
    Sleep_Hours:float
    Physical_Activity_Hours:float
    Mental_Health_Score:float
    Physical_Health_Score:float
    Social_Isolation_Score:float
    Burnout_Level:str
    Academic_Performance_Score:float

@app.get("/")
def home():
    return {"status":"API is running successfully"}
@app.post("/predict")
def predict_risk(data: StudentData):
    try:
        # Convert Pydantic model to dict
        input_dict = data.dict()
        input_df = pd.DataFrame([input_dict])

        # Prediction execute karein
        prediction_val = int(model.predict(input_df)[0])

        if hasattr(model, "predict_proba"):
            prob_val = float(model.predict_proba(input_df)[0][1])
        else:
            prob_val = float(prediction_val)

        return {
            "academic_failure_risk": prediction_val,
            "risk_probability": round(prob_val * 100, 2),
            "status": "High Risk" if prediction_val == 1 else "Safe/Low Risk"
        }
    except Exception as e:
        # Agar Gender encoding ya kisi waja se error aaye to backend crash hone se bachayen
        print("Backend Prediction Error:", str(e))
        return {
            "academic_failure_risk": 0,
            "risk_probability": 0.0,
            "status": f"Encoding Error: {str(e)}"
        }

