from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import dill as pkl

model = pkl.load(open("model.pkl", "rb"))

y_encode = pkl.load(open("y_encode.pkl", "rb"))

X_pipeline = pkl.load(open("X_pipeline.pkl", "rb"))

y_encoder = y_encode["y_encoder"]

app = FastAPI()

class InputData(BaseModel):
    Age: int
    Height: float
    Weight: float
    FCVC: float
    NCP: float
    CH2O: float
    FAF: float
    TUE: float
    Gender: str
    family_history_with_overweight: str
    FAVC: str
    SMOKE: str
    SCC: str
    CAEC: str
    CALC: str
    MTRANS: str

@app.post("/predict")
def predict(data: InputData):
    data_dict = data.model_dump()
    sample = pd.DataFrame([data_dict])

    sample = X_pipeline.transform(sample)
    pred = model.predict(sample)

    label = y_encoder.inverse_transform(pred.reshape(-1, 1))[0][0]
    return {"prediction": label}
