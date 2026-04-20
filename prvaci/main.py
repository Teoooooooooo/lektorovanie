from typing import Any

from fastapi import FastAPI, Request
import uvicorn

app: FastAPI = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello world"}


@app.get("/test/1")
def test():
    return {"message": "This is a test endpoint"}

@app.get("/test/2")
def test1():
    return {"message": "Hahahah hehehe"}

<<<<<<< Updated upstream
=======
@app.get("/teovacesta")
def teo():
    return {"pi" : "3.1415926535897932384626"}
>>>>>>> Stashed changes

@app.get("/user/{user_id}")
def get_user(user_id: int) -> dict[str, Any]:
    try:
        return {
            "user_id": user_id,
            "name": f"User {user_id}",
        }
    except Exception as e:
        return {"error": str(e)}
    
@app.post("/echo")
async def echo(request: Request):
    body = await request.json()
    return {"my_answer": body["input"],
            "moje_mone": body["meno"]}

@app.post("{/scitanie")
async def scitanie(request: Request):
    body = await request.json()
    return {"sucet": body["cislo1"] + body["cislo2"]}

@app.post("/odcitanie")
async def odcitanie(request: Request):
    body = await request.json()
    return {"sucet": body["cislo1"] - body["cislo2"]}

@app.post("/nasobenie")
async def nasobenie(request: Request):
    body = await request.json()
    return {"sucet": body["cislo1"] * body["cislo2"]}

@app.post("/delenie")
async def delenie(request: Request):
    body = await request.json()
    return {"sucet": body["cislo1"] / body["cislo2"]}


@app.get("/scitanie/{cislo1}/{cislo2}")
async def scitanie(cislo1: int,cislo2: int):
    return {"sucet": cislo1 + cislo2}

@app.post("/spojenie")
async def spojenie(request: Request):
    body = await request.json()
    return {"vysledok": body["meno"] + " " + body["priezvysko"]}
    
@app.post("/login")
async def login(request: Request):
    body = await request.json()
    if(body["username"] == "admin" and body["password"] == "heslo"):
        return {"message" : "login succesfull"}
    else:
        return {"message" : "login failed"}
        
    


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8005,
        reload=True,
    )