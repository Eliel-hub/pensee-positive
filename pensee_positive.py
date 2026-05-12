import streamlit as st
import random
from datetime import datetime

# Configuration de la page
st.set_page_config(
    page_title="Pensée Positive",
    page_icon="✨",
    layout="centered"
)

# ========== 1. DATE EN FRANÇAIS ==========
# Dictionnaire pour traduire les jours et mois en français
jours_fr = {
    "Monday": "Lundi",
    "Tuesday": "Mardi",
    "Wednesday": "Mercredi",
    "Thursday": "Jeudi",
    "Friday": "Vendredi",
    "Saturday": "Samedi",
    "Sunday": "Dimanche"
}

mois_fr = {
    "January": "janvier",
    "February": "février",
    "March": "mars",
    "April": "avril",
    "May": "mai",
    "June": "juin",
    "July": "juillet",
    "August": "août",
    "September": "septembre",
    "October": "octobre",
    "November": "novembre",
    "December": "décembre"
}

aujourdhui = datetime.now()
jour_semaine = jours_fr[aujourdhui.strftime("%A")]
jour = aujourdhui.day
mois = mois_fr[aujourdhui.strftime("%B")]
annee = aujourdhui.year

date_formatee = f"{jour_semaine} {jour} {mois} {annee}"

# Titre avec la date
st.title("✨ Pensée Positive ✨")
st.caption(f"📅 {date_formatee}")

# ========== 2. PRÉSENTATION DE COCO ET STEVEN ==========

# Sélecteur de personnage
personne = st.radio(
    "Qui veux-tu consulter aujourd'hui ?",
    ("🐱 Coco", "🦊 Steven"),
    horizontal=True
)

nom = "Coco" if "Coco" in personne else "Steven"

# Phrase de présentation selon le personnage
if nom == "Coco":
    presentation = "🌸 **Coco** - Ta partenaise bien-être et pensée positive 🌸\n\n*Je suis là pour illuminer tes journées avec douceur et bienveillance. Ma mission : t'aider à voir la vie du bon côté !*"
    question = f"Alors {nom}, as-tu besoin d'une belle pensée positive aujourd'hui ?"
else:
    presentation = "🦊 **Steven** - Ton conseiller en développement personnel 🦊\n\n*Je t'accompagne pour cultiver la confiance, la force intérieure et l'optimisme. Ensemble, on va aller loin !*"
    question = f"Alors {nom}, es-tu prêt·e à recevoir une dose de motivation ?"

st.info(presentation, icon="💫")

# Question à l'utilisateur
st.write(f"**{question}**")

# Sélecteur de catégorie
categorie = st.selectbox(
    "Choisis une catégorie :",
    ["💪 Motivation", "😌 Calme", "❤️ Amour", "🌟 Confiance", "🎉 Joie"]
)

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
emoji_personnage = "🌸" if nom == "Coco" else "🦊"

# Variable pour stocker le message actuel
if 'dernier_message' not in st.session_state:
    st.session_state.dernier_message = ""

# Bouton principal
col1, col2 = st.columns([4, 1])

with col1:
    if st.button("✨ Recevoir une pensée ✨", type="primary", use_container_width=True):
        message = random.choice(messages)
        st.session_state.dernier_message = f"{emoji_personnage} **{nom}** dit : {message}\n\n{emoji_categorie} *Catégorie : {categorie}*"
        
        # Afficher l'heure
        maintenant = datetime.now().strftime("%H:%M:%S")
        
        st.success(st.session_state.dernier_message)
        st.caption(f"📨 Message délivré à {maintenant}")

# Bouton copier
if st.session_state.dernier_message:
    with col2:
        if st.button("📋 Copier", help="Copier le message dans le presse-papier"):
            message_a_copier = st.session_state.dernier_message.replace("**", "").replace("*", "")
            st.toast("✅ Message copié dans ton presse-papier ! Tu peux le partager 💌", icon="🎉")

# Petit footer
st.divider()
st.markdown("*Prends soin de toi, chaque jour est un cadeau ✨*")