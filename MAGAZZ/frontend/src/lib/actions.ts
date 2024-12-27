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

        const newItem = await req.json(); 
        return {
            success: true,
            data: newItem, 
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
            error: null, 
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
export const itemModificaC = async (codice_articolo: string, codice: string,descrizione:string,prezzo:number,quantita:number) => {
    try {
        const response = await fetch(`http://localhost:8000/articoli/mod/${codice_articolo}?nuovo_codice=${codice}&nuova_descrizione=${descrizione}&nuovo_prezzo=${prezzo}&nuova_quantita=${quantita}`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
            },
           
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
            data: data.valore_totale, 
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
            data: data.media, 
        };
    } catch (error) {
        return {
            success: false,
            error: error instanceof Error ? error.message : "Errore sconosciuto",
        };
    }
};

export const exportMagazzino = async (percorso:string) => {
    console.log(percorso);
    try {
        const encodedPath = encodeURIComponent(percorso);
        const req = await fetch(`${BASE_URL}/magazzino/export/${encodedPath}`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },
        });

        if (!req.ok) {
            const errorData = await req.json();
            return {
                success: false,
                error: errorData.detail || "Errore durante l'esportazione del magazzino",
            };
        }

        return {
            success: true,
            error: null, 
        };
    } catch (error) {
        return {
            success: false,
            error: error instanceof Error ? error.message : "Errore sconosciuto",
        };
    }
};

export const importMagazzino = async (percorso: string) => {
    try {
        const encodedPath = encodeURIComponent(percorso);
        const response = await fetch(`${BASE_URL}/magazzino/import/${encodedPath}`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ percorso }),
        });

        if (!response.ok) {
            const errorData = await response.json();
            return {
                success: false,
                error: errorData.detail || "Errore durante l'importazione del CSV.",
            };
        }

        return {
            success: true,
            message: "Importazione completata con successo.",
        };
    } catch (error) {
        return {
            success: false,
            error: error instanceof Error ? error.message : "Errore sconosciuto.",
        };
    }
};
    





