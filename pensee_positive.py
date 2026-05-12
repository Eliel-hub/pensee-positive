import streamlit as st
import random
from datetime import datetime

# Configuration de la page
st.set_page_config(
    page_title="Pensée Positive",
    page_icon="✨",
    layout="wide"
)

# ========== DATE EN FRANÇAIS ==========
jours_fr = {
    "Monday": "Lundi", "Tuesday": "Mardi", "Wednesday": "Mercredi",
    "Thursday": "Jeudi", "Friday": "Vendredi", "Saturday": "Samedi",
    "Sunday": "Dimanche"
}

mois_fr = {
    "January": "janvier", "February": "février", "March": "mars",
    "April": "avril", "May": "mai", "June": "juin",
    "July": "juillet", "August": "août", "September": "septembre",
    "October": "octobre", "November": "novembre", "December": "décembre"
}

aujourdhui = datetime.now()
jour_semaine = jours_fr[aujourdhui.strftime("%A")]
jour = aujourdhui.day
mois = mois_fr[aujourdhui.strftime("%B")]
annee = aujourdhui.year

date_formatee = f"{jour_semaine} {jour} {mois} {annee}"

# ========== FONCTIONS DE RÉPONSE ==========
def reponse_coco(message, prenom_utilisateur):
    message = message.lower()
    
    if any(word in message for word in ["triste", "déprime", "ça va pas", "mal", "pleure"]):
        return f"🌸 Oh {prenom_utilisateur}, je suis désolée que tu te sentes comme ça. Je suis là pour toi. N'oublie pas que les moments difficiles passent toujours. Veux-tu qu'on trouve ensemble quelque chose qui pourrait te réconforter ? 💝"
    
    elif any(word in message for word in ["stress", "angoiss", "peur", "inquiet"]):
        return f"🌸 Je comprends que le stress puisse être pesant, {prenom_utilisateur}. Prends une grande respiration avec moi. Inspire... expire... Tu n'es pas seul·e face à ça. Qu'est-ce qui te stresse particulièrement ? 🫶"
    
    elif any(word in message for word in ["fatigu", "épuis", "plus d'énergie"]):
        return f"🌸 Repose-toi, {prenom_utilisateur}. Tu as le droit de faire une pause. Ton corps et ton esprit ont besoin de douceur. Bois de l'eau, prends l'air quelques minutes. Je veille sur toi 💆‍♀️💤"
    
    elif any(word in message for word in ["amour", "cœur", "sentiment", "aimer"]):
        return f"🌸 L'amour est la plus belle des énergies, {prenom_utilisateur}. Tu mérites d'aimer et d'être aimé·e. N'aie pas peur d'ouvrir ton cœur, la vie te réserve de belles rencontres ❤️🌹"
    
    elif any(word in message for word in ["travail", "boulot", "job", "colleg", "patron"]):
        return f"🌸 Le travail ne définit pas ta valeur, {prenom_utilisateur}. Tu fais de ton mieux et c'est déjà énorme. Fais-toi confiance et n'oublie pas de prendre du temps pour toi 💪💼"
    
    elif any(word in message for word in ["merci", "gentil", "sympa"]):
        return f"🌸 Avec plaisir, {prenom_utilisateur} ! C'est tout naturel pour moi. Tu mérites tout le bonheur du monde. Reviens me voir quand tu veux 🌟💖"
    
    elif any(word in message for word in ["bonjour", "salut", "coucou", "hello"]):
        reponses_salut = [
            f"🌸 Coucou {prenom_utilisateur} ! Quelle joie de te voir aujourd'hui ! ☀️",
            f"🌸 Bonjour mon doux/ma douce {prenom_utilisateur} ! Comment vas-tu ? 💕",
            f"🌸 Hé {prenom_utilisateur} ! Je suis contente que tu sois là ✨"
        ]
        return random.choice(reponses_salut)
    
    else:
        reponses_generiques = [
            f"🌸 Je t'écoute, {prenom_utilisateur}. Parle-moi de ce qui te traverse l'esprit 💫",
            f"🌸 Merci de te confier à moi, {prenom_utilisateur}. Je suis là pour toi, toujours 🫂",
            f"🌸 Continue, {prenom_utilisateur}. Je suis tout·e ouïe 📖💖"
        ]
        return random.choice(reponses_generiques)

def reponse_steven(message, prenom_utilisateur):
    message = message.lower()
    
    if any(word in message for word in ["triste", "déprime", "ça va pas", "mal", "pleure"]):
        return f"🦊 Hé {prenom_utilisateur}, les moments bas arrivent à tout le monde. Mais souviens-toi : chaque difficulté est une opportunité de devenir plus fort ! Relève la tête, je crois en toi ! 🚀💪"
    
    elif any(word in message for word in ["stress", "angoiss", "peur", "inquiet"]):
        return f"🦊 Le stress, c'est ton corps qui se prépare à performer, {prenom_utilisateur} ! Canalise cette énergie. Fais une liste, priorise, et attaque le plus important. Tu vas gérer, j'en suis sûr ! 🔥🎯"
    
    elif any(word in message for word in ["fatigu", "épuis", "plus d'énergie"]):
        return f"🦊 La fatigue est un signal, {prenom_utilisateur}. Écoute-toi. Une bonne nuit de sommeil ou une micro-sieste peut tout changer. Et demain, tu seras encore plus fort ! 💤✨"
    
    elif any(word in message for word in ["amour", "cœur", "sentiment", "aimer"]):
        return f"🦊 L'amour est une force incroyable, {prenom_utilisateur}. N'aie pas peur d'aimer pleinement. Les plus grandes réussites viennent du cœur. Lance-toi, tu ne le regretteras pas ! ❤️✨"
    
    elif any(word in message for word in ["travail", "boulot", "job", "colleg", "patron", "projet"]):
        return f"🦊 Le travail, c'est le terrain de jeu des battants, {prenom_utilisateur} ! Organise-toi, fixe-toi des petits objectifs, et célèbre chaque victoire. Tu es plus capable que tu ne le penses ! 🏆💼"
    
    elif any(word in message for word in ["merci", "gentil", "sympa"]):
        return f"🦊 C'est tout naturel, {prenom_utilisateur} ! Je suis là pour te booster. Ensemble, on va aller loin ! 🤘🎉"
    
    elif any(word in message for word in ["bonjour", "salut", "coucou", "hello"]):
        reponses_salut = [
            f"🦊 Salut {prenom_utilisateur} ! Prêt·e à déchirer ta journée ? ☀️💥",
            f"🦊 Hé {prenom_utilisateur} ! Lève-toi et brille, aujourd'hui est un nouveau terrain de jeu ! 🚀",
            f"🦊 Bien le bonjour {prenom_utilisateur} ! On attaque ça comment aujourd'hui ? 🎯"
        ]
        return random.choice(reponses_salut)
    
    else:
        reponses_generiques = [
            f"🦊 Je t'écoute, {prenom_utilisateur}. Dis-moi ce qui te motive ou te freine, et on va avancer ensemble ! 💬🔥",
            f"🦊 Parle-moi, {prenom_utilisateur}. Je suis ton conseiller, ta caisse de résonance. Ensemble on va trouver des solutions ! 🧠🚀",
            f"🦊 Continue, {prenom_utilisateur}. Je sens que tu as des choses à dire, et je suis là pour ça ! 🤘💬"
        ]
        return random.choice(reponses_generiques)

# ========== INITIALISATION ==========
if 'historique_chat' not in st.session_state:
    st.session_state.historique_chat = []
if 'prenom_utilisateur' not in st.session_state:
    st.session_state.prenom_utilisateur = ""

# ========== CSS POUR UN CHAT PLUS PROPRE ==========
st.markdown("""
<style>
    .chat-message-user {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 12px 18px;
        border-radius: 20px;
        border-bottom-right-radius: 5px;
        margin: 10px 0;
        margin-left: 20%;
        text-align: left;
        box-shadow: 0 1px 2px rgba(0,0,0,0.1);
    }
    .chat-message-assistant {
        background: #f0f2f6;
        color: #1a1a2e;
        padding: 12px 18px;
        border-radius: 20px;
        border-bottom-left-radius: 5px;
        margin: 10px 0;
        margin-right: 20%;
        text-align: left;
        box-shadow: 0 1px 2px rgba(0,0,0,0.1);
    }
    .chat-time {
        font-size: 10px;
        color: #888;
        margin-top: 4px;
    }
    .assistant-name {
        font-size: 12px;
        font-weight: bold;
        margin-bottom: 5px;
        color: #555;
    }
</style>
""", unsafe_allow_html=True)

# ========== AFFICHAGE PRINCIPAL ==========
col1, col2 = st.columns([1, 1.2])

with col1:
    st.title("✨ Pensée Positive ✨")
    st.caption(f"📅 {date_formatee}")
    
    personne = st.radio(
        "Qui veux-tu consulter aujourd'hui ?",
        ("🐱 Coco", "🦊 Steven"),
        horizontal=True
    )
    
    nom = "Coco" if "Coco" in personne else "Steven"
    
    if nom == "Coco":
        presentation = "🌸 **Coco** - Ta partenaire bien-être 🥰\n\n*Je suis là pour écouter ton cœur et t'apporter douceur et réconfort.*"
    else:
        presentation = "🦊 **Steven** - Ton coach motivation 🔥\n\n*Je suis là pour te booster, te motiver et t'accompagner vers le meilleur de toi-même !*"
    
    st.info(presentation, icon="💫")
    
    if st.session_state.prenom_utilisateur == "":
        prenom_input = st.text_input("Comment t'appelles-tu ? (Coco/Steven veulent savoir !)")
        if prenom_input:
            st.session_state.prenom_utilisateur = prenom_input
            st.rerun()
    else:
        st.success(f"🌟 Content de te voir, {st.session_state.prenom_utilisateur} ! 🌟")
        
        categorie = st.selectbox(
            "Choisis une catégorie pour tes pensées :",
            ["💪 Motivation", "😌 Calme", "❤️ Amour", "🌟 Confiance", "🎉 Joie"]
        )
        
        nombre_messages = st.slider(
            "Combien de pensées veux-tu recevoir ?",
            min_value=1, max_value=5, value=1, step=1
        )
        
        messages_base = {
            "💪 Motivation": ["Tu es plus fort·e que tu ne le penses ! 💪", "Chaque petit pas compte 🚀", "Continue, tu gères ! ✨"],
            "😌 Calme": ["Respire profondément, tout va bien 🌬️", "Lâche prise, tu as fait assez 🍃", "Le calme est ta force 🧘"],
            "❤️ Amour": ["Tu es aimé·e plus que tu ne l'imagines ❤️", "Sois tendre avec toi-même 💝", "L'amour que tu donnes revient toujours 🌹"],
            "🌟 Confiance": ["Crois en toi 🌈", "Tu es capable de grandes choses ✨", "Fais confiance à ton instinct 🧭"],
            "🎉 Joie": ["Rire est un super-pouvoir 😂", "Trouve la joie dans les petits moments 🎈", "Fais ce qui te rend heureux·se 🍭"]
        }
        
        messages = messages_base[categorie]
        emoji_categorie = categorie.split()[0]
        emoji_personnage = "🌸" if nom == "Coco" else "🦊"
        
        if st.button("✨ Recevoir mes pensées ✨", type="primary", use_container_width=True):
            messages_choisis = random.sample(messages, min(nombre_messages, len(messages)))
            maintenant = datetime.now().strftime("%H:%M:%S")
            
            st.success(f"📨 {nom} t'a préparé {len(messages_choisis)} pensée(s) positive(s) !", icon="✨")
            for i, msg in enumerate(messages_choisis, 1):
                st.info(f"{emoji_personnage} **Pensée {i}** : {msg}", icon=emoji_categorie)
            st.caption(f"💫 Délivré à {maintenant}")

# ========== ZONE DE CHAT ==========
with col2:
    st.markdown(f"### 💬 Conversation avec {nom}")
    
    # Conteneur du chat avec scroll
    chat_container = st.container(height=450)
    
    with chat_container:
        if not st.session_state.historique_chat:
            st.info(f"💫 Commence la conversation avec {nom} !")
        else:
            for msg in st.session_state.historique_chat:
                if msg["role"] == "user":
                    st.markdown(f"""
                    <div class="chat-message-user">
                        👤 {msg['content']}
                        <div class="chat-time">{msg.get('heure', '')}</div>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div class="chat-message-assistant">
                        <div class="assistant-name">{msg['personnage']}</div>
                        {msg['content']}
                        <div class="chat-time">{msg.get('heure', '')}</div>
                    </div>
                    """, unsafe_allow_html=True)
    
    # Zone de saisie
    if st.session_state.prenom_utilisateur:
        col_input, col_send = st.columns([5, 1])
        with col_input:
            user_input = st.text_area("", placeholder="💬 Écris ton message ici...", key="chat_input", height=80, label_visibility="collapsed")
        with col_send:
            st.write("")
            st.write("")
            envoyer = st.button("📤 Envoyer", use_container_width=True)
        
        if envoyer and user_input.strip():
            # Ajouter message utilisateur
            st.session_state.historique_chat.append({
                "role": "user",
                "content": user_input,
                "heure": datetime.now().strftime("%H:%M")
            })
            
            # Générer réponse
            if nom == "Coco":
                reponse = reponse_coco(user_input, st.session_state.prenom_utilisateur)
            else:
                reponse = reponse_steven(user_input, st.session_state.prenom_utilisateur)
            
            # Ajouter réponse assistant
            st.session_state.historique_chat.append({
                "role": "assistant",
                "personnage": f"{nom} {emoji_personnage}",
                "content": reponse,
                "heure": datetime.now().strftime("%H:%M")
            })
            
            st.rerun()
    else:
        st.info("👋 Entre ton prénom dans la colonne de gauche pour commencer à discuter !")

# Footer
st.divider()
st.markdown("*💬 Une discussion vaut mille pensées — Coco & Steven sont là pour toi*")