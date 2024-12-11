const BASE_URL = 'http://localhost:8000';
export const itemAdd = async (codice_articolo: string, descrizione_articolo: string, prezzo: number, quantita: number) => {
    try {
        const req = await fetch(BASE_URL + '/articoli/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ codice_articolo, descrizione_articolo, prezzo, quantita }),
        });

        if (!req.ok) {
            const errorData = await req.json();
            return {
                success: false,
                error: errorData.detail || "Errore durante l'aggiunta dell'articolo",
            };
        }

        const newItem = await req.json(); // Ottieni i dati dell'articolo aggiunto
        return {
            success: true,
            data: newItem, // Aggiungi la proprietà `data`
            error: null,
        };
    } catch (error) {
        return {
            success: false,
            error: error instanceof Error ? error.message : "Errore sconosciuto",
        };
    }
};


export const itemList = async () =>{
    const req = await fetch(BASE_URL+ '/articoli/');
    const res= await req.json();
    return res;

}

export const itemDelete = async (codice_articolo: string) => {
    try {
        const req = await fetch(`${BASE_URL}/articoli/${codice_articolo}`, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
            },
        });

        if (!req.ok) {
            const errorData = await req.json();
            return {
                success: false,
                error: errorData.detail || "Errore durante la cancellazione dell'articolo",
            };
        }

        return {
            success: true,
            error: null, // Nessun errore
        };
    } catch (error) {
        return {
            success: false,
            error: error instanceof Error ? error.message : "Errore sconosciuto",
        };
    }
};

export const itemModifica = async (codice_articolo: string, quantita: number) => {
    try {
        const response = await fetch(`http://localhost:8000/articoli/${codice_articolo}?nuova_quantita=${quantita}`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
            },
            // body: JSON.stringify({ quantita }), 
        });

        if (!response.ok) {
            const errorData = await response.json();
            return { success: false, error: errorData.detail || "Errore durante la modifica della quantità" };
        }

        const updatedItem = await response.json();
        return { success: true, data: updatedItem };
    } catch (error) {
        return {
            success: false,
            error: error instanceof Error ? error.message : "Errore sconosciuto",
        };
    }
};


export const valoreMagazzo = async () => {
    try {
        const req = await fetch(`${BASE_URL}/magazzino/valore`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },
        });

        if (!req.ok) {
            const errorData = await req.json();
            return {
                success: false,
                error: errorData.detail || "Errore durante il recupero del valore del magazzino",
            };
        }

        const data = await req.json();
        return {
            success: true,
            data: data.valore_totale, // Valore del magazzino
        };
    } catch (error) {
        return {
            success: false,
            error: error instanceof Error ? error.message : "Errore sconosciuto",
        };
    }
};
export const mediaMagazzo = async () => {
    try {
        const req = await fetch(`${BASE_URL}/magazzino/media`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },
        });

        if (!req.ok) {
            const errorData = await req.json();
            return {
                success: false,
                error: errorData.detail || "Errore durante il recupero della media del magazzino",
            };
        }

        const data = await req.json();
        return {
            success: true,
            data: data.media, // Valore della media
        };
    } catch (error) {
        return {
            success: false,
            error: error instanceof Error ? error.message : "Errore sconosciuto",
        };
    }
};


