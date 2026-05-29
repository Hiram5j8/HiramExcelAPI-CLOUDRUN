from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello Git + FastAPI OK 26052915555555555 "}