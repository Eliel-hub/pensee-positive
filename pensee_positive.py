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

# Sélecteur de catégorie
categorie = st.selectbox(
    "Choisis une catégorie :",
    ["💪 Motivation", "😌 Calme", "❤️ Amour", "🌟 Confiance", "🎉 Joie"]
)

# Nettoyer le nom pour l'affichage
nom = "Coco" if "Coco" in personne else "Steven"

# ========== MESSAGES PAR CATÉGORIE ==========

messages_motivation = [
    "Tu es plus fort·e que tu ne le penses ! 💪",
    "Chaque petit pas compte, continue comme ça 🚀",
    "Les difficultés d'aujourd'hui sont les forces de demain",
    "N'abandonne pas, la meilleure version de toi est en chemin",
    "Ce que tu fais aujourd'hui peut changer demain ✨",
    "La persévérance est la clé du succès 🔑",
    "Crois en toi, même quand personne d'autre ne le fait 🌟"
]

messages_calme = [
    "Respire profondément, tout va bien aller 🌬️",
    "Accueille ce moment de calme comme un cadeau 🎁",
    "Tu n'es pas obligé de tout contrôler. Lâche prise 🍃",
    "Le silence est parfois la meilleure réponse 🤫",
    "Prends une pause, tu l'as bien mérité 💆‍♀️",
    "La paix intérieure commence par une seule respiration",
    "Ralentir n'est pas un échec, c'est une sagesse 🦥"
]

messages_amour = [
    "Tu es aimé·e plus que tu ne l'imagines ❤️",
    "Ton cœur mérite toute la douceur du monde 🫶",
    "L'amour que tu donnes revient toujours vers toi",
    "Sois tendre avec toi-même aujourd'hui 💝",
    "Tu es digne d'amour, toujours, sans condition",
    "Un petit geste d'amour peut tout changer 🌹",
    "Aimer et être aimé, c'est la plus belle des forces"
]

messages_confiance = [
    "Tu as tout ce qu'il faut en toi pour réussir 🌈",
    "Fais confiance à ton instinct, il te guide bien 🧭",
    "Les doutes sont normaux, mais ils ne te définissent pas",
    "Tu as déjà surmonté des difficultés, tu peux recommencer 💪",
    "La confiance naît de l'action. Lance-toi !",
    "Tu es capable de choses que tu n'imagines même pas ✨",
    "Regarde tout le chemin parcouru, sois fier·ère 🏆"
]

messages_joie = [
    "Trouve une petite joie dans chaque instant présent 🎈",
    "Rire est un super-pouvoir. Utilise-le aujourd'hui 😂",
    "La joie est contagieuse, partage-la autour de toi 🎉",
    "Danse comme si personne ne regardait 💃",
    "Un sourire sincère peut illuminer ta journée ☀️",
    "Fais quelque chose qui te rend heureux·se aujourd'hui 🍭",
    "La vie est trop courte pour ne pas célébrer les petits bonheurs 🎊"
]

# Associer la catégorie aux messages
if "Motivation" in categorie:
    messages = messages_motivation
    emoji_categorie = "💪"
elif "Calme" in categorie:
    messages = messages_calme
    emoji_categorie = "😌"
elif "Amour" in categorie:
    messages = messages_amour
    emoji_categorie = "❤️"
elif "Confiance" in categorie:
    messages = messages_confiance
    emoji_categorie = "🌟"
else:  # Joie
    messages = messages_joie
    emoji_categorie = "🎉"

# Emoji selon le personnage
emoji_personnage = "🌸" if nom == "Coco" else "🌟"

# Bouton
if st.button("✨ Recevoir une pensée ✨", type="primary", use_container_width=True):
    message = random.choice(messages)
    st.success(f"{emoji_personnage} **{nom}** dit : {message}\n\n{emoji_categorie} *Catégorie : {categorie}*")
    
    # Afficher l'heure
    maintenant = datetime.now().strftime("%H:%M:%S")
    st.caption(f"Message délivré à {maintenant}")

# Petit footer
st.divider()
st.markdown("*Choisis une catégorie et laisse-toi inspirer 💫*")