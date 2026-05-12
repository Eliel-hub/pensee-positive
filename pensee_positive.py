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

# ========== CSS POUR LE CHAT MODERNE (STYLE MESSENGER) ==========
st.markdown("""
<style>
    /* Chat container - caché par défaut */
    .chat-popup {
        display: none;
        position: fixed;
        bottom: 80px;
        right: 20px;
        width: 380px;
        max-width: 90vw;
        height: 500px;
        background: white;
        border-radius: 15px;
        box-shadow: 0 5px 25px rgba(0,0,0,0.2);
        z-index: 1000;
        flex-direction: column;
        overflow: hidden;
        border: 1px solid #e0e0e0;
    }
    
    .chat-popup.show {
        display: flex;
    }
    
    /* En-tête du chat */
    .chat-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 12px 15px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        cursor: pointer;
    }
    
    .chat-header h4 {
        margin: 0;
        font-size: 16px;
    }
    
    .close-chat {
        background: none;
        border: none;
        color: white;
        font-size: 20px;
        cursor: pointer;
    }
    
    /* Corps du chat */
    .chat-body {
        flex: 1;
        overflow-y: auto;
        padding: 15px;
        background: #f8f9fa;
    }
    
    /* Messages */
    .message-user {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 10px 14px;
        border-radius: 18px;
        border-bottom-right-radius: 5px;
        margin: 8px 0;
        margin-left: 20%;
        text-align: left;
        word-wrap: break-word;
    }
    
    .message-assistant {
        background: white;
        color: #1a1a2e;
        padding: 10px 14px;
        border-radius: 18px;
        border-bottom-left-radius: 5px;
        margin: 8px 0;
        margin-right: 20%;
        text-align: left;
        word-wrap: break-word;
        box-shadow: 0 1px 2px rgba(0,0,0,0.05);
    }
    
    .message-time {
        font-size: 9px;
        color: #999;
        margin-top: 4px;
    }
    
    .assistant-name {
        font-size: 11px;
        font-weight: bold;
        color: #667eea;
        margin-bottom: 5px;
    }
    
    /* Pied du chat */
    .chat-footer {
        padding: 10px;
        background: white;
        border-top: 1px solid #e0e0e0;
        display: flex;
        gap: 8px;
    }
    
    .chat-footer input {
        flex: 1;
        padding: 10px;
        border: 1px solid #ddd;
        border-radius: 20px;
        outline: none;
    }
    
    .chat-footer button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 20px;
        padding: 8px 18px;
        cursor: pointer;
    }
    
    /* Bulle flottante */
    .chat-bubble {
        position: fixed;
        bottom: 20px;
        right: 20px;
        width: 60px;
        height: 60px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        z-index: 1001;
        transition: transform 0.2s;
    }
    
    .chat-bubble:hover {
        transform: scale(1.05);
    }
    
    .chat-bubble span {
        font-size: 28px;
    }
    
    /* Bouton effacer */
    .clear-btn {
        background: none;
        border: none;
        color: #ff6b6b;
        cursor: pointer;
        font-size: 14px;
        padding: 5px;
    }
    
    .clear-btn:hover {
        color: #ff4444;
    }
</style>

<script>
function toggleChat() {
    var chat = document.getElementById('chatPopup');
    chat.classList.toggle('show');
}

function closeChat() {
    var chat = document.getElementById('chatPopup');
    chat.classList.remove('show');
}
</script>
""", unsafe_allow_html=True)

# ========== INITIALISATION ==========
if 'historique_chat' not in st.session_state:
    st.session_state.historique_chat = []
if 'prenom_utilisateur' not in st.session_state:
    st.session_state.prenom_utilisateur = ""
if 'dernier_personnage' not in st.session_state:
    st.session_state.dernier_personnage = None

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
    
    # Vérifier si on a changé de personnage
    if st.session_state.dernier_personnage is not None and st.session_state.dernier_personnage != nom:
        # Réinitialiser la conversation
        st.session_state.historique_chat = []
        st.toast(f"💫 Nouvelle conversation avec {nom} !", icon="✨")
    
    st.session_state.dernier_personnage = nom
    
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

# ========== BULLE DE CHAT FLOTTANTE ==========
# Bulle pour ouvrir le chat
st.markdown(f"""
<div class="chat-bubble" onclick="toggleChat()">
    <span>💬</span>
</div>

<div id="chatPopup" class="chat-popup">
    <div class="chat-header" onclick="closeChat()">
        <h4>💬 Discussion avec {nom}</h4>
        <button class="close-chat">✕</button>
    </div>
    <div class="chat-body" id="chatBody">
""", unsafe_allow_html=True)

# Afficher les messages dans la bulle
if st.session_state.historique_chat:
    for msg in st.session_state.historique_chat:
        if msg["role"] == "user":
            st.markdown(f"""
            <div class="message-user">
                {msg['content']}
                <div class="message-time">{msg.get('heure', '')}</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="message-assistant">
                <div class="assistant-name">{msg['personnage']}</div>
                {msg['content']}
                <div class="message-time">{msg.get('heure', '')}</div>
            </div>
            """, unsafe_allow_html=True)
else:
    st.markdown(f"<div style='text-align:center;color:#999;padding:20px;'>💫 Commence la conversation avec {nom} !</div>", unsafe_allow_html=True)

# Pied du chat avec champ de saisie et bouton effacer
st.markdown(f"""
    </div>
    <div class="chat-footer">
        <input type="text" id="chatInput" placeholder="Écris ton message..." />
        <button onclick="sendMessage()">Envoyer</button>
        <button onclick="clearChat()" style="background:#ff6b6b;">🗑️</button>
    </div>
</div>

<script>
function sendMessage() {{
    var input = document.getElementById('chatInput');
    var message = input.value;
    if(message.trim() !== '') {{
        // Envoyer via Streamlit
        var data = {{type: 'chat', message: message}};
        // Utiliser un formulaire caché
        var form = document.createElement('form');
        form.method = 'post';
        form.action = '';
        var inputField = document.createElement('input');
        inputField.type = 'hidden';
        inputField.name = 'chat_message';
        inputField.value = message;
        form.appendChild(inputField);
        document.body.appendChild(form);
        form.submit();
    }}
}}

function clearChat() {{
    var form = document.createElement('form');
    form.method = 'post';
    form.action = '';
    var inputField = document.createElement('input');
    inputField.type = 'hidden';
    inputField.name = 'clear_chat';
    inputField.value = 'true';
    form.appendChild(inputField);
    document.body.appendChild(form);
    form.submit();
}}
</script>
""", unsafe_allow_html=True)

# Traitement des messages du chat (via formulaire POST)
# Note: Cette partie nécessite st.form pour fonctionner correctement
# Alternative plus simple avec des boutons Streamlit

# Footer
st.divider()
st.markdown("*💬 Clique sur la bulle en bas à droite pour discuter avec ton consultant !*")