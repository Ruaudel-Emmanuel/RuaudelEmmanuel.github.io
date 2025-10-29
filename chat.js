fetch('https://votre-serveur.com/api/chat', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({ message: 'Bonjour, je suis un client potentiel !' })
});
