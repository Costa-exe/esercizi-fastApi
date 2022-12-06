from fastapi import FastAPI
from dataServices.service import Services

app = FastAPI()

@app.get("/zip")
async def zipBytes(stringa : str):
    with open(Services.zip(Services.FileGenerate('fileDiTesto', Services.bytes(stringa))), 'rb') as file_data:
        bytes_content = file_data.read()
        return bytes_content.hex()

@app.get("/validation")
async def validazione(id : int, CF : str, Email : str, numTel : int):
    arrayresult = []
    arrayresult.append(Services.validResult("IdAnagrafica", id))
    arrayresult.append(Services.validResult("CF", CF))
    arrayresult.append(Services.validResult("email", Email))
    arrayresult.append(Services.validResult("numTel", numTel))

    if "KO" in arrayresult:
        return "KO"
    return arrayresult[0]