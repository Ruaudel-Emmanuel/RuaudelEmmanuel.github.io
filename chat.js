// =============================================================
//          chat.js - Logique du Front-End du Chatbot
// =============================================================

// --- CONFIGURATION ---
// 👇 C'EST LA LIGNE QUI A ÉTÉ CORRIGÉE 👇
// L'URL pointe maintenant vers l'endpoint '/api/chat' de votre serveur.
const API_URL = "https://ruaudelemmanuel-github-io.onrender.com/api/chat";

// --- SÉLECTION DES ÉLÉMENTS DU DOM ---
// Assurez-vous que votre fichier HTML contient des éléments avec ces IDs.
const chatBox = document.getElementById('chat-box'); // La zone où les messages apparaissent
const userInput = document.getElementById('user-input'); // Le champ de texte pour l'utilisateur
const sendBtn = document.getElementById('send-btn'); // Le bouton pour envoyer

/**
 * Affiche un message dans la boîte de chat.
 * @param {string} message - Le texte du message à afficher.
 * @param {string} sender - L'expéditeur ('user' ou 'bot').
 */
function displayMessage(message, sender) {
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('message', sender); // Ajoute les classes CSS 'message' et 'user' ou 'bot'
    messageDiv.textContent = message;
    chatBox.appendChild(messageDiv);

    // Fait défiler automatiquement vers le bas pour voir le dernier message
    chatBox.scrollTop = chatBox.scrollHeight;
}

/**
 * Envoie le message de l'utilisateur à l'API et affiche la réponse.
 */
async function sendMessage() {
    const message = userInput.value.trim();
    if (message === '') return; // Ne rien faire si le message est vide

    // 1. Affiche immédiatement le message de l'utilisateur
    displayMessage(message, 'user');
    userInput.value = ''; // Vide le champ de saisie

    try {
        // 2. Envoie le message à l'API back-end (maintenant avec la bonne URL)
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message: message })
        });

        if (!response.ok) {
            // Affiche l'erreur 405 si elle se produit toujours, ou une autre erreur HTTP
            throw new Error(`Erreur HTTP: ${response.status}`);
        }

        const data = await response.json();

        // 3. Affiche la réponse du bot
        displayMessage(data.response, 'bot');

    } catch (error) {
        // 4. Gère les erreurs de communication
        console.error("Erreur lors de la communication avec l'API:", error);
        displayMessage("Désolé, je n'arrive pas à me connecter au serveur en ce moment. Veuillez réessayer plus tard.", 'bot');
    }
}

// --- GESTION DES ÉVÉNEMENTS ---

// Envoyer le message en cliquant sur le bouton
sendBtn.addEventListener('click', sendMessage);

// Envoyer le message en appuyant sur la touche "Entrée"
userInput.addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        event.preventDefault(); // Empêche le comportement par défaut (comme sauter une ligne)
        sendMessage();
    }
});
