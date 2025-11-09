# ==============================================================================
# app.py - Serveur Backend pour Chatbot IA et Formulaire de Contact
# ==============================================================================
# --- IMPORTATIONS ---
# ------------------------------------------------------------------------------
from flask import Flask, request, jsonify, render_template 
import os
import openai
from flask_cors import CORS
from dotenv import load_dotenv
# NOUVELLES IMPORTATIONS POUR L'ENVOI D'E-MAILS
from flask_mail import Mail, Message

# --- CONFIGURATION INITIALE ---
# ------------------------------------------------------------------------------
load_dotenv()
app = Flask(__name__)
CORS(app)

# --- CONFIGURATION DE L'API OPENAI ---
# ------------------------------------------------------------------------------
openai.api_key = os.getenv("OPENAI_API_KEY")

# --- NOUVEAU : CONFIGURATION POUR FLASK-MAIL ---
# ------------------------------------------------------------------------------
# Charge la configuration pour l'envoi d'e-mails depuis les variables d'environnement.
app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT', 587))
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS', 'True').lower() in ['true', 'on', '1']
app.config['MAIL_USE_SSL'] = os.getenv('MAIL_USE_SSL', 'False').lower() in ['true', 'on', '1']

# Initialise l'extension Mail. C'est la ligne que vous aviez mentionnée.
mail = Mail(app)

# --- DÉFINITION DES ROUTES DE L'APPLICATION ---
# ------------------------------------------------------------------------------
@app.route('/')
def index():
    return render_template('index.html')

# Route pour servir la page de contact
@app.route('/contact')
def contact():
    # Flask va automatiquement chercher 'Contact.html' dans le dossier /templates
    return render_template('Contact.html')

# Route pour servir la page GitHub
@app.route('/github')
def github():
    # Flask va chercher 'github.html' dans le dossier /templates
    return render_template('github.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message')
    if not user_message:
        return jsonify({"error": "Aucun message fourni"}), 400
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message}
            ]
        )
        bot_response = response.choices[0].message['content'].strip()
    except Exception as e:
        print(f"Erreur OpenAI : {e}")
        return jsonify({"error": "Erreur avec le service de chat."}), 500
    return jsonify({'response': bot_response})

# --- NOUVEAU : ROUTE POUR LE FORMULAIRE DE CONTACT ---
# ------------------------------------------------------------------------------
# Cette route va recevoir les données du formulaire de la page Contact.html.
@app.route('/send_message', methods=['POST'])
def send_message():
    try:
        # Récupère les données du formulaire.
        # Assurez-vous que les attributs 'name' de vos champs de formulaire correspondent
        # (ex: <input type="text" name="name">).
        name = request.form['name']
        email = request.form['email']
        message_body = request.form['message']

        # Crée l'e-mail à envoyer.
        msg = Message(
            subject=f"Nouveau message de {name} via votre site web",
            sender=app.config['MAIL_USERNAME'],
            recipients=[app.config['MAIL_USERNAME']] # L'e-mail est envoyé à vous-même.
        )

        # Définit le contenu de l'e-mail.
        msg.body = f"De : {name} <{email}>\n\n{message_body}"

        # Envoie l'e-mail.
        mail.send(msg)

        # Retourne une réponse de succès.
        return jsonify({"success": "Votre message a été envoyé avec succès."})

    except Exception as e:
        # Gère les erreurs d'envoi d'e-mail.
        print(f"Erreur lors de l'envoi de l'e-mail : {e}")
        return jsonify({"error": "Désolé, une erreur est survenue lors de l'envoi de votre message."}), 500

# --- DÉMARRAGE DE L'APPLICATION ---
# ------------------------------------------------------------------------------
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

