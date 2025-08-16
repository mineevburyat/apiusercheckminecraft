from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
 
app = FastAPI()
 
@app.get("/")
def root():
    data = {"message": "Hello METANIT.COM", 
            "url": "https://metanit.com/python/fastapi/1.6.php"}
    json_data = jsonable_encoder(data)
    return JSONResponse(content=json_data)

@app.get("/api/check_player/")
def check_player():
    data = {"verified": True}
    json_data = jsonable_encoder(data)
    return JSONResponse(content=json_data)
    
@app.get("/api/check_nick/{nic}")
def check_nick(nic):
    nick_list = ["mineev", "KacPsi"]
    if nic in nick_list:
        data = {"verified": True}
    else:
        data = {"verified": False}
    json_data = jsonable_encoder(data)
    return JSONResponse(content=json_data)

@app.get("/status")
def check_nick_other(nick):
    nick_list = ["mineev", "KacPsi"]
    if nick in nick_list:
        data = {"verified": True}
    else:
        data = {"verified": False}
    json_data = jsonable_encoder(data)
    return JSONResponse(content=json_data)