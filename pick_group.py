import requests
from time import sleep

token = '6087028385:AAHRBTY2TvIM2yuhZkWOzZvVwwfQ9xwBiC4'
last_update_id = 0

def get_message():
    url = f'https://api.telegram.org/bot{token}/getUpdates'
    response = requests.get(url)
    dados = response.json()

    if response.json()['result']:
        # Itera sobre cada atualização de mensagem disponível
        for result in response.json()['result']:
            # Extrai o ID da atualização de mensagem
            update_id = result['update_id']

            # Verifica se a atualização de mensagem é mais recente do que a última atualização recebida
            if update_id > last_update_id:
                # Atualiza o último ID de atualização recebido
                last_update_id = update_id

                # Extrai o conteúdo da mensagem recebida
                message = result['message']
                content = message.get('text', '')  # Extraindo o campo de texto da mensagem. Se não houver um campo de texto, a variável content será vazia.

                # Exibe o conteúdo da mensagem na saída padrão
                print(content)
    else:
        print('Não há novas mensagens disponíveis.')

    last_message = response.json()['result'][-1]['message']['text']
    chat_user = response.json()['result'][0]['message']['chat']['id']

    if last_message == 'send a message':
        send_message(chat_user, 'please send the name of the group you want to send a message')
        get_chat_id()
        send_message(chat_user, 'wait a moment')

    return last_message


def send_message(chat_id):
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    requests.post(url, data={'chat_id': chat_id, 'text': 'specify the message that you want to send'})
    #receber e guardar a mensagem

    #bot solicita o nome do grupo

    #bot manda mensagem pro grupo

    response = requests.post(url, data={'chat_id': chat_id, 'text': text})

    if response.status_code == 200:
        send_message(chat_id, 'sucess!')
        print('Mensagem enviada com sucesso!')
    else:
        send_message(chat_id, 'things didnt work well')
        print('Erro ao enviar a mensagem.')


def get_user_id(update):
    # Obtenha o user_id do usuário que enviou a mensagem
    user_id = update['message']['from']['id']
    return user_id

def get_chat_id(token, user_id):
    # Envie uma mensagem vazia para o usuário
    response = requests.post(f'https://api.telegram.org/bot{token}/sendMessage', data={'chat_id': user_id, 'text': ''})

    # Verifique se a mensagem foi enviada com sucesso
    if response.status_code == 200:
        # Obtenha o chat_id do usuário a partir da resposta da API
        data = response.json()
        chat_id = data['result']['chat']['id']
        return chat_id
    else:
        return None


offset = 0

while True:
    # Envie uma solicitação HTTP GET para a API do Telegram para receber novas mensagens
    response = requests.get(f'https://api.telegram.org/bot{token}/getUpdates', params={'offset': offset})

    # Verifique se a solicitação foi bem-sucedida e se há novas mensagens
    if response.status_code == 200:
        data = response.json()
        if data['ok']:
            # Processar cada mensagem recebida
            for update in data['result']:
                att = data['result'][-1]
                # Armazenar a mensagem em uma lista, banco de dados ou arquivo
                message = update['message']['text']
                print(f'Mensagem recebida: {message}')
                if message == 'send message':
                    user_id = get_user_id(att)
                    send_message(user_id)
                # Atualizar o offset para receber apenas novas mensagens
                offset = update['update_id'] + 1
    else:
        print('Erro ao receber mensagens.')
