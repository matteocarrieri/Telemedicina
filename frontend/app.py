import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

# Configurazione API
API_URL = "http://localhost:8000"  # Cambia se il backend è remoto

st.title("🐾 Veterinary Telemonitoring App")

# Menu laterale
menu = st.sidebar.selectbox(
    "Menu",
    ["Registra Animale", "Inserisci Parametri", "Visualizza Storico"]
)

if menu == "Registra Animale":
    st.header("Registra Nuovo Animale")
    with st.form("animal_form"):
        name = st.text_input("Nome animale")
        species = st.selectbox("Specie", ["Cane", "Gatto", "Coniglio", "Altro"])
        owner_name = st.text_input("Nome proprietario")
        owner_phone = st.text_input("Telefono proprietario")
        
        if st.form_submit_button("Salva"):
            try:
                response = requests.post(
                    f"{API_URL}/animals/",
                    json={
                        "name": name,
                        "species": species,
                        "owner_name": owner_name,
                        "owner_phone": owner_phone
                    }
                )
                response.raise_for_status()
                st.success("Animale registrato con successo!")
            except requests.exceptions.RequestException as e:
                st.error(f"Errore durante la registrazione: {e}")

elif menu == "Inserisci Parametri":
    st.header("Inserisci Parametri Vitali")
    animal_id = st.number_input("ID Animale", min_value=1)
    temperature = st.number_input("Temperatura (°C)", min_value=30.0, max_value=45.0, value=38.5)
    heart_rate = st.number_input("Frequenza Cardiaca (bpm)", min_value=40, max_value=200, value=90)
    symptoms = st.text_area("Sintomi (separati da virgola)")
    
    if st.button("Salva Parametri"):
        try:
            response = requests.post(
                f"{API_URL}/vitals/",
                json={
                    "animal_id": animal_id,
                    "temperature": temperature,
                    "heart_rate": heart_rate,
                    "symptoms": symptoms
                }
            )
            response.raise_for_status()
            if response.json().get("status") == "warning":
                st.warning("⚠️ Febbre alta rilevata!")
            st.success("Dati salvati!")
        except requests.exceptions.RequestException as e:
            st.error(f"Errore durante il salvataggio: {e}")

elif menu == "Visualizza Storico":
    st.header("Storico Parametri")
    animal_id = st.number_input("ID Animale", min_value=1, key="history_animal_id")
    
    if st.button("Carica Storico"):
        try:
            response = requests.get(f"{API_URL}/vitals/{animal_id}")
            response.raise_for_status()
            data = response.json()
            df = pd.DataFrame(data)
            df["timestamp"] = pd.to_datetime(df["timestamp"])
            
            st.write("### Ultime misurazioni")
            st.table(df.tail())
            
            st.write("### Grafico Temperatura")
            fig, ax = plt.subplots(figsize=(10, 4))
            ax.plot(df["timestamp"], df["temperature"], marker="o")
            ax.set_xlabel("Data")
            ax.set_ylabel("Temperatura (°C)")
            st.pyplot(fig)
            plt.close(fig)
        except requests.exceptions.RequestException as e:
            st.error(f"Errore durante il caricamento: {e}")
