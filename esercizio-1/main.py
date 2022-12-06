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
    arrayresult = {}
    arrayresult['ID'] = Services.validResult("IdAnagrafica", id)
    arrayresult['CF'] = Services.validResult("CF", CF)
    arrayresult['E-mail'] = Services.validResult("email", Email)
    arrayresult['Numero di Telefono'] = Services.validResult("numTel", numTel)

    for x, y in arrayresult.items():
        if y == "Not Valid":
            return f"formato di '{x}' non valido"
    
    return arrayresult