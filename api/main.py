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

    return {"map": buf.read().decode('utf-8')}
