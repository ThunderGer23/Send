from fastapi import APIRouter
from os import listdir as ld
import ssl
from os import path as pth
from config.db import conn
import requests

routes = APIRouter()

@routes.get('/probando')
def getTest():
    lista = ld('./document')
    # for i in range(len(lista)):
    #     with open(f'./document/{lista[i]}', 'rb') as f:

    value = {
        "name": "documentoX.PDF",
        "id": ["13875943", '72452']
    }
    
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    print(f'Enviando {value}')
    response = requests.post("https://recive-production.up.railway.app/probando", headers=headers, json=value)
    # requests.post(f'https://recive-production.up.railway.app/probando/${value.name}')
    return 'ok'

@routes.post('/probando')
def postTest():
    print('Hola mundo2')
    return 'ok'