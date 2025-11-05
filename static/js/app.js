// Тамерлан ИИ - Frontend Logic

class TamerlaneAI {
    constructor() {
        this.sessionId = this.generateSessionId();
        this.apiUrl = '/api';
        this.init();
    }

    generateSessionId() {
        return 'session_' + Date.now() + '_' + Math.random().toString(36).substr(2, 9);
    }

    init() {
        this.chatContainer = document.getElementById('chatContainer');
        this.messageInput = document.getElementById('messageInput');
        this.sendBtn = document.getElementById('sendBtn');
        this.clearBtn = document.getElementById('clearBtn');
        this.modelSelect = document.getElementById('modelSelect');
        this.sendBtnText = document.getElementById('sendBtnText');
        this.loadingSpinner = document.getElementById('loadingSpinner');
        this.statusIndicator = document.getElementById('statusIndicator');

        this.attachEventListeners();
        this.checkHealth();
    }

    attachEventListeners() {
        // Отправка сообщения
        this.sendBtn.addEventListener('click', () => this.sendMessage());

        // Отправка по Enter (Shift+Enter для новой строки)
        this.messageInput.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                this.sendMessage();
            }
        });

        // Очистка чата
        this.clearBtn.addEventListener('click', () => this.clearChat());

        // Автоматическое изменение высоты textarea
        this.messageInput.addEventListener('input', () => {
            this.messageInput.style.height = 'auto';
            this.messageInput.style.height = this.messageInput.scrollHeight + 'px';
        });
    }

    async checkHealth() {
        try {
            const response = await fetch(`${this.apiUrl}/health`);
            const data = await response.json();

            if (data.status === 'ok') {
                this.statusIndicator.textContent = '🟢 Online';
                this.statusIndicator.style.color = '#2ecc71';

                if (!data.api_configured) {
                    this.showWarning('⚠️ API ключ не настроен. Работает в демо-режиме.');
                }
            }
        } catch (error) {
            this.statusIndicator.textContent = '🔴 Offline';
            this.statusIndicator.style.color = '#e74c3c';
            console.error('Health check failed:', error);
        }
    }

    async sendMessage() {
        const message = this.messageInput.value.trim();

        if (!message) {
            this.showWarning('Пожалуйста, введите сообщение');
            return;
        }

        // Отключаем кнопку отправки
        this.setLoading(true);

        // Отображаем сообщение пользователя
        this.addMessage(message, 'user');

        // Очищаем поле ввода
        this.messageInput.value = '';
        this.messageInput.style.height = 'auto';

        try {
            const response = await fetch(`${this.apiUrl}/chat`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    message: message,
                    session_id: this.sessionId,
                    model: this.modelSelect.value
                })
            });

            const data = await response.json();

            if (response.ok) {
                this.addMessage(data.response, 'assistant');
            } else {
                this.showError(`Ошибка: ${data.error || 'Неизвестная ошибка'}`);
            }
        } catch (error) {
            this.showError(`Ошибка соединения: ${error.message}`);
            console.error('Send message error:', error);
        } finally {
            this.setLoading(false);
        }
    }

    addMessage(content, role) {
        // Удаляем приветственное сообщение при первом сообщении
        const welcomeMessage = this.chatContainer.querySelector('.welcome-message');
        if (welcomeMessage) {
            welcomeMessage.remove();
        }

        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${role}-message`;

        const roleText = role === 'user' ? 'Вы' : '🏹 Тамерлан';
        const roleDiv = document.createElement('div');
        roleDiv.className = 'message-role';
        roleDiv.textContent = roleText;

        const contentDiv = document.createElement('div');
        contentDiv.className = 'message-content';
        contentDiv.textContent = content;

        if (role === 'user') {
            messageDiv.appendChild(roleDiv);
            messageDiv.appendChild(contentDiv);
        } else {
            messageDiv.appendChild(roleDiv);
            messageDiv.appendChild(contentDiv);
        }

        this.chatContainer.appendChild(messageDiv);

        // Прокрутка вниз
        this.scrollToBottom();
    }

    async clearChat() {
        if (!confirm('Вы уверены, что хотите очистить историю чата?')) {
            return;
        }

        try {
            const response = await fetch(`${this.apiUrl}/clear`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    session_id: this.sessionId
                })
            });

            if (response.ok) {
                // Очищаем контейнер чата
                this.chatContainer.innerHTML = `
                    <div class="welcome-message">
                        <h2>Сәлеметсіз бе! / Здравствуйте!</h2>
                        <p>Я Тамерлан - ваш Тюркский ИИ-ассистент. Готов помочь вам с:</p>
                        <ul>
                            <li>🏛️ Историей и культурой тюркских народов</li>
                            <li>🗣️ Изучением тюркских языков (казахский, турецкий, узбекский и др.)</li>
                            <li>💻 Программированием и технологиями</li>
                            <li>📚 Образованием и саморазвитием</li>
                            <li>💼 Бизнес-консультациями</li>
                            <li>🌟 Любыми другими вопросами</li>
                        </ul>
                        <p class="hint">Просто напишите ваш вопрос ниже...</p>
                    </div>
                `;

                // Генерируем новый session ID
                this.sessionId = this.generateSessionId();
            }
        } catch (error) {
            this.showError('Ошибка при очистке чата');
            console.error('Clear chat error:', error);
        }
    }

    setLoading(loading) {
        this.sendBtn.disabled = loading;
        this.messageInput.disabled = loading;

        if (loading) {
            this.sendBtnText.style.display = 'none';
            this.loadingSpinner.style.display = 'inline-block';
        } else {
            this.sendBtnText.style.display = 'inline';
            this.loadingSpinner.style.display = 'none';
        }
    }

    showWarning(message) {
        this.showNotification(message, 'warning');
    }

    showError(message) {
        this.showNotification(message, 'error');
    }

    showNotification(message, type) {
        const notification = document.createElement('div');
        notification.className = `notification ${type}`;
        notification.textContent = message;
        notification.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            padding: 15px 25px;
            border-radius: 10px;
            background: ${type === 'error' ? '#e74c3c' : '#f39c12'};
            color: white;
            font-weight: bold;
            z-index: 1000;
            animation: slideIn 0.3s ease;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
        `;

        document.body.appendChild(notification);

        setTimeout(() => {
            notification.style.animation = 'slideOut 0.3s ease';
            setTimeout(() => notification.remove(), 300);
        }, 3000);
    }

    scrollToBottom() {
        setTimeout(() => {
            this.chatContainer.scrollTop = this.chatContainer.scrollHeight;
        }, 100);
    }
}

// Инициализация приложения
document.addEventListener('DOMContentLoaded', () => {
    window.tamerlaneAI = new TamerlaneAI();
    console.log('🏹 Тамерлан ИИ инициализирован');
});

// Добавляем CSS анимации
const style = document.createElement('style');
style.textContent = `
    @keyframes slideIn {
        from {
            transform: translateX(400px);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }

    @keyframes slideOut {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(400px);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);
