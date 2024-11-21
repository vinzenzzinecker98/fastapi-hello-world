
from fastapi import FastAPI, HTTPException
import os 
from dotenv import load_dotenv

def get_key():
    load_dotenv()
    key =  os.environ["OUR_API_KEY"]
    print(f"loaded key {key}")
    return key

our_key = get_key()

app = FastAPI(
              swagger_ui_parameters={"tryItOutEnabled": True},
              title="Virtual Support Bot",)#

@app.post("/hello_world")
def hello_world(req:str, key:str):
    print(f"got request, key is {key}")
    if key == our_key:
        print("key is fine")
        return f"hello world, got your {req}"
    else:
        print("key is absolutely not fine")
        raise HTTPException(status_code=401, detail="No key provided")