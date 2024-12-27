#!/usr/bin/env python3
from fastapi import FastAPI, HTTPException
from magazzino3 import Magazzino,Articolo
from fastapi.middleware.cors import CORSMiddleware
from typing import List
magazzino = Magazzino()
app = FastAPI()
filepath="data.json"

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/articoli/")
def crea_articolo(articolo: Articolo):
    if magazzino.inserisci_articolo(articolo):
        magazzino.salva_magazzino(filepath)  
        return {"message": "Articolo aggiunto con successo"}
    raise HTTPException(status_code=409, detail="l'articolo con il codice inserito esiste già.")


@app.get("/articoli/", response_model=List[Articolo])
def lista_articoli():
    magazzino.carica_magazzino(filepath)
    return magazzino.elenco_articoli()

@app.delete("/articoli/{codice_articolo}")
def elimina_articolo(codice_articolo: str):
    if magazzino.rimuovi_articolo(codice_articolo):
        magazzino.salva_magazzino(filepath)
        return {"message": "Articolo rimosso con successo"}
    raise HTTPException(status_code=404, detail="Articolo non trovato")

@app.put("/articoli/{codice_articolo}")
def aggiorna_quantita(codice_articolo: str, nuova_quantita: int):
    if magazzino.modifica_quantita(codice_articolo, nuova_quantita):
        magazzino.salva_magazzino(filepath)
        return {"message": "Quantità aggiornata con successo"}
    raise HTTPException(status_code=404, detail="Articolo non trovato")

@app.put("/articoli/mod/{codice_articolo}")
def aggiorna_articolo(codice_articolo:str,nuovo_codice:str,nuova_descrizione:str,nuovo_prezzo:float,nuova_quantita:int):
    if magazzino.modifica_parametri(codice_articolo,nuovo_codice,nuova_descrizione,nuovo_prezzo,nuova_quantita):
        magazzino.salva_magazzino(filepath)
        return{"message":"Articolo aggionrnato con successo"}
    raise HTTPException(status_code=404, detail="Articolo non trovato")

@app.get("/articoli/{codice_articolo}", response_model=Articolo)
def dettaglio_articolo(codice_articolo: str):
    articolo = magazzino.visualizza_articolo(codice_articolo)
    if articolo:
        return articolo
    raise HTTPException(status_code=404, detail="Articolo non trovato")

@app.get("/magazzino/valore")
def valore_totale_magazzino():
    return {"valore_totale": magazzino.valore_magazzino()}

@app.get("/magazzino/media")
def media_valore_magazzino():
    media = magazzino.media_valore_magazzino()
    return {"media": media}

@app.get("/magazzino/export/{percorso}")
def esporta_csv(percorso: str):
    magazzino.carica_magazzino(filepath)
    res = magazzino.esporta_csv(percorso)
    if res:
        return {"message": "File esportato con successo"}
    raise HTTPException(status_code=404, detail="Percorso non trovato")

@app.get("/magazzino/exportPdf/{percorso}")
def esporta_pdf(percorso:str):
    magazzino.carica_magazzino(filepath)
    res=magazzino.esporta_pdf(percorso)
    if res:
        return {"message":"File esportato con successo"}
    raise HTTPException(status_code=404,detail="Percorso non trovato")




@app.post("/magazzino/import/{percorso}")
def importa_csv(percorso: str):
    magazzino.carica_magazzino(filepath)
    errori = magazzino.importa_csv(percorso)
    if errori:
        raise HTTPException(status_code=400, detail=errori)
    magazzino.salva_magazzino(filepath)
    return {"message": "Importazione completata con successo."}


