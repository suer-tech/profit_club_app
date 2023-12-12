import telebot
from .telegram_services.keyboard import *

from .telegram_services.get_price_service import get_curr
from .telegram_services.telegram_config import *

bot = telebot.TeleBot(token)


def run_bot():
    @bot.message_handler(commands=['start', 'help'])
    def send_welcome(message):
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIDZ2JEZuGR8N1D5s__y0O8cIUGMk9OAAIiEwACXWxwS64th70744A-IwQ')
        mess = f'Привет, <b>{message.from_user.first_name}</b>! Здесь будут уведомления об изменении цены по основным биржевым активам.'
        bot.reply_to(message, mess, reply_markup=greet_kb1)

    @bot.message_handler(content_types='text')
    def send_message(message):
        if message.text == "Индексы":
            mess = get_curr()
            bot.send_message(message, mess)

    @bot.message_handler(func=lambda message: True)
    def echo_all(message):
        bot.reply_to(message, message.text)

    bot.infinity_polling()
