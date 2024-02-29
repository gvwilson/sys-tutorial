from fastapi import FastAPI
import os
import pandas as pd
import uvicorn
import sys

sandbox, filename = sys.argv[1], sys.argv[2]
os.chdir(sandbox)
df = pd.read_csv(filename)

app = FastAPI()

@app.get("/")
async def get_birds(year: int = None, species: str = None):
    result = df.copy()
    if species is not None:
        result = result[result["species_id"] == species]
    if year is not None:
        result = result[result["year"] == year]
    result["num"].fillna(0, inplace=True)
    return result.to_dict(orient="records")

uvicorn.run(app)
