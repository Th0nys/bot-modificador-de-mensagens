from telegram.ext import *


def sample_responses(update, text):
    user_message = str(input()).lower()

    if user_message in ("olá"):
        user_message = update.message.text('hello')