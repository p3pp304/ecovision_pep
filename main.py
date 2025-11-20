import streamlit as st
from PIL import Image
import os

# --- Configurazione della Pagina ---
st.set_page_config(
    page_title="Assistente Raccolta Differenziata",
    page_icon="♻️",
    layout="centered"
)

# --- Titolo e Introduzione ---
st.title("♻️ Dove lo butto?")
st.markdown("""
Carica una foto di un rifiuto o scattala direttamente. 
L'Intelligenza Artificiale ti dirà **cos'è**, **se devi pulirlo** e **in quale bidone va buttato**.
""")

# --- Gestione API Key (Sicurezza) ---
api_key = None
if "GOOGLE_API_KEY" in st.secrets:
    api_key = st.secrets["GOOGLE_API_KEY"]
else:
    # Fallback per inserimento manuale se non presente nei secrets
    api_key = st.text_input("Inserisci la tua Google API Key:", type="password")

# --- Input Immagine ---
if api_key:
    option = st.radio("Come vuoi caricare l'immagine?", ("Carica file", "Scatta foto"))
    image_file = None

    if option == "Carica file":
        image_file = st.file_uploader("Scegli un'immagine...", type=["jpg", "jpeg", "png"])
    else:
        image_file = st.camera_input("Scatta una foto al rifiuto")

    # Anteprima immagine
    if image_file is not None:
        image = Image.open(image_file)
        st.image(image, caption="Immagine caricata", use_container_width=True)
        
        # Placeholder per il bottone di analisi (lo implementeremo dopo)
        st.info("Immagine pronta per l'analisi.")

else:
    st.warning("Per iniziare, inserisci la tua API Key.")

# --- Footer ---
st.markdown("---")
st.caption("Powered by Google Gemini & Streamlit")