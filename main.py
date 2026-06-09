from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def read_root():
    return {"Hello": "World"}   

@app.get('login')
def login():
    return "Logged In Successfully"