from fastapi import FastAPI
from dataServices.service import Services
import random
from pydantic import BaseModel


class Item(BaseModel):
    ID: int
    CF: str
    Email: str
    NumTelefono: int

app = FastAPI()

@app.get("/zip")
async def zipBytes(stringa : str):
    with open(Services.zip(Services.FileGenerate('fileDiTesto', Services.bytes(stringa))), 'rb') as file_data:
        bytes_content = file_data.read()
        return bytes_content.hex()

@app.post("/insertClient")
async def validazione(item : Item):
    result = {}
    result['ID'] = Services.validResult("IdAnagrafica", item.ID)
    result['CF'] = Services.validResult("CF", item.CF)
    result['E-mail'] = Services.validResult("email", item.Email)
    result['Numero di Telefono'] = Services.validResult("numTel", item.NumTelefono)

    idsap = random.randint(10000000000, 99999999999)

    for x, y in result.items():
        if y == "Not Valid":
            return {"Validation" : "KO",
                    "Error" : f"formato di '{x}' non valido",
                    "ID-SAP": None}
    
    return {"Validation" : "OK",
            "Error" : "No Errors",
            "ID-SAP": idsap}