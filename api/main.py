from typing import Any, Dict

from fastapi import FastAPI

import api.maps as maps

app = FastAPI()


@app.get("/")
def create_map(radius: int = 500) -> Dict[str, Any]:
    buf = maps.create_map(radius)

    return {"map": buf.read().decode('utf-8')}
