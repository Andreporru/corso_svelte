from magazzino import Magazzino
from articolo import Articolo


def main():
    magazzino = Magazzino()
    filepath="data.json"
    magazzino.carica_magazzino(filepath)
   

    

    while True:
        print("\nMenu Magazzino")
        print("1. Inserisci Articolo")
        print("2. Elenco Articoli")
        print("3. Rimuovi Articolo")
        print("4. Modifica Quantità")
        print("5. Modifica Prezzo")
        print("6. Visualizza Articolo")
        print("7. Salva Magazzino su File")
        print("8. Calcola Valore Totale Magazzino")
        print("9. Calcola Media Valore Magazzino")
        print("0. Esci")
        scelta = input("Seleziona un'opzione: ")

        if scelta == "1":
            codice = input("Codice Articolo: ")
            descrizione = input("Descrizione Articolo: ")
            prezzo = float(input("Prezzo: "))
            quantita = int(input("Quantità: "))
            magazzino.inserisci_articolo(Articolo(codice, descrizione, prezzo, quantita))
            magazzino.salva_magazzino(filepath)

        elif scelta == "2":
            print("\nElenco Articoli:")
            for articolo in magazzino.elenco_articoli():
                print(articolo)
            input("")

        elif scelta == "3":
            codice = input("Codice Articolo da rimuovere: ")
            magazzino.rimuovi_articolo(codice)
            magazzino.salva_magazzino(filepath)

        elif scelta == "4":
            codice = input("Codice Articolo da modificare: ")
            quantita = int(input("Nuova Quantità: "))
            if magazzino.modifica_quantita(codice, quantita):
                print("Quantità aggiornata.")
                magazzino.salva_magazzino(filepath)
            else:
                print("Articolo non trovato.")
            
        elif scelta =="5":
            codice=input("Codcie articolo da modificare: ")
            prezzo= float(input("Nuovo Prezzo: "))
            if magazzino.modifica_prezzo(codice,prezzo):
                print("Prezzo aggiornato.")
            else:
                print("Articolo non trovato.")
                
                
        elif scelta == "6":
                codice = input("Codice Articolo da visualizzare: ")
                print(magazzino.visualizza_articolo(codice))
    

      
            
        

        elif scelta == "7":
            filepath = "data.json"
            magazzino.salva_magazzino(filepath)
            print("Magazzino salvato.")

        elif scelta == "8":
            print(f"Valore Totale Magazzino: {magazzino.valore_magazzino():.2f}€")
            input("")

        elif scelta == "9":
            print(f"Media Valore Magazzino: {magazzino.media_valore_magazzino():.2f}€")
            input("")

        elif scelta == "0":
            print("Uscita...")
            break

        else:
            print("Scelta non valida!")

if __name__ == "__main__":
    main()
