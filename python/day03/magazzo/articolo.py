#!/usr/bin/env python3
import json

class Articolo:
    def __init__(self,codice_articolo,descrizione_articolo,prezzo,quantita):
        self.codice_articolo=codice_articolo
        self.descrizione_articolo = descrizione_articolo
        self.prezzo = prezzo
        self.quantita = quantita
    
    @staticmethod
    def from_json(json_data):
        data = json.loads(json_data)
        return Articolo(
            data['codice_articolo'],
            data['descrizione_articolo'],
            data['prezzo'],
            data['quantita']
        )
    
    def to_json(self):
        return json.dumps({
            'codice_articolo':self.codice_articolo,
            'descrizione_articolo':self.descrizione_articolo,
            'prezzo':self.prezzo,
            'quantita':self.quantita
        })
    
    def __str__(self):
        return (f"Codice: {self.codice_articolo}, Descrizione: {self.descrizione_articolo},"
                f"Prezzo: {self.prezzo:.2f}, Quantità:{self.quantita}")
                
