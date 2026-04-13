from typing import Any

from fastapi import FastAPI
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


@app.get("/user/{user_id}")
def get_user(user_id: int) -> dict[str, Any]:
    try:
        return {
            "user_id": user_id,
            "name": f"User {user_id}",
        }
    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
    )