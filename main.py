import Constants as keys
from telegram.ext import *
import Responses as R


def start_commands(update, context):
    update.message.reply_text('')
    pass


def hellp_commands(update, context):
    update.message.reply_text('')
    pass


def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)

    update.message.reply_text(response)


def error(update, context):
    print(f"Update {update} caused error {context.error}")


def main():
    updater = Updater(keys.API_KEY, use_context=True)
    updater.start_polling()





