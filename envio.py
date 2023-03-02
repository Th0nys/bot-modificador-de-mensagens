import requests

bot_token = "6087028385:AAHRBTY2TvIM2yuhZkWOzZvVwwfQ9xwBiC4"
chat_id = "test_group157"
msg = "Messege received from chatbot"


def send_message(msg):
   telegram_api_url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id=@{chat_id}&text={msg}"
   tel_resp = requests.get(telegram_api_url)
   if tel_resp.status_code == 200:
       print("Mensagem enviada ao grupo..")
   else:
       print("Mensagem não pôde ser enviada!!")
      
send_message("nova mensagem")




