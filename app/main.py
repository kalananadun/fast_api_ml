import pandas as pd
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel
import pickle
app = FastAPI()


class Item(BaseModel):
    longitude: float
    latitude:  float
    housing_median_age: float
    total_rooms: float
    total_bedrooms: float
    median_income: float
    ocean_proximity: int


filename = 'model.pkl'

with open(filename, 'rb') as file:
    model = pickle.load(file)


@app.post("/")
async def predict_price(item: Item):
    df = pd.DataFrame([item.dict().values()], columns=item.dict().keys())
    yhat = model.predict(df)
    return {"predicted_price": float(yhat)}
