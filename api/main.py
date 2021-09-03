import base64
import concurrent.futures
from io import BytesIO
import json
import time
from typing import Generator

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse

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
def create_map(radius: int = 500) -> StreamingResponse:
    with concurrent.futures.ThreadPoolExecutor() as thread_pool:
        future = thread_pool.submit(maps.create_map, radius)

    return StreamingResponse(map_iterator(future), media_type='application/json')


def map_iterator(future: concurrent.futures.Future[BytesIO]) -> Generator[str, None, None]:
    done = False
    while not done:
        time.sleep(0.1)
        yield " "
        done = future.done()

    buf = future.result()
    b64_map = base64.b64encode(buf.read())
    b64_map_str = b64_map.decode("utf-8")

    yield json.dumps({"map": b64_map_str})
