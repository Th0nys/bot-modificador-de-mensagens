import requests

bot_token = '6087028385:AAHRBTY2TvIM2yuhZkWOzZvVwwfQ9xwBiC4'

url = f'https://api.telegram.org/bot{bot_token}/getUpdates'
response = requests.get(url)

if response.status_code == 200:
    update = response.json()['result'][-1]
    chat_id = update['message']['chat']['id']
    message_id = update['message']['message_id']
    print(f'O chat_id da mensagem é {chat_id} e o message_id é {message_id}.')
else:
    print('Ocorreu um erro ao obter as atualizações do bot.')