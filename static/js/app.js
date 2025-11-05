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
        this.providerSelect = document.getElementById('providerSelect');
        this.modelSelect = document.getElementById('modelSelect');
        this.sendBtnText = document.getElementById('sendBtnText');
        this.loadingSpinner = document.getElementById('loadingSpinner');
        this.statusIndicator = document.getElementById('statusIndicator');
        this.currentProvider = 'anthropic';
        this.providers = {};

        this.attachEventListeners();
        this.loadProviders();
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

        // Смена провайдера
        this.providerSelect.addEventListener('change', (e) => {
            this.currentProvider = e.target.value;
            this.loadModelsForProvider(this.currentProvider);
        });

        // Автоматическое изменение высоты textarea
        this.messageInput.addEventListener('input', () => {
            this.messageInput.style.height = 'auto';
            this.messageInput.style.height = this.messageInput.scrollHeight + 'px';
        });
    }

    async loadProviders() {
        try {
            const response = await fetch(`${this.apiUrl}/providers`);
            const data = await response.json();

            this.providers = data.providers;
            this.updateProvidersStatus();
            this.checkHealth();
        } catch (error) {
            console.error('Error loading providers:', error);
            this.checkHealth();
        }
    }

    updateProvidersStatus() {
        // Обновляем визуальный статус провайдеров
        Object.keys(this.providers).forEach(providerName => {
            const provider = this.providers[providerName];
            const option = this.providerSelect.querySelector(`option[value="${providerName}"]`);
            if (option) {
                const status = provider.configured ? '✅' : '⚠️';
                option.textContent = `${status} ${option.textContent.replace(/^(✅|⚠️)\s/, '')}`;
            }
        });
    }

    async loadModelsForProvider(providerName) {
        try {
            const response = await fetch(`${this.apiUrl}/providers/${providerName}/models`);
            const data = await response.json();

            // Обновляем список моделей
            this.modelSelect.innerHTML = '';
            data.models.forEach(model => {
                const option = document.createElement('option');
                option.value = model;
                option.textContent = model;
                this.modelSelect.appendChild(option);
            });

            // Показываем селектор моделей если есть выбор
            if (data.models.length > 1) {
                this.modelSelect.style.display = 'inline-block';
            } else {
                this.modelSelect.style.display = 'none';
            }
        } catch (error) {
            console.error('Error loading models:', error);
            this.modelSelect.style.display = 'none';
        }
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
            const requestBody = {
                message: message,
                session_id: this.sessionId,
                provider: this.currentProvider
            };

            // Добавляем модель если она выбрана
            if (this.modelSelect.value && this.modelSelect.style.display !== 'none') {
                requestBody.model = this.modelSelect.value;
            }

            const response = await fetch(`${this.apiUrl}/chat`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(requestBody)
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
                        <h2>🏹 Сәлеметсіз бе! Merhaba! Salom! Здравствуйте!</h2>
                        <p style="font-size: 1.1em; font-weight: bold; color: #8b4513; margin-bottom: 15px;">
                            Мен Тәмірлан - Түрік әлемінің жасанды интеллекті!<br>
                            Ben Timur - Türk dünyasının yapay zeka asistanı!<br>
                            Men Temur - Turk dunyosining sun'iy intellekt yordamchisi!<br>
                            Я Тамерлан - ИИ-ассистент тюркского мира!
                        </p>

                        <h3 style="color: #1e3a5f; margin-top: 20px;">💬 Барлық түркі тілдерінде сөйлеймін / Tüm Türk dillerinde konuşurum:</h3>
                        <div style="background: #f9f6f0; padding: 15px; border-radius: 10px; margin: 15px 0;">
                            <p style="margin: 5px 0;"><strong>Қазақша</strong> • <strong>Türkçe</strong> • <strong>O'zbek</strong> • <strong>Кыргызча</strong> • <strong>Azərbaycan</strong></p>
                            <p style="margin: 5px 0;"><strong>Татарча</strong> • <strong>Башҡортса</strong> • <strong>Түркмен</strong> • <strong>Саха тыла</strong> • <strong>Чӑваш</strong></p>
                        </div>

                        <h3 style="color: #1e3a5f; margin-top: 20px;">✨ Мен не істей аламын / Neler yapabilirim:</h3>
                        <ul>
                            <li>🏛️ <strong>Түрік тарихы</strong> / Türk tarihi / История тюркского мира</li>
                            <li>🗣️ <strong>Тілдерді үйрету</strong> / Dil öğretimi / Изучение всех тюркских языков</li>
                            <li>💻 <strong>Программалау</strong> / Programlama / Программирование (түркі тілдерінде!)</li>
                            <li>📚 <strong>Білім беру</strong> / Eğitim / Образование и наука</li>
                            <li>💼 <strong>Бизнес кеңесі</strong> / İş danışmanlığı / Бизнес-консультации</li>
                            <li>🎭 <strong>Мәдениет</strong> / Kültür / Традиции и культура</li>
                            <li>🌟 <strong>Күнделікті сұрақтар</strong> / Günlük sorular / Любые вопросы</li>
                        </ul>

                        <div style="background: linear-gradient(135deg, #1e3a5f 0%, #c9a961 100%); color: white; padding: 15px; border-radius: 10px; margin-top: 20px;">
                            <p class="hint" style="margin: 0; font-size: 1.05em;">
                                ✍️ Өз тіліңізде жазыңыз! / Kendi dilinizde yazın! / Пишите на своём языке!<br>
                                <span style="font-size: 0.9em; opacity: 0.9;">Мен автоматты түрде сіздің тіліңізді анықтаймын / Dilinizi otomatik algılarım</span>
                            </p>
                        </div>
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
