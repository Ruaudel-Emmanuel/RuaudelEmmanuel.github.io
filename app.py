from flask import Flask, request, redirect, url_for, flash, render_template
from flask_cors import CORS
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import socket
import os

app = Flask(__name__)
app.secret_key = "change_ce_secret"  # à changer pour quelque chose d'unique
CORS(app)

# Configuration SMTP (laisse-les pour plus tard, on va d'abord faire fonctionner le formulaire)
SMTP_SERVER = os.environ.get("SMTP_SERVER", "smtp.orange.fr")
SMTP_PORT = int(os.environ.get("SMTP_PORT", "587"))
SMTP_USER = os.environ.get("SMTP_USER", "ton_adresse_orange@orange.fr")
SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD", "ton_mot_de_passe_orange")
DESTINATION_EMAIL = os.environ.get("DESTINATION_EMAIL", "ruaudel.emmanuel@orange.fr")


@app.route("/Contact.html", methods=["GET"])
def contact():
    """
    Affiche la page de contact.
    Assure-toi que Contact.html est dans le dossier 'templates' du projet.
    """
    return render_template("Contact.html")


@app.route("/sendmessage", methods=["POST"])
def send_message():
    """
    Réception du formulaire de contact.
    Pour l'instant, on simule l'envoi de mail pour éviter les problèmes de SMTP sur Render.
    """
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    # Validation minimale
    if not name or not email or not message:
        flash("Tous les champs sont obligatoires.", "error")
        return redirect(url_for("contact"))

    # Log du message reçu (visible dans les logs Render)
    subject = f"Nouveau message depuis le portfolio - {name}"
    body = f"Nom : {name}\nEmail : {email}\n\nMessage :\n{message}"

    print("=== Nouveau message de contact ===")
    print(subject)
    print(body)
    print("=== (envoi SMTP éventuellement désactivé sur Render) ===")

    # Si tu veux TENTER un envoi SMTP, décommente la partie ci-dessous.
    # Attention : Render bloque souvent les connexions SMTP sortantes, donc ça peut échouer.
    try:
        # Décommente si tu veux tester réellement l'envoi :
        #
        # socket.setdefaulttimeout(5)
        # msg = MIMEMultipart()
        # msg["From"] = SMTP_USER
        # msg["To"] = DESTINATION_EMAIL
        # msg["Subject"] = subject
        # msg.attach(MIMEText(body, "plain", "utf-8"))
        #
        # with smtplib.SMTP(SMTP_SERVER, SMTP_PORT, timeout=5) as server:
        #     server.starttls()
        #     server.login(SMTP_USER, SMTP_PASSWORD)
        #     server.send_message(msg)

        # Même si on ne tente pas l'envoi, on considère le traitement comme OK
        flash("Votre message a bien été envoyé !", "success")

    except Exception as e:
        print("Erreur envoi mail :", e)
        flash("Une erreur est survenue lors de l'envoi du message.", "error")

    return redirect(url_for("contact"))


# Optionnel : route racine pour éviter un 404 sur "/"
@app.route("/", methods=["GET"])
def index():
    """
    Redirige vers la page de contact par défaut.
    """
    return redirect(url_for("contact"))


if __name__ == "__main__":
    # En local, Flask écoute sur le port 10000 si défini par Render, sinon 5000
    port = int(os.environ.get("PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=True)
