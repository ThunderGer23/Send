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
    ids = []
    for i in range(len(lista)):
        with open(f'./document/{lista[i]}', 'rb') as f:
            ids.append(str(conn.local.files.insert_one({ "name": lista[i], "data": f.read() }).inserted_id))
    value = {
        "id": ids,
    }
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    response = requests.post("https://recive-production.up.railway.app/probando", headers=headers, json=value)
    # response = requests.post("http://localhost:8005/probando", headers=headers, json=value)    
    return 'ok'

@routes.post('/probando')
def postTest():
    print('Hola mundo2')
    return 'ok'