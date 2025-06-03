from fastapi import FastAPI, HTTPException, Query
from typing import Optional, List
import requests
import os
import json

app = FastAPI()

OUTPUT_FOLDER = "dados"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

# Carregar URLs do arquivo externo
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
URLS_PATH = os.path.join(BASE_DIR, "options.json")

with open(URLS_PATH, "r", encoding="utf-8") as f:
    URLS = json.load(f)

def download_file(name: str, url: str):
    output_path = os.path.join(OUTPUT_FOLDER, f"{name}.pdf")
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        with open(output_path, "wb") as f:
            f.write(response.content)
        return output_path
    except requests.RequestException as e:
        raise RuntimeError(f"Erro ao baixar {name}: {e}")

@app.get("/baixar/producao")
def baixar_producao():
    url = "http://vitibrasil.cnpuv.embrapa.br/download/Producao.csv"
    caminho = download_file("producao", url)
    return {"mensagem": f"Arquivo 'producao.pdf' salvo em {caminho}"}

@app.get("/baixar/processamento")
def baixar_processamento(subgrupos: Optional[List[str]] = Query(
        None,
        description="Opções: " + ", ".join(URLS["processamento"].keys())
    )):
    baixados = []
    if subgrupos is None:
        subgrupos = list(URLS["processamento"].keys())

    for subgrupo in subgrupos:
        if subgrupo not in URLS["processamento"]:
            raise HTTPException(status_code=400, detail=f"Subgrupo inválido: {subgrupo}")
        url = URLS["processamento"][subgrupo]
        caminho = download_file(f"processamento_{subgrupo}", url)
        baixados.append(caminho)

    return {"mensagem": f"{len(baixados)} arquivo(s) salvos", "arquivos": baixados}

@app.get("/baixar/comercializacao")
def baixar_comercializacao():
    url = "http://vitibrasil.cnpuv.embrapa.br/download/Comercio.csv"
    caminho = download_file("comercializacao", url)
    return {"mensagem": f"Arquivo 'comercializacao.pdf' salvo em {caminho}"}

@app.get("/baixar/importacao")
def baixar_importacao(subgrupos: Optional[List[str]] = Query(
        None,
        description="Opções: " + ", ".join(URLS["importacao"].keys())
    )):
    baixados = []
    if subgrupos is None:
        subgrupos = list(URLS["importacao"].keys())

    for subgrupo in subgrupos:
        if subgrupo not in URLS["importacao"]:
            raise HTTPException(status_code=400, detail=f"Subgrupo inválido: {subgrupo}")
        url = URLS["importacao"][subgrupo]
        caminho = download_file(f"importacao_{subgrupo}", url)
        baixados.append(caminho)

    return {"mensagem": f"{len(baixados)} arquivo(s) salvos", "arquivos": baixados}

@app.get("/baixar/exportacao")
def baixar_exportacao(subgrupos: Optional[List[str]] = Query(
        None,
        description="Opções: " + ", ".join(URLS["exportacao"].keys())
    )):
    baixados = []
    if subgrupos is None:
        subgrupos = list(URLS["exportacao"].keys())

    for subgrupo in subgrupos:
        if subgrupo not in URLS["exportacao"]:
            raise HTTPException(status_code=400, detail=f"Subgrupo inválido: {subgrupo}")
        url = URLS["exportacao"][subgrupo]
        caminho = download_file(f"exportacao_{subgrupo}", url)
        baixados.append(caminho)

    return {"mensagem": f"{len(baixados)} arquivo(s) salvos", "arquivos": baixados}
