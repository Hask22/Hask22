from fastapi import FastAPI
import joblib

app = FastAPI()

model = joblib.load("model.pkl")


@app.get("/")
def accueil():
    return {
       "message": "API ML fonctionne"
    }



@app.get("/predict/{valeur}")
def predict(valeur: int):

    prediction = model.predict([[valeur]])

    return {
       "prediction": prediction[0]
    }
