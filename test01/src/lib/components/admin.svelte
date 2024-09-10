<script lang="ts">
	import { ibanUser } from "$lib/stores/iban.svelte";
	import { userLogs } from "$lib/stores/logs.svelte";
	import { userActivities } from '$lib/stores/attivita.svelte';
	import { storeUser } from "$lib/stores/user.svelte";
	import {financesStore} from '$lib/stores/financesStore.svelte';

	
	let sw_err: number = 0;
	let sw_err_id: number = 0;
	let sw_id: number = 0;
	let id: string = '';
	let password: string = '';
	let id_2: string = '';
	let nome: string='';
	let mail: string='';
	let cognome: string='';
	let indirizzo: string='';
	let password_2: string ='';
	let datan: string = '';
	let luogon: string='';
	let creazione:string='';
	let iban:string;
	let sw_salva: number=0;
	let sw_scelta:number=0;
	let sw_cancella:number=0;
	


	
	$: sw_err = password === '' || id===null ? 0 : sw_err;
	$: sw_err_id = id_2 === '' ? 0 : sw_err;

	const onclick = () => {
		if (id =='999' && password =='admin') {
			console.log('login admin effettuato');
			sw_id = 1;
		} else {
			sw_err = 1;
		}
	};
	const indietro=()=>{
		nome = '';
		cognome = '';
		mail = '';
		indirizzo = '';
		datan= '';
		luogon = '';
		creazione = '';
		iban = '';
		sw_salva=0;
	};
	const salva=()=>{
				const id_err = localStorage.getItem(`id_${id_2}`);
				if(id_err)
				{
					sw_salva=1;
				}else{
					sw_err_id =1;
				}
		
				
		
				const savedname = localStorage.getItem(`nome_${id_2}`);
				const savedmail = localStorage.getItem(`mail_${id_2}`);
				const savedAdress = localStorage.getItem(`indirizzo_${id_2}`);
				const savedSurname=localStorage.getItem(`cognome_${id_2}`);
				const savedDatan=localStorage.getItem(`datan_${id_2}`);
				const savedLuogon=localStorage.getItem(`luogon_${id_2}`);
				const savediban = localStorage.getItem(`iban_${id_2}`);
				const savedDc =localStorage.getItem(`firstLogin_${id_2}`);
				
				
				if (savedname) {
					nome = savedname;
				}
				if (savedmail) {
					mail = savedmail;
				}
				if (savedAdress) {
					indirizzo = savedAdress;
				}
				if (savediban) {
					iban = savediban;
				}
				if(savedSurname){
					cognome =savedSurname;
				}
				if(savedDatan){
					datan=savedDatan;
				}
				if(savedLuogon){
					luogon=savedLuogon;
				}
				if(savedDc){
					creazione=savedDc
				}
		
	};
	const loadLogs = () => {
	const savedLogs = localStorage.getItem(`logs_${id_2}`);
	if (savedLogs) {
		userLogs.set(JSON.parse(savedLogs));
	} else {
		userLogs.set([]);
	}
};
	const loadAttivita = () => {
		const savedAttivita = localStorage.getItem(`activities_${id_2}`);
		if (savedAttivita) {
			userActivities.set(JSON.parse(savedAttivita));
		} else {
			userActivities.set([]);
		}
	};

	const loadExpenses = () => {
		
			financesStore.resetExpenses();
			financesStore.loadExpenses(id_2); 
		
	};

	const stampalog = () => {
		loadLogs();
		const printEL = window.open('', '_blank');
		if (printEL) {
			const logs = $userLogs;
			let logsHtml = '';

			logs.forEach((attività: {  nlog: string; data: string  }) => {
				logsHtml += `
					<tr>
						<td>${attività.nlog}</td>
						<td>${attività.data}</td>
					</tr>
				`;
			});

			printEL.document.open();
			printEL.document.write(`
				<html>
					<head>
						<title>stampa_logs_${nome}_${cognome}</title>
						<style>
							table {
								width: 100%;
								border-collapse: collapse;
								margin-top: 20px;
								font-family: Arial, sans-serif;
							}
							th, td {
								border: 1px solid #ddd;
								padding: 8px;
								text-align: left;
							}
							th {
								background-color: #f4f4f4;
								color: #333;
								font-weight: bold;
							}
							tr:nth-child(even) {
								background-color: #f9f9f9;
							}
							tr:hover {
								background-color: #f1f1f1;
							}
							td {
								color: #555;
							}
							table {
								box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
							}
						</style>
					</head>
					<body>
						<h1>Logs di ${nome} ${cognome} </h1>
						<table>
							<thead>
								<tr>
									<th>N° logs</th>
									<th>Data</th>
									
								</tr>
							</thead>
							<tbody>
								${logsHtml}
							</tbody>
						</table>
					</body>
				</html>
			`);
			printEL.document.close();

			
			printEL.focus();
			printEL.onload = () => {
				printEL.print(); 
				printEL.close(); 
			};
		} else {
			console.error('La finestra non può essere aperta');
		}
	};
	const stampadati = () => {
		const printEL = window.open('', '_blank');
		if (printEL) {
			printEL.document.open();
			printEL.document.write(`
			<html>
				<style>
					table {
					width: 100%;
					border-collapse: collapse;
					margin-top: 20px;
					font-family: Arial, sans-serif;
					}

					th, td {
					border: 1px solid #ddd;
					padding: 8px;
					text-align: left;
					}

					th {
					background-color: #f4f4f4;
					color: #333;
					font-weight: bold;
					}

					tr:nth-child(even) {
					background-color: #f9f9f9;
					}

					tr:hover {
					background-color: #f1f1f1;
					}

					td {
					color: #555;
					}

					table {
					box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
					}

				</style>
				<title>stampa_dati_${nome}_${cognome}</title>
				<body>
					<h1>Informazioni  di ${nome} ${cognome}</h1>
					<div>
						<table>
							<tr><td>ID</td><td>Nome</td><td>Cognome</td><td>Data nascita</td><td>Luogo nascita</td><td>Email</td><td>iban</td><td>creazione account</td></tr>
							<tr><td>${id}</td><td>${nome}</td><td>${cognome}</td><td>${datan}</td><td>${luogon}</td><td>${mail}</td><td>${iban}</td><td>${creazione}</td></tr>
						</table>
					</div>
				</body>
			</html>
			`);
			printEL.document.close();

			printEL.focus();
			printEL.onload = () => {
				printEL.print();
				printEL.close();
			};
		} else {
			console.error('la finestra non può essere aperta');
		}
	};

	const stampaattivita = () =>{
		loadAttivita();
		const printEL=window.open('','_blank');
		if(printEL){
			const attivita = $userActivities;
			let attivitaHtml = '';

			attivita.forEach((activities) => {
				attivitaHtml += `
				<tr>
					<td>${activities.nome}</td>
					<td>${activities.data}</td>
					<td>${activities.completata ? 'SI' : 'NO'}
				</tr>`;
			});

			printEL.document.open();
			printEL.document.write(`
			<html>
					<head>
						<title>stampa_attivita_${nome}_${cognome}</title>
						<style>
							table {
								width: 100%;
								border-collapse: collapse;
								margin-top: 20px;
								font-family: Arial, sans-serif;
							}
							th, td {
								border: 1px solid #ddd;
								padding: 8px;
								text-align: left;
							}
							th {
								background-color: #f4f4f4;
								color: #333;
								font-weight: bold;
							}
							tr:nth-child(even) {
								background-color: #f9f9f9;
							}
							tr:hover {
								background-color: #f1f1f1;
							}
							td {
								color: #555;
							}
							table {
								box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
							}
						</style>
					</head>
					<body>
						<h1>Attività di ${nome} ${cognome}</h1>
						<table>
							<thead>
								<tr>
									<th>Attività</th>
									<th>Data</th>
									<th>Completata</th>
								</tr>
							</thead>
							<tbody>
								${attivitaHtml}
							</tbody>
						</table>
					</body>
				</html>
			`)
			printEL.document.close();

			printEL.focus();
			printEL.onload = () => {
				printEL.print();
				printEL.close();
			};

		}else{
			console.error('La finsetra non può essere aperta');
		}
	};
	const stampaspese = () => {
		loadExpenses();
		let c:number=0;
		const printEL = window.open('', '_blank');
		if (printEL) {
			const spese = $financesStore;
			let speseHtml = '';
			let Totale='';
			let totale=0;
			spese.forEach((finanze) => {
				c=c+1;
				totale+=finanze.amount;
				speseHtml += `
					<tr>
						<td>${c}</td>
						<td>${finanze.description}</td>
						<td>${finanze.amount.toFixed(2)}€</td>
					</tr>
				`;
			});
			Totale=`<tr>
						<td>Totale:</td>
						<td></td>
						<td>${totale.toFixed(2)}€</td>
					</tr>`

			printEL.document.open();
			printEL.document.write(`
				<html>
					<head>
						<title>stampa_spese_${nome}_${cognome}</title>
						<style>
							table {
								width: 100%;
								border-collapse: collapse;
								margin-top: 20px;
								font-family: Arial, sans-serif;
							}
							th, td {
								border: 1px solid #ddd;
								padding: 8px;
								text-align: left;
							}
							th {
								background-color: #f4f4f4;
								color: #333;
								font-weight: bold;
							}
							tr:nth-child(even) {
								background-color: #f9f9f9;
							}
							tr:hover {
								background-color: #f1f1f1;
							}
							td {
								color: #555;
							}
							table {
								box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
							}
						</style>
					</head>
					<body>
						<h1>Spese di ${nome} ${cognome} </h1>
						<table>
							<thead>
								<tr>
									<th>N°</th>
									<th>Descrizione</th>
									<th>Importo</th>
								</tr>
							</thead>
							<tbody>
								${speseHtml}
								${Totale}
							</tbody>
						</table>
					</body>
				</html>
			`);
			printEL.document.close();

			
			printEL.focus();
			printEL.onload = () => {
				printEL.print(); 
				printEL.close(); 
			};
		} else {
			console.error('La finestra non può essere aperta');
		}
		
	};


	const stampaTuttiUtenti = () => {
    const utenti: { id: string; nome: string; cognome: string; datan: string; luogon: string; mail:string; iban:string; firstLogin:string; password:string; }[]= [];
    const ids = new Set<string>();

    // Itera su tutte le chiavi nel localStorage
    for (let i = 0; i < localStorage.length; i++) {
        const key = localStorage.key(i);
        
        // Verifica se la chiave inizia con "nome_", "cognome_", "datan_" o "luogon_"
        if (key && (key.startsWith('nome_') || key.startsWith('cognome_') || key.startsWith('datan_') || key.startsWith('luogon_') || key.startsWith('mail_') || key.startsWith('iban_') || key.startsWith('firstLogin_') || key.startsWith('password_'))) {
            const idUtente = key.split('_')[1]; // Estrai l'ID utente dalla chiave
            ids.add(idUtente); // Aggiungi l'ID utente a un Set per garantire che ogni ID sia unico
        }
    }

    // Ora iteriamo su tutti gli ID unici e raccogliamo i dati associati
    ids.forEach(id => {
        const nome = localStorage.getItem(`nome_${id}`) || 'N/A';
        const cognome = localStorage.getItem(`cognome_${id}`) || 'N/A';
        const datan = localStorage.getItem(`datan_${id}`) || 'N/A';
        const luogon = localStorage.getItem(`luogon_${id}`) || 'N/A';
		const mail = localStorage.getItem(`mail_${id}`) || 'N/A';
		const iban= localStorage.getItem(`iban_${id}`) || 'N/A';
		const firstLogin = localStorage.getItem(`firstLogin_${id}`) || 'N/A';
		const password = localStorage.getItem(`password_${id}`) || 'N/A';

        utenti.push({ id, nome, cognome, datan, luogon,mail,iban,firstLogin,password });
    });

    // Stampa gli utenti in una nuova finestra
    const printEL = window.open('', '_blank');
    if (printEL) {
        let utentiHtml = utenti.map((utente) => `
            <tr>
                <td>${utente.id}</td>
                <td>${utente.nome}</td>
                <td>${utente.cognome}</td>
                <td>${utente.datan}</td>
                <td>${utente.luogon}</td>
				<td>${utente.mail}</td>
				<td>${utente.iban}</td>
				<td>${utente.firstLogin}</td>
				<td>${utente.password}</td>
            </tr>
        `).join('');

        printEL.document.open();
        printEL.document.write(`
            <html>
                <head>
                    <title>stampa_dati_utenti_admin</title>
                    <style>
                        table {
                            width: 100%;
                            border-collapse: collapse;
                            margin-top: 20px;
                            font-family: Arial, sans-serif;
                        }
                        th, td {
                            border: 1px solid #ddd;
                            padding: 8px;
                            text-align: left;
                        }
                        th {
                            background-color: #f4f4f4;
                            color: #333;
                            font-weight: bold;
                        }
                        tr:nth-child(even) {
                            background-color: #f9f9f9;
                        }
                        tr:hover {
                            background-color: #f1f1f1;
                        }
                    </style>
                </head>
                <body>
                    <h1>Lista di Tutti gli Utenti</h1>
                    <table>
                        <thead>
                            <tr>
                                <th>ID</th>
                                <th>Nome</th>
                                <th>Cognome</th>
                                <th>Data di Nascita</th>
                                <th>Luogo di Nascita</th>
								<th>mail</th>
								<th>iban</th>
								<th>data creazione account</th>
								<th>password</th>
                            </tr>
                        </thead>
                        <tbody>
                            ${utentiHtml}
                        </tbody>
                    </table>
                </body>
            </html>
        `);
        printEL.document.close();

        // Focalizza la finestra di stampa
        printEL.focus();

        // Stampa e chiudi la finestra
        printEL.onload = () => {
            printEL.print();
            printEL.close();
        };
    }
};
	const cancellautenti = () => {
		sw_scelta=1;
	};
	const annulla = () => {
		sw_scelta= 0 ;
	}
	const elimina = () => {
		sw_cancella=1;
		localStorage.removeItem(`id_${id_2}`);
		localStorage.removeItem(`logs_${id_2}`);
		localStorage.removeItem(`nome_${id_2}`);
		localStorage.removeItem(`mail_${id_2}`);
		localStorage.removeItem(`indirizzo_${id_2}`);
		localStorage.removeItem(`cognome_${id_2}`);
		localStorage.removeItem(`datan_${id_2}`);
		localStorage.removeItem(`luogon_${id_2}`);
		localStorage.removeItem(`iban_${id_2}`);
		localStorage.removeItem(`firstLogin_${id_2}`);
		localStorage.removeItem(`activities_${id_2}`);
		localStorage.removeItem(`nlog_${id_2}`);
		localStorage.removeItem(`expenses_${id_2}`);
		localStorage.removeItem(`password_${id_2}`);
		localStorage.removeItem(`lastLogin_${id_2}`);

	}
	

	
	


</script>

<!-- svelte-ignore css_unused_selector -->
<br /><br />
<div class="container">
    {#if sw_id === 0}
		<h1>Admin area</h1>
		<label for="IDuser">ID</label>
		<input type="number" id="IDuser" name="IDuser" bind:value={id} />
		<label for="password">password</label>
		<input type="password" id="password" name="password" bind:value={password} />
        <br>
		<button onclick={onclick}>login</button>
        <br><br>
        {#if sw_err === 1}
        <div class="wrongpass">
            <p class="errato">Password o id errati</p>
        </div>
        {/if}
    {:else}
		{#if sw_salva === 0}
        <h1>Gestisci</h1>
		<label for="IDutente">Inserisci id utente su cui effettuare le operazioni</label>
		<input type="number" id="IDutente" name="IDutente" bind:value={id_2} />
		{#if sw_err_id === 1}
			<p class="errato">id inesistente</p>
		{/if}
		<button onclick={salva}>salva</button>
		{:else}
			{#if sw_scelta === 0}
			<button class = "stampa" onclick={stampalog}>stampa log</button>
			<button class = "stampa" onclick={stampadati}>stampa Dati</button>
			<button class = "stampa" onclick={stampaattivita}>stampa attività</button>
			<button class = "stampa" onclick={stampaspese}>stampa spese</button>
			<button class = "stampa" onclick={stampaTuttiUtenti}>stampa tutti utenti</button>
			<button class = "stampa" onclick={cancellautenti}>cancella account</button>
			<button class = "indietro" onclick={indietro}>indietro</button>
			{:else}
				{#if sw_cancella===0}
					<h1>Sei sicuro?</h1>
					<p>una volta elimninato l'account sarà impossibile recuperarlo</p>
					<br>
					<div class="cancella">
						<button class ="Annulla"onclick={annulla}>Annulla</button>
						<button class="elimina"onclick={elimina}>elimina</button>
					</div>
				{:else}
					<h1>Account eliminato correttamente</h1>
					<button class="Annulla" onclick={indietro}>indietro</button>
				{/if}
			{/if}
		{/if}

    {/if}
</div>
<pre>
{sw_err}
</pre>

<div class="footer">
	&copy; 2024 Gestionale Personale di Porru Andrea. Tutti i diritti riservati.
</div>

<style>
	/* CSS invariato */
	.container .elimina{
		float:right;
	
	}
	
	p.errato {
		color: red;
		font-size: 15px;
		margin-top: -10px;
	}
    .wrongpass {
		font-family: Arial, sans-serif;
		text-align: center;
		max-width: 400px;
		font-size: 20;
		margin: 0 auto;
		background: white;
		padding: 20px;
		border-radius: 10px;
		box-shadow: 0 0 10px rgba(255, 2, 2, 0.3);
		background-color: #ec13133d;
	}

	button {
		border-radius: 5px;
		padding: 5px 10px;
		font-size: 14px;
		background-color: blueviolet;
		color: white;
		border: none;
		cursor: pointer;
	}
	 .Annulla {

		border-radius: 5px;
		padding: 5px 10px;
		font-size: 14px;
		background-color: blueviolet;
		color: white;
		border: none;
		cursor: pointer;
	}
	.Annulla:hover {
		background-color: rgb(78, 0, 78);
	}
	.Annulla:active{
		transform: translateY(2px);
	}

	button:hover {
		background-color: rgb(78, 0, 78);
	}
	button:active {
		transform: translateY(2px);
	}

	.container {
		font-family: Arial, sans-serif;
		max-width: 400px;
		margin: 0 auto;
		background: white;
		padding: 20px;
		border-radius: 10px;
		box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
		background-color: #f4f4f9;
	}

	h1 {
		color: blueviolet;
		font-size: 24px;
		margin-bottom: 20px;
		text-align: center;
	}

	label {
		display: block;
		margin: 10px 0 5px;
		font-weight: bold;
	}

	input[type='number'],
    input[type="password"] {
		width: 100%;
		padding: 10px;
		margin: 5px 0 20px;
		border: 1px solid #ccc;
		border-radius: 5px;
		box-sizing: border-box;
	}
	p {
		display: block;
		margin: 10px 0 5px;
	}


	.footer {
        background-color: #333;
        color: white;
        text-align: center;
        padding: 10px;
        position: fixed;
        bottom: 0;
        width: 100%;
        margin-left:0;
    }
	button.stampa {
    border-radius: 5px;
    padding: 10px 15px;
	
    font-size: 16px;
    background-color: green;
    color: white;
    border: none;
    cursor: pointer;
    margin: 5px 0;
    transition: background-color 0.3s ease, transform 0.2s;
}

	button.stampa:hover {
		background-color: darkgreen;
	}

	button.stampa:active {
		transform: translateY(2px);
	}
	button.elimina{
	
		border-radius: 5px;
		padding: 5px 10px;
		font-size: 14px;
		background-color: #ff4d4d;
		color: white;
		border: none;
		cursor: pointer;
		margin: 5px 0;
		transition: background-color 0.3s ease, transform 0.2s;
	}
	button.elimina:hover {
		background-color: #e60000;
	}

	button.elimina:active {
		transform: translateY(2px);
	}



	
	button.indietro {
		border-radius: 5px;
		padding: 10px 15px;
		font-size: 16px;
		background-color: #ff4d4d;
		color: white;
		border: none;
		cursor: pointer;
		margin: 5px 0;
		transition: background-color 0.3s ease, transform 0.2s;
	}

	button.indietro:hover {
		background-color: #e60000;
	}

	button.indietro:active {
		transform: translateY(2px);
	}

	button.stampa {
		margin-right: 10px;
	}

</style>