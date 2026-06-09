import fastapi from FastAPI

app = FastAPI()
@app.get("/")
def read_root():
    return {"Hello": "World"}   

@app.get("signout")
def sign_out():
    return {"message": "You have been signed out."}