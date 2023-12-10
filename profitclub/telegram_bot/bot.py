import requests
import telebot
from django.urls import reverse


bot = telebot.TeleBot('6419893616:AAG-tbu524ZN7IGIulbJA_ZxNLykdaJWeU0')


@bot.message_handler(commands=['Индексы'])
def get_currency_handler(message):
    user_id = message.chat.id
    # Отправить запрос к Django серверу для получения данных о валютах
    response = requests.get(f'http://yourdomain.com{reverse("telegram_bot:get_curr")}?user_id={user_id}')
    data = response.json()
    bot.send_message(user_id, data)


# Запуск обработчика событий бота
bot.polling()
