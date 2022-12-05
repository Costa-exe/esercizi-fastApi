from fastapi import FastAPI
from dataServices.service import Services

app = FastAPI()

@app.get("/zip")
async def zipBytes(stringa : str):
    with open(Services.zip(Services.FileGenerate('fileDiTesto', Services.bytes(stringa))), 'rb') as file_data:
        bytes_content = file_data.read()
        return bytes_content.hex()
