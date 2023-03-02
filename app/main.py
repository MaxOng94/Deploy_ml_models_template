
from fastapi import FastAPI
from pydantic import BaseModel
from app.model.model import predict_pipeline
from app.model.model import __version__ as model_version


app = FastAPI()


# declaring that we want it to be string type
# type forcing the inputs and outputs to be both string type
class TextIn(BaseModel):
    text:str

class PredictionOut(BaseModel):
    language:str

@app.get("/")
async def home():
    return {"health_check": "OK", "model_version": model_version}

@app.post("/predict", response_model=PredictionOut)
def predict(payload: TextIn):
    # telling fastapi we want the input to be string, if not fastapi will raise an error
    language = predict_pipeline(payload.text)
    return {"language":language}