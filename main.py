from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import pickle

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS (VERY IMPORTANT)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

# Input schema
class HouseData(BaseModel):
    sqft: float
    bedrooms: int

# API endpoint
@app.post("/predict")
def predict(data: HouseData):
    features = np.array([[data.sqft, data.bedrooms]])
    prediction = model.predict(features)[0]

    return {
        "predicted_price": round(prediction, 2)
    }