from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.model_utils import predict_disease
from app.explain_utils import get_disease_explanation

app = FastAPI()

class SymptomInput(BaseModel):
    symptoms: list[str]

@app.post("/predict")
def predict(input_data: SymptomInput):
    try:
        disease = predict_disease(input_data.symptoms)
        return {"disease": disease}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/explain")
def explain(disease: str):
    try:
        explanation = get_disease_explanation(disease)
        return {"explanation": explanation}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))