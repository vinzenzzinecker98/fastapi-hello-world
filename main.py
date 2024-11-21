
from fastapi import FastAPI, HTTPException
import os 
from dotenv import load_dotenv
load_dotenv()
our_key = os.environ["OUR_API_KEY"]

app = FastAPI(
              swagger_ui_parameters={"tryItOutEnabled": True},
              title="Virtual Support Bot",)#

@app.post("/hello_world")
def hello_world(req:str, key:str):
    if key == our_key:
        return f"hello world, got your {req}"
    else:
        raise HTTPException(status_code=401, detail="No key provided")