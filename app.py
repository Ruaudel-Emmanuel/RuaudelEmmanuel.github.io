from flask import Flask, request, jsonify, render_template, redirect, url_for, flash
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = 'ton_secret_key'  # Change ce secret
CORS(app)

@app.route('/sendmessage', methods=['POST'])
def send_message():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    
    # Exemple de traitement : ici, tu pourrais enregistrer, envoyer un mail, etc.
    if not name or not email or not message:
        flash('Tous les champs sont obligatoires.', 'error')
        return redirect(url_for('contact'))
    
    # Traitement fictif réussi
    flash('Votre message a bien été envoyé !', 'success')
    return redirect(url_for('contact'))

@app.route('/Contact.html')
def contact():
    return render_template('Contact.html')

if __name__ == '__main__':
    app.run(debug=True)
