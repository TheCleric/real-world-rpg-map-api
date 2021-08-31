import base64
from typing import Any, Dict

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api import maps

app = FastAPI()

origins = ['https://thecleric.github.io']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def create_map(radius: int = 500) -> Dict[str, Any]:
    buf = maps.create_map(radius)
    b64_map = base64.b64encode(buf.read())
    b64_map_str = b64_map.decode("utf-8")

    return {"map": b64_map_str}
