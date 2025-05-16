const messagesContainer = document.getElementById('messages-container');
    const textInput = document.getElementById('text-input');
    const sendButton = document.getElementById('send-button');
    const typingIndicator = document.getElementById('typing-indicator'); // precisa existir no HTML
    const toggleModeBtn = document.getElementById('toggle-mode');

    function addMessage(message, type) {
        const messageElement = document.createElement('div');
        messageElement.classList.add('message', type);
        messageElement.innerHTML = marked.parse(message);
        messagesContainer.appendChild(messageElement);
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }

    function setTyping(isTyping) {
        if (typingIndicator) {
            typingIndicator.style.display = isTyping ? 'block' : 'none';
        }
    }

    function sendMessage() {
        const messageText = textInput.value.trim();
        if (messageText !== '') {
            addMessage(messageText, 'sent');
            textInput.value = '';
            setTyping(true);

            fetch('/api/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ mensagem: messageText })
            })
            .then(response => response.json())
            .then(data => {
                setTyping(false);
                if (data?.resposta) {
                    addMessage(data.resposta, 'received');
                } else {
                    addMessage("*❌ Resposta vazia do SnarkBOT.*", 'received');
                }
            })
            .catch(() => {
                setTyping(false);
                addMessage("*Erro ao se conectar ao SnarkBOT.*", 'received');
            });
        }
    }

    sendButton.addEventListener('click', sendMessage);
    textInput.addEventListener('keydown', (event) => {
        if (event.key === 'Enter' && !event.shiftKey) {
            event.preventDefault();
            sendMessage();
        }
    });

    // Alternar dark mode
    toggleModeBtn?.addEventListener('click', () => {
        document.body.classList.toggle('dark');
    });