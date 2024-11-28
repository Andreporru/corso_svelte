from fastapi import FastAPI, HTTPException
from magazzino2 import Magazzino,Articolo
from typing import List

app = FastAPI()
magazzino = Magazzino()

@app.post("/articoli/")
def crea_articolo(articolo: Articolo):
    magazzino.inserisci_articolo(articolo)
    return {"message": "Articolo aggiunto con successo"}

@app.get("/articoli/", response_model=List[Articolo])
def lista_articoli():
    return magazzino.elenco_articoli()

@app.delete("/articoli/{codice_articolo}")
def elimina_articolo(codice_articolo: str):
    if magazzino.rimuovi_articolo(codice_articolo):
        return {"message": "Articolo rimosso con successo"}
    raise HTTPException(status_code=404, detail="Articolo non trovato")

@app.put("/articoli/{codice_articolo}")
def aggiorna_quantita(codice_articolo: str, nuova_quantita: int):
    if magazzino.modifica_quantita(codice_articolo, nuova_quantita):
        return {"message": "Quantità aggiornata con successo"}
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
def media_valore_articoli():
    return {"media_valore": magazzino.media_valore_magazzino()}
