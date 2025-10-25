import pickle
import glob
from fastapi import FastAPI
from pydantic import BaseModel

# Load model and DictVectorizer
# pipeline_file = 'pipeline_v1.bin'

# Find files matching pattern
files = glob.glob('pipeline_v*.bin')
if not files:
    raise FileNotFoundError("No pipeline file found matching pattern 'pipeline_v*.bin'")
# Pick the first match (or you could sort by version)
pipeline_file = files[0]

with open(pipeline_file, 'rb') as f_in:
    pipeline = pickle.load(f_in)

# Define FastAPI app
app = FastAPI(title="Prediction API", version="1.0")

class Customer(BaseModel):
    lead_source: str
    number_of_courses_viewed: int
    annual_income: float

@app.post("/predict")
def predict(customer: Customer):
    X = [customer.model_dump()]
    y_pred = pipeline.predict_proba(X)[:, 1]
    convert = y_pred >= 0.5

    result = {
        "convert_probability": float(y_pred),
        "convert": bool(convert)
    }
    return result

# For local dev run: uvicorn app:app --reload --host 0.0.0.0 --port 9696
