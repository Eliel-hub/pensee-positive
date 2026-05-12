import streamlit as st
import random
from datetime import datetime

# Configuration de la page
st.set_page_config(
    page_title="Pensée Positive",
    page_icon="✨",
    layout="centered"
)

# Titre
st.title("✨ Pensée Positive ✨")
st.caption("Une dose de bonheur chaque jour")

# Sélecteur de personnage
personne = st.radio(
    "Choisis ton héros du jour :",
    ("🐱 Coco", "🦊 Steven"),
    horizontal=True
)

# Nettoyer le nom pour l'affichage
nom = "Coco" if "Coco" in personne else "Steven"

# Base de messages
messages_coco = [
    "Sois fier·e de toi aujourd'hui !",
    "Tu mérites tout le bonheur du monde 💝",
    "Chaque petite victoire compte, célèbre-la !",
    "Ton sourire peut illuminer la journée de quelqu'un"
]

messages_steven = [
    "Crois en toi comme je crois en toi ! 🚀",
    "Aujourd'hui est une nouvelle chance de réussir",
    "Ton potentiel est infini, ne l'oublie jamais",
    "Un pas après l'autre, tu vas y arriver"
]

# Sélection des messages selon le personnage
if nom == "Coco":
    messages = messages_coco
    emoji = "🌸"
else:
    messages = messages_steven
    emoji = "🌟"

# Bouton
if st.button("✨ Recevoir une pensée positive ✨", type="primary", use_container_width=True):
    message = random.choice(messages)
    st.success(f"{emoji} **{nom}** dit : {message}")
    
    # Afficher l'heure pour un effet plus sympa
    maintenant = datetime.now().strftime("%H:%M:%S")
    st.caption(f"Message délivré à {maintenant}")

# Petit footer
st.divider()
st.markdown("*L'application qui vous veut du bien 💫*")