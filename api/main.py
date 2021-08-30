from typing import Any, Dict

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello() -> Dict[str, Any]:
    return {"message": "Hello"}
