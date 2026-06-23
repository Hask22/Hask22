
from fastapi import FastAPI

app = FastAPI()



@app.get("/")
def accueil():
	return {
		"message": "API MLops fonctionne"

	}
