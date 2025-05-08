import request

def verifica_sito(url):
    try:
        risposta = request.get(url)
        if risposta.status_code == 200:
            print(f"il sito : {url} è raggiungibile")
        else:
            print(f"il sito {url} ha risposto con lo status code: {risposta.status_code:}")
    except request.exceptions.RequestException as e:
        print(f"Errore durante la richiesta al sito {url}: {e}")
    

verifica_sito("https://www.google.com")