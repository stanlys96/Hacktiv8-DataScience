from fastapi import FastAPI, Request, Response, HTTPException, Header
import pandas as pd
import json

app = FastAPI()

API_KEY = "WalaoehASD"

data = {
  "New York City": {
    "temperature": "30 degrees Fahrenheit",
    "condition": "Calm"
  },
  "Los Angeles": {
    "temperature": "50 degrees Fahrenheit",
    "condition": "Chaos"
  },
  "Chicago": {
    "temperature": "60 degrees Fahrenheit",
    "condition": "Michael Jordan"
  }
}

@app.get("/weather/{location}")
def get_location(location):
  if location not in data.keys():
    raise HTTPException(status_code=404, detail=f"Location {location} not found")
  return data[location]

@app.get("/authenticate")
def authentication(api_key: str = Header(None)):
  if api_key is None or api_key != API_KEY:
    raise HTTPException(status_code=401, detail="Invalid API Key")

  return {"message": "You got the correct API key!", "data": data}