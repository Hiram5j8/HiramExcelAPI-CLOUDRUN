from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello Git + FastAPI OK 260529145 test work flow!!OK "}