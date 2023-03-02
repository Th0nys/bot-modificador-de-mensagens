import requests
import id_message


bot_token = '6087028385:AAHRBTY2TvIM2yuhZkWOzZvVwwfQ9xwBiC4'
chat_id = id_message.chat_id
message_id = id_message.message_id

novo_texto = 'Este é o novo texto da mensagem.'

url = f'https://api.telegram.org/bot{bot_token}/editMessageText'
params = {'chat_id': chat_id, 'message_id': message_id, 'text': novo_texto}
response = requests.post(url, params=params)

if response.status_code == 200:
    print('A mensagem foi editada com sucesso!')
else:
    print('Ocorreu um erro ao editar a mensagem.')