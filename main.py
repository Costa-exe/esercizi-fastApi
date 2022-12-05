from fastapi import FastAPI
from dataServices.service import Services

app = FastAPI()

@app.get("/zip")
async def zipBytes(stringa : str): 
   return Services.zip(Services.FileGenerate('fileDiTesto', Services.bytes(stringa)))
