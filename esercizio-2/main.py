from fastapi import FastAPI
from dataServices.service import Services

app = FastAPI()

@app.get("/validation")
async def validazione(CF : str, Email : str, numTel : int):
    arrayresult = []
    arrayresult.append(Services.validResult("CF", CF))
    arrayresult.append(Services.validResult("email", Email))
    arrayresult.append(Services.validResult("numTel", numTel))

    if "KO" in arrayresult:
        return "KO"
    return "OK"
