import json
from articolo import Articolo
class Magazzino:
    def __init__(self):
        self.articoli = []

    def inserisci_articolo(self, articolo):
        self.articoli.append(articolo)

    def elenco_articoli(self):
        return [str(articolo) for articolo in self.articoli]

    def rimuovi_articolo(self, codice_articolo):
        self.articoli = [articolo for articolo in self.articoli if articolo.codice_articolo != codice_articolo]

    def modifica_quantita(self, codice_articolo, nuova_quantita):
        for articolo in self.articoli:
            if articolo.codice_articolo == codice_articolo:
                articolo.quantita = nuova_quantita
                return True
        return False
    
    def modifica_prezzo(self,codice_articolo,nuovo_prezzo):
        for articolo in self.articoli:
            if articolo.codice_articolo == codice_articolo:
                articolo.prezzo = nuovo_prezzo
                return True
        return False

    def visualizza_articolo(self, codice_articolo):
        for articolo in self.articoli:
            if articolo.codice_articolo == codice_articolo:
                return str(articolo)
        return "Articolo non trovato."

    def carica_magazzino(self, filepath):
        with open(filepath, 'r') as file:
            data = json.load(file)
            self.articoli = [Articolo.from_json(json.dumps(item)) for item in data]

    def salva_magazzino(self, filepath):
        with open(filepath, 'w') as file:
            json.dump([json.loads(articolo.to_json()) for articolo in self.articoli], file)

    def valore_magazzino(self):
        return sum(articolo.prezzo * articolo.quantita for articolo in self.articoli)

    def media_valore_magazzino(self):
        totale_quantita = sum(articolo.quantita for articolo in self.articoli)
        return self.valore_magazzino() / totale_quantita if totale_quantita > 0 else 0
