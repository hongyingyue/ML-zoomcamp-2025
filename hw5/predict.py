import pickle
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression

pipeling_file = 'pipeline_v1.bin'

with open(pipeling_file, 'rb') as f_in:
    pipeline = pickle.load(f_in)

X = {
    "lead_source": "paid_ads",
    "number_of_courses_viewed": 2,
    "annual_income": 79276.0
}

y_pred = pipeline.predict_proba(X)[:, 1]
print(y_pred)
print()