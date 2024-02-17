# myapp/google_forms.py

import requests

# URL вашей Google-формы
url = 'https://docs.google.com/forms/d/e/1FAIpQLSfF7QyxMNwVMx8J7tBeO_JhjXrX-KD9rqonmbL9qgnj3cQH-A/formResponse'

# Данные для отправки, замените их на реальные значения
data = {
    'entry.1234567890': 'Значение для поля 1',
    'entry.0987654321': 'Значение для поля 2',
    # Добавьте другие поля и значения по мере необходимости
}

# Отправка POST-запроса
response = requests.post(url, data=data)

# Проверка статуса ответа
if response.status_code == 200:
    print('Запрос успешно отправлен!')
else:
    print('Возникла проблема при отправке запроса:', response.status_code)
