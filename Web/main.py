import requests

response = requests.get('https://rozetka.com.ua/')
with open('new.html', 'wt', encoding='utf-8') as file:
    file.write(response.text)
