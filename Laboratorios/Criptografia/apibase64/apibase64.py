from pydoc import text
from fastapi import FastAPI
from modelodatos import ModeloDatos
import base64  


app: FastAPI = FastAPI(
    title = "TalentoTech - API Cifrado Base64", 
    description = "API Cifrado Base64"
)

@app.get(
    "/cifrarbase64", 
    summary = "Base64",
    description = "Cifrar Base64", 
    tags = ["Base64"]
)

async def cifrar_base64(textoplano):
    mensaje_bytes = textoplano.encode('utf-8')
    textocifrado = base64.b64encode(mensaje_bytes)
    return textocifrado.decode('utf-8')

@app.get(
    "/descifrarbase64", 
    summary = "Base64",
    description = "Descifrar Base64", 
    tags = ["Base64"]
)

async def descifrar_base64(textocifrado):
    textoplano_bytes = base64.b64decode(textocifrado)
    return textoplano_bytes.decode('utf-8')


@app.post(
    "/cifrarbase64", 
    summary = "Base64",
    description = "Cifrar Base64", 
    tags = ["Base64"]
)

async def cifrar_base64(textoplano: ModeloDatos):
    textoplano.Texto = cifrarbase64(textoplano.Texto)
    return textoplano

@app.post(
    "/decifrarbase64", 
    summary = "Base64",
    description = "Cifrar Base64", 
    tags = ["Base64"]
)


async def descifrar_base64_json(textocifrado: ModeloDatos):
    textocifrado.Texto = descifrarbase64(textocifrado.Texto)
    return textocifrado

def cifrarbase64(textoplano):
    mensaje_bytes = textoplano.encode('utf-8')
    textocifrado = base64.b64encode(mensaje_bytes)
    return textocifrado.decode('utf-8')


def descifrarbase64(textocifrado):
    textoplano_bytes = base64.b64decode(textocifrado)
    return textoplano_bytes.decode('utf-8')