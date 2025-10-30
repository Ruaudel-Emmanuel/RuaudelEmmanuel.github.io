# ========================================================
#          app.py - Serveur Chatbot avec API Perplexity
# ========================================================

# --- 1. Imports des bibliothèques (inchangés) ---
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
from openai import OpenAI # On utilise toujours le SDK OpenAI

# --- 2. Configuration initiale (inchangée) ---
load_dotenv()
app = Flask(__name__)
CORS(app)

# --- 3. Configuration du client pour l'API PERPLEXITY ---

# Récupérer la clé API Perplexity depuis le fichier .env
api_key = os.getenv('PERPLEXITY_API_KEY')
if not api_key:
    raise ValueError("La clé API Perplexity n'a pas été trouvée. Assurez-vous qu'elle est dans le .env sous le nom PERPLEXITY_API_KEY")

# 👇 LA MODIFICATION CLÉ EST ICI 👇
# On initialise le client en spécifiant l'URL de l'API Perplexity.
client = OpenAI(
    api_key=api_key,
    base_url="https://api.perplexity.ai"
)

# --- 4. Définition de l'API pour le chat ---

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message')

    if not user_message:
        return jsonify({"error": "Aucun message n'a été fourni"}), 400

    try:
        # On appelle la méthode `create` exactement comme avant
        response = client.chat.completions.create(
            # On utilise un des modèles de Perplexity, par exemple 'sonar-medium-online'
            # qui a accès à internet pour des réponses à jour.
            model="sonar-medium-online",
            messages=[
                {
                    "role": "system",
                    "content": "Tu es un assistant virtuel pour un développeur Python freelance. Ton but est d'accueillir les visiteurs et de qualifier les prospects. Sois amical, professionnel et concis."
                },
                {
                    "role": "user",
                    "content": user_message
                }
            ]
        )
        
        bot_response = response.choices[0].message.content

    except Exception as e:
        print(f"Erreur lors de l'appel à l'API Perplexity : {e}")
        bot_response = "Désolé, une erreur technique est survenue. Veuillez réessayer plus tard."
# ... (votre code pour la route /api/chat) ...

    return jsonify({'response': bot_response})


# Route racine pour les "health checks" de Render
@app.route('/api/chat', methods=['POST'])
def chat():
    return "Le serveur du chatbot est en ligne.", 200

# La section "if __name__ == '__main__':" a été supprimée.
# Le fichier s'arrête ici.

