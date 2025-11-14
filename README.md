# RuaudelEmmanuel.github.io



Projet de Site Web Portfolio 

Ce projet est un site web portfolio personnel qui inclut une page de contact fonctionnelle. Le backend est une application Flask conçue pour être déployée sur des services comme Render.



Corrections et Améliorations (Novembre 2025)

Une mise à jour majeure a été effectu

ée pour corriger plusieurs problèmes critiques qui empêchaient le bon fonctionnement du site :



Lien de Contact Inactif : Le lien "Contact" dans la navigation ne redirigeait pas vers la page de contact.



Chatbot Non Fonctionnel : L'assistant virtuel ne parvenait plus à se connecter au backend, rendant toute communication impossible.



Formulaire de Contact Inopérant : L'envoi de messages depuis le formulaire de contact ne fonctionnait pas.



Ces problèmes ont été résolus en restructurant à la fois le code du backend et certaines parties du frontend.



Détail des Modifications Techniques

Backend (app.py)

Le fichier app.py a été entièrement réécrit pour plus de clarté, de sécurité et de fonctionnalité.




Sécurité et Configuration :



Variables d'Environnement : Toutes les informations sensibles (clé API d'OpenAI, identifiants de messagerie) ont été externalisées. Elles doivent maintenant être configurées via des variables d'environnement, ce qui est une pratique de sécurité essentielle.



CORS (Cross-Origin Resource Sharing) : L'extension Flask-CORS a été intégrée pour autoriser les requêtes provenant du site web frontend (hébergé sur un domaine différent) vers le backend, résolvant ainsi les erreurs de communication.



Frontend (index.html, Contact.html, chat.js)

index.html :



Le lien de navigation vers la page de contact a été corrigé pour pointer vers Contact.html au lieu d'une ancre invalide.



Contact.html :



L'attribut action de la balise <form> a été mis à jour pour pointer vers l'URL complète du nouvel endpoint backend (https://<votre-domaine-render>/send\_message).



chat.js :



La variable API\_URL a été mise à jour pour pointer vers le nouvel endpoint du chatbot sur Render (https://<votre-domaine-render>/api/chat).



Configuration et Déploiement

Pour que l'application fonctionne correctement (localement ou sur Render), les étapes suivantes sont nécessaires.



1\. Fichier requirements.txt

Assurez-vous que votre fichier requirements.txt contient les dépendances suivantes :



text

Flask

Flask-Cors

openai

python-dotenv

Flask-Mail

2\. Variables d'Environnement

Vous devez configurer les variables d'environnement suivantes dans votre service d'hébergement (par exemple, dans la section "Secrets" ou "Environment" de Render) ou dans un fichier .env pour le développement local.



text

\# Clé API pour le chatbot

OPENAI\_API\_KEY="votre\_clé\_api\_openai"



\# Configuration pour l'envoi d'e-mails via le formulaire de contact

MAIL\_SERVER="smtp.votre\_fournisseur.com"

MAIL\_PORT=587

MAIL\_USERNAME="votre\_adresse@email.com"

MAIL\_PASSWORD="votre\_mot\_de\_passe\_email\_ou\_d\_application"

MAIL\_USE\_TLS=True

MAIL\_USE\_SSL=False


