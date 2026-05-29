from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello Git + FastAPI OK 2605291118 test work flow!! "}