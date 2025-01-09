from pydantic import BaseModel
from typing import List
import json
import csv


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
    def modifica_parametri(self,codice_articolo: str,nuovo_codice:str,nuova_descrizione:str,nuovo_prezzo:float,nuova_quantita:int)->bool:
        for articolo in self.articoli:
            if nuovo_codice == articolo.codice_articolo:
               return False
        for articolo in self.articoli:
            if articolo.codice_articolo == codice_articolo:
                articolo.codice_articolo = nuovo_codice
                articolo.descrizione_articolo = nuova_descrizione
                articolo.prezzo = nuovo_prezzo
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
    
    def totale_quantita(self)->int:
        return sum(articolo.quantita for articolo in self.articoli)

    def carica_magazzino(self, filepath: str):
        with open(filepath, "r") as file:
            data = json.load(file)
            self.articoli = [Articolo(**item) for item in data]

    def salva_magazzino(self, filepath: str):
        with open(filepath, "w") as file:
            json.dump([articolo.dict() for articolo in self.articoli], file, indent=4)
            
    
            
    def esporta_csv(self, percorso: str) -> bool:
        try:
            with open(percorso, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                
                writer.writerow(["Codice Articolo", "Descrizione", "Prezzo", "Quantita'"])
                
                for articolo in self.articoli:
                    writer.writerow([
                        articolo.codice_articolo,
                        articolo.descrizione_articolo,
                        f"{articolo.prezzo:.2f}", 
                        articolo.quantita
                    ])
                valore = self.valore_magazzino()
                totale_q = self.totale_quantita()
                writer.writerow(["", "Totali",valore,f"{totale_q:.2f}"])
            
            return True
        except Exception as e:
            print(f"Errore durante l'esportazione: {e}")
            return False
        
   
        
    
    def importa_csv(self, percorso: str) -> List[str]:
        errori = []
        codici_esistenti = {articolo.codice_articolo for articolo in self.articoli}

        try:
            with open(percorso, mode="r", encoding="utf-8") as file:
                reader = csv.reader(file, delimiter=';', quotechar='"')

                intestazione = next(reader, None)
                    # if intestazione != ["Codice Articolo", "Descrizione", "Prezzo", "Quantita"]:
                    #     errori.append("Intestazione non valida nel file CSV.")
                    #     return errori

                for numero_riga, riga in enumerate(reader, start=2):
                    

                    codice, descrizione, prezzo, quantita = riga

                    if not codice:
                        errori.append(f"Riga {numero_riga}: Codice articolo mancante.")
                        continue

                    if codice in codici_esistenti:
                        errori.append(f"Riga {numero_riga}: Codice articolo '{codice}' già esistente.")
                        continue

                    try:
                        prezzo = float(prezzo)
                        quantita = int(quantita)

                        nuovo_articolo = Articolo(
                            codice_articolo=codice,
                            descrizione_articolo=descrizione,
                            prezzo=prezzo,
                            quantita=quantita
                        )
                        self.articoli.append(nuovo_articolo)
                        codici_esistenti.add(codice)
                    except ValueError:
                        errori.append(f"Riga {numero_riga}: Prezzo o quantità non validi.")

            if errori:
                return errori

            return None  

        except FileNotFoundError:
            return ["File non trovato."]
        except Exception as e:
            return [f"Errore durante l'importazione: {e}"]