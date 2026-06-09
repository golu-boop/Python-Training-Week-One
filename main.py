from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def read_root():
    return {"Hello": "World"}   

<<<<<<< HEAD
@app.get('login')
def login():
    return "Logged In Successfully"
=======
@app.get("signout")
def sign_out():
    return {"message": "You have been signed out."}
>>>>>>> signout
