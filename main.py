from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import numpy as np
import pickle

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Templates folder
templates = Jinja2Templates(directory="templates")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Input schema
class HouseData(BaseModel):
    sqft: float
    bedrooms: int

# 🔷 Serve HTML page
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# 🔷 Prediction API
@app.post("/predict")
def predict(data: HouseData):
    features = np.array([[data.sqft, data.bedrooms]])
    prediction = model.predict(features)[0]

    return {"predicted_price": round(prediction, 2)}