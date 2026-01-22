import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException

load_dotenv()

app = FastAPI()

API = os.getenv("API")
print("API FROM ENV =", repr(API))

@app.get("/")
def read_root():
    return {"msg": "Hello from Everest region, Nepal!", "v": "0.1"}


@app.get("/protected")
def read_protected(api_key: str = None):
    if not api_key or api_key != API:
        raise HTTPException(status_code=401, detail="Unauthorized access")

    return {"msg": "Welcome to the protected route!"}
