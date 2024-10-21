from fastapi import FastAPI, Request, Response, HTTPException, Header
import pandas as pd

df = pd.read_csv("properties_rent.csv").T.to_dict()

app = FastAPI()

@app.get("/")
def home():
  result = []
  for k, v in df.items():
    result.append(v['price'])
  unique_prices = list(set(result))
  unique_prices = sorted(unique_prices)
  return {"message": "success", "unique_prices_sorted": unique_prices, "length": len(unique_prices)}