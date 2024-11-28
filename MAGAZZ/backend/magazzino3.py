from pydantic import BaseModel
from typing import List
import json


class Articolo(BaseModel):
    codice_articolo: str
    descrizione_articolo: str
    prezzo: float
    quantita: int

    def valore_totale(self) -> float:
        return self.prezzo * self.quantita

    def __str__(self) -> str:
        return f"Articolo(codice_articolo='{self.codice_articolo}', descrizione_articolo='{self.descrizione_articolo}', prezzo={self.prezzo}, quantita={self.quantita})"


class Magazzino:
    def __init__(self):
        self.articoli: List[Articolo] = []

    def inserisci_articolo(self, articolo: Articolo):
        # Verifica se il codice articolo è già presente
        if any(a.codice_articolo == articolo.codice_articolo for a in self.articoli):
            return False
        self.articoli.append(articolo)
        return True

    def elenco_articoli(self) -> List[Articolo]:
        return self.articoli

    def rimuovi_articolo(self, codice_articolo: str) -> bool:
        for articolo in self.articoli:
            if articolo.codice_articolo == codice_articolo:
                self.articoli.remove(articolo)
                return True
        return False

    def modifica_quantita(self, codice_articolo: str, nuova_quantita: int) -> bool:
        for articolo in self.articoli:
            if articolo.codice_articolo == codice_articolo:
                articolo.quantita = nuova_quantita
                return True
        return False
  

    def visualizza_articolo(self, codice_articolo: str) -> Articolo:
        for articolo in self.articoli:
            if articolo.codice_articolo == codice_articolo:
                return articolo
        return None

    def valore_magazzino(self) -> float:
        return sum(articolo.valore_totale() for articolo in self.articoli)

    def media_valore_magazzino(self) -> float:
        if not self.articoli:
            return 0.0
        return self.valore_magazzino() / len(self.articoli)

    def carica_magazzino(self, filepath: str):
        with open(filepath, "r") as file:
            data = json.load(file)
            self.articoli = [Articolo(**item) for item in data]

    def salva_magazzino(self, filepath: str):
        with open(filepath, "w") as file:
            json.dump([articolo.dict() for articolo in self.articoli], file, indent=4)
