# 🐾 Veterinary Telemonitoring App

**Applicazione di telemedicina veterinaria** per il monitoraggio remoto dei parametri vitali degli animali domestici.

L’applicazione permette ai veterinari e ai proprietari di registrare e monitorare facilmente i parametri vitali degli animali nel tempo.

---

## ✨ Funzionalità Principali

- **Registrazione Animale**: Inserimento di nuovi pazienti con nome, specie, nome del proprietario e numero di telefono
- **Inserimento Parametri Vitali**: Registrazione di temperatura corporea, frequenza cardiaca e sintomi clinici
- **Sistema di Allerta Automatico**: Rilevamento automatico di febbre alta (temperatura > 39.0 °C) con avviso visivo
- **Visualizzazione Storico**: Tabella delle misurazioni e grafico interattivo dell’andamento della temperatura nel tempo
- **Interfaccia intuitiva**: Realizzata con Streamlit, semplice da usare anche per utenti non tecnici

---

## 🛠️ Tecnologie utilizzate

- **Frontend**: Streamlit
- **Backend**: FastAPI
- **Database**: SQLite con SQLAlchemy
- **Visualizzazione dati**: Pandas + Matplotlib

---

## 📁 Struttura del Progetto
``` Veterinary-telemonitoring/
├── app.py                 # Interfaccia utente Streamlit
├── main.py                # API Backend FastAPI
├── database.py            # Modelli e configurazione del database
├── requirements.txt       # Dipendenze Python
├── veterinary.db          # Database SQLite (creato automaticamente)
└── README.md
```


---

## ⚡ Funzionalità del Sistema
L'applicazione è progettata per semplificare il telemonitoraggio veterinario:

* **Registrazione rapida** degli animali e dei proprietari.
* **Salvataggio cronologico** di temperatura e battito cardiaco.
* **Rilevamento automatico** di anomalie con alert.
* **Visualizzazione chiara** tramite grafici.

---

## 🔮 Possibili Sviluppi Futuri

Integrazione con dispositivi IoT: 
* **Collegamento a sensori indossabili** o collari smart per il rilevamento automatico e in tempo reale di temperatura, frequenza cardiaca e attività dell’animale
* **Aggiunta di altri parametri vitali** (frequenza respiratoria, saturazione ossigeno, peso, movimento)
* **Notifiche automatiche** via email, SMS o WhatsApp al proprietario in caso di valori critici
* **Autenticazione multi-utente** (per più veterinari o cliniche)
* **Esportazione dei dati** in formato PDF o CSV per referti medici
* **Inserimento e visualizzazione di foto dell’animale**
* **Dashboard analitica** con statistiche e trend a lungo termine
* **Gestione della mandria** durante i calori (inseminazione, monta)
* **Supporto per il deploy su cloud** (Render, Railway, AWS, ecc.)

---

### 📋 Requisiti
`fastapi`, `uvicorn[standard]`, `sqlalchemy`, `pydantic`, `streamlit`, `pandas`, `matplotlib`, `requests`

---

Author

**Matteo Carrieri** MSc candidate — Biotecnologie Mediche, Veterinarie e Farmaceutiche (LM-9)
University of Bologna · DIMEVET

📧 [matteo.carrieri@studio.unibo.it](mailto:matteo.carrieri@studio.unibo.it)

🔗 [LinkedIn Profile](https://www.linkedin.com/in/matteo-carrieri-9951a0281/)

Sviluppato per migliorare la cura e il monitoraggio degli animali. ❤️

License

This project is released under the MIT License — free to use, modify and distribute with attribution.
