from flask_cors import CORS
from dotenv import load_dotenv
from openai import OpenAI
from flask import Flask,  request, jsonify
import os



# --- 1. Configuration ---
load_dotenv()
app = Flask(__name__)
CORS(app)

# Initialisation du client pour l'API
try:
    client = OpenAI(
        api_key=os.getenv('PERPLEXITY_API'),
        base_url="https://api.perplexity.ai"
    )
except Exception as e:
    # Gérer une éventuelle erreur si la clé n'est pas définie
    print(f"Erreur critique d'initialisation du client API: {e}")
    client = None

# --- 2. Définition des Routes ---

@app.route('/')
def index():
    """Route racine pour les vérifications de santé (health checks)."""
    return "Le serveur du chatbot est en ligne.", 200

@app.route('/api/chat', methods=['POST'])
def chat():
    """
    Endpoint principal pour la conversation avec le chatbot.
    Reçoit le message de l'utilisateur et retourne la réponse de l'IA.
    """
    data = request.json
    user_message = data.get('message')
    status_code = 200
    bot_response = ""

    if not client:
        bot_response = "Erreur critique: Le client API n'a pas pu être initialisé. Vérifiez la clé API sur Render."
        status_code = 500
    elif not user_message:
        bot_response = "Erreur: Aucun message n'a été fourni."
        status_code = 400
    else:
        try:
            # Communication avec l'API Perplexity
            response = client.chat.completions.create(
                model="sonar-pro",
                messages=[
                    {
                        "role": "system",
                        "content": "Tu es un assistant virtuel pour un développeur Python freelance. "
                        "Ton but est d'accueillir les visiteurs. Sois amical et professionnel. "
                        "Messages courts, concis et pertinents. L'idée est d'engager la conversation "
                        "et d'inciter les visiteurs à poser des questions sur les services offerts."
                        "Si l'utilisateur pose une question hors sujet, redirige-le poliment vers les services "
                        "offerts par le développeur."
                        " N'utilise pas de balises HTML dans tes réponses."
                        "Si un utilisateur semble intéressé par une collaboration ou demande comment vous contacter,"
                        "encouragez-le à envoyer un mail en le présentant comme la meilleure étape."
                        "Fournissez l'adresse Ruaudel.emmanuel@orange.fr et ajoutez une phrase d'encouragement comme 'Je vous répondrai sous 24h'."

                    },
                    {
                        "role": "user",
                        "content": user_message
                    }
                ]
            )



            bot_response = response.choices[0].message.content

        except Exception as e:
            # Gérer les erreurs pendant l'appel à l'API
            print(f"Erreur lors de l'appel à l'API Perplexity: {e}")
            bot_response = "Désolé, une erreur technique interne est survenue. L'administrateur a été notifié."
            status_code = 500

    # Point de sortie unique et sécurisé pour la fonction
    return jsonify({'response': bot_response}), status_code
