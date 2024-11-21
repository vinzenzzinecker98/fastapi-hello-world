from fastapi import FastAPI


app = FastAPI(
              swagger_ui_parameters={"tryItOutEnabled": True},
              title="Virtual Support Bot",)#

@app.post("/hello_world")
def hello_world(req:str):
    return f"hello world, got your {req}"