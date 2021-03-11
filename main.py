from typing import Optional
from fastapi import FastAPI
from operation.service import get_time
from typing import List

app = FastAPI(title="Swahiliflix reminder")

@app.post("/get_time", tags=['Get Time'])
def read_time(time_list: List):
    return get_time(time_list)