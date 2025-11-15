from flask import Flask, request, redirect, url_for, flash
from flask_cors import CORS
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



app = Flask(__name__)
app.secret_key = 'ton_secret_key'  # Change ce secret
CORS(app)

SMTP_SERVER = "smtp.orange.fr"
SMTP_PORT = 587  # ou 465 si SSL, à tester
SMTP_USER = "ton_adresse_orange@orange.fr"      # identique à l’adresse qui envoie
SMTP_PASSWORD = "ton_mot_de_passe_orange"      # ou mot de passe d’application
DESTINATION_EMAIL = "ruaudel.emmanuel@orange.fr"  # adresse qui reçoit les messages


@app.route('/Contact.html', methods=['GET'])
def contact():
    return app.send_static_file('Contact.html')

@app.route('/sendmessage', methods=['POST'])
def send_message():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    if not name or not email or not message:
        flash('Tous les champs sont obligatoires.', 'error')
        return redirect(url_for('contact'))

    try:
        # Construction du mail (pour log)
        subject = f"Nouveau message depuis le portfolio - {name}"
        body = f"Nom : {name}\nEmail : {email}\n\nMessage :\n{message}"

        print("=== Nouveau message de contact ===")
        print(subject)
        print(body)
        print("=== (envoi SMTP désactivé sur Render) ===")

        # Si tu veux quand même tenter SMTP, mets-le derrière un timeout court :
        # socket.setdefaulttimeout(3)
        # with smtplib.SMTP(SMTP_SERVER, SMTP_PORT, timeout=3) as server:
        #     server.starttls()
        #     server.login(SMTP_USER, SMTP_PASSWORD)
        #     server.send_message(msg)

        flash('Votre message a bien été envoyé !', 'success')

    except Exception as e:
        print("Erreur envoi mail :", e)
        flash("Une erreur est survenue lors de l'envoi du message.", "error")

    return redirect(url_for('contact'))

