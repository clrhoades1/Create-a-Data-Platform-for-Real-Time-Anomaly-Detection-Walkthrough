from fastapi import FastAPI
from joblib import load

model = load("model.joblib")


app = FastAPI()

@app.post("/prediction")
async def prediction(feature_vector : list, score: bool):
    response = {"is_inlier": model.predict(feature_vector)[0]}



    if(score):
        response["anomaly_score"]=model.anomaly_score(feature_vector)[0]

    return response

@app.get("/model_information")
async def model_information():
    return model.get_params()
