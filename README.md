# Portfolio développeur – Flask

Ce dépôt contient le code source d’un petit site de portfolio développé avec Flask, incluant une page de contact fonctionnelle et plusieurs pages statiques (accueil, contact, page GitHub, etc.).  

## Fonctionnalités

- Affichage de pages HTML statiques (portfolio, compétences, projets, liens GitHub…).  
- Formulaire de contact accessible via `/Contact.html`.  
- Validation basique du formulaire côté serveur (vérification que tous les champs sont remplis).  
- Messages flash pour informer l’utilisateur en cas d’erreur ou de succès lors de l’envoi du formulaire.  
- Gestion des requêtes CORS via Flask-Cors.  

## Technologies utilisées

- Python 3  
- Flask  
- Flask-Cors  
- Gunicorn (pour le déploiement en production)  
- HTML / CSS (pages `index.html`, `Contact.html`, `github.html`, etc.)  

Les dépendances Python sont listées dans le fichier `requirements.txt`.  

## Installation

1. Cloner le dépôt :


2. Créer et activer un environnement virtuel (recommandé) :


3. Installer les dépendances :


## Configuration

L’application utilise une clé secrète pour les sessions Flask (messages flash).  
Dans `app.py`, remplace la valeur de :


par une vraie clé secrète générée aléatoirement.  

Si besoin, tu peux également ajouter un fichier `.env` pour centraliser les variables d’environnement (par exemple pour une future configuration d’envoi d’e-mails via Flask-Mail).  

## Lancement en développement

Lancer le serveur Flask en mode développement :


Par défaut, l’application tourne en mode `debug=True` sur `http://127.0.0.1:5000/`.  

- La page de contact est accessible à l’URL : `http://127.0.0.1:5000/Contact.html`  

## Déploiement (exemple)

Pour un déploiement sur un serveur (Linux), tu peux utiliser Gunicorn :


Adapte ensuite la configuration avec un serveur web (Nginx, etc.) pour servir l’application en production.  

## Structure du projet

Exemple de structure minimale :


Les fichiers HTML doivent se trouver dans le dossier `templates` pour être correctement rendus par `render_template`.  

## Améliorations possibles

- Brancher réellement le formulaire de contact à un service d’envoi d’e-mails (Flask-Mail, API externe…).  
- Ajouter une validation plus poussée (vérification du format d’e-mail, captcha, etc.).  
- Ajouter d’autres pages (blog, projets détaillés, CV en ligne…).  
- Mettre en place des tests automatisés et un pipeline CI/CD complet.  

## Licence

Préciser ici la licence de ton choix (par exemple MIT, GPL, ou « Tous droits réservés »).



