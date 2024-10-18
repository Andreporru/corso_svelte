#!/usr/bin/env python3

from fastapi import FastAPI
from pydantic import BaseModel

class ReverseRequest(BaseModel):
    name:str
app = FastAPI()

@app.get("/hello")
async def _hello():
    return {"message":"Hello,world!"}

@app.get("/hello/{name}")
async def _hello_name(name: str):
    return {
        "message":"Hello, " + name,
        "name":name,
        "reverse": name[::-1],
    }

@app.post("/reverse")
async def _reverse(data: ReverseRequest):
    name=data.name
    
    return {
        "message":"Hello, " + name,
        "name":name,
        "reverse": name[::-1],
    }