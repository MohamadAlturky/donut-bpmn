from fastapi import FastAPI

app = FastAPI()

@app.post("/patient/create")
def home(int: int):
    return int
