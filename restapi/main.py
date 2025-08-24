from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import db as db

app = FastAPI()
nicks_list = db.NicksDB()

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
    if nicks_list.check(nic):
        data = {"verified": True}
    else:
        data = {"verified": False}
    json_data = jsonable_encoder(data)
    return JSONResponse(content=json_data)

@app.get("/status")
def check_nick_other(nick):
    if nicks_list.check(nick):
        data = {"verified": True}
    else:
        data = {"verified": False}
    json_data = jsonable_encoder(data)
    return JSONResponse(content=json_data)


@app.get("/api/add_nick/{nick}")
def add_nick(nick):
    """
    Добавить ник в базу данных (через телеграм бота)
    """
    data = {"result": nicks_list.add(nick)}
    return JSONResponse(content=jsonable_encoder(data))

@app.get("/api/del_nick/{nick}")
def del_nick(nick):
    """
    Удалить ник из базы данных (через телеграм бота)
    """
    data = {"result": nicks_list.delete(nick)}
    return JSONResponse(content=jsonable_encoder(data))

@app.get("/api/save")
def save_db():
    """
    Сохранить состояние базы данных
    """
    data = nicks_list.save()
    return JSONResponse(content=jsonable_encoder(data))

@app.post("/api2/add_nick")
def add2(nick):
    pass