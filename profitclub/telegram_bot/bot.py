import requests
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove
from aiogram.utils import executor
from keyboard import *

from profitclub.telegram_bot.telegram_services.get_price_service import get_curr
from telegram_services.telegram_config import *

bot = Bot(token)
dp = Dispatcher(bot)


async def start_telegram_handlers(dp):
    @dp.message_handler(commands=['start'])
    async def process_start_command(message: types.Message):
        await bot.send_sticker(message.chat.id,
                               'CAACAgIAAxkBAAIDZ2JEZuGR8N1D5s__y0O8cIUGMk9OAAIiEwACXWxwS64th70744A-IwQ')
        mess = f'Привет, <b>{message.from_user.first_name}</b>! Здесь будут уведомления об изменении цены по основным биржевым активам.'
        await bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=greet_kb1)

    @dp.message_handler(Text(equals="Индексы"))
    async def get_price(message: types.Message):
        mess = get_curr()
        await bot.send_message(message.chat.id, mess, reply_markup=greet_kb1)

    executor.start_polling(dp)
