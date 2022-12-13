import os
from zipfile import ZipFile
from fastapi import FastAPI, UploadFile
import random
from pydantic import BaseModel


class Item(BaseModel):
    ID: int
    CF: str
    Email: str
    NumTelefono: int

app = FastAPI()

@app.post("/zipit/")
async def create_upload_file(file: UploadFile):

  filename = file.filename[:file.filename.__len__()-4:1]
  PDFNAME = f'{filename}.pdf'
  ZIPNAME = f'{filename}.zip'
  _pdf = open(PDFNAME, "wb")
  _pdf.write(file.file.read());
  _pdf.close()
  
  with ZipFile(ZIPNAME, 'w') as zip:
    zip.write(os.path.basename(PDFNAME))
  
  os.remove(PDFNAME)
  zipped = open(ZIPNAME, 'rb')
  b_array = zipped.read()
  zipped.close()
  os.remove(ZIPNAME)
  return {'zipped' : str(b_array)}

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