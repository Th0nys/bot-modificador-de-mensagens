import requests

bot_token = "6087028385:AAHRBTY2TvIM2yuhZkWOzZvVwwfQ9xwBiC4"
chat_id = "modificatest.bot"
msg = "Messege received from chatbot"


def send_message(msg):
   telegram_api_url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id=@{chat_id}&text={msg}"
   tel_resp = requests.get(telegram_api_url)
   if tel_resp.status_code == 200:
       print("Mensagem enviada ao grupo..")
   else:
       print("Mensagem não pôde ser enviada!!")

var = send_message('outra mensagem 1 2 3 ')
var


def message_ind(msg):
    params = {
    'offset': 0, 
    'limit': 10,
    }

    response = requests.get(f'https://api.telegram.org/bot{bot_token}/getUpdates', params=params)

    if response.status_code == 200:
        data = response.json()
        for update in data['result']:
            if 'message' in update and 'from' in update['message'] and update['message']['from']['is_bot']:
                message_id = update['message']['message_id']
    
    return message_id


def chat_ind(msg):
    url = f'https://api.telegram.org/bot{bot_token}/getUpdates'
    response = requests.get(url)
    
    if response.status_code == 200:
        update = response.json()['result'][-1]
        chat_id = update['message']['chat']['id']
    
    return chat_id
    


def edit_message():
    novo_texto = 'nova mensagem'
    message_id = message_ind(var)
    chat_id = chat_ind(var)
    url = f'https://api.telegram.org/bot{bot_token}/editMessageText'
    params = {'chat_id': chat_id, 'message_id': message_id, 'text': novo_texto}
    response = requests.post(url, params=params)

    # Verifique se a solicitação foi bem-sucedida
    if response.status_code == 200:
        print('A mensagem foi editada com sucesso!')
    else:
        print('Ocorreu um erro ao editar a mensagem.')

edit_message()
print(message_ind(var))
print(chat_ind(var))
