from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"Message": "Hello, world!, First Program"}

