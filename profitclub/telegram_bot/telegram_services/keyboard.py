from telebot.types import ReplyKeyboardMarkup, KeyboardButton

button_index = KeyboardButton("Индексы")
button_crypto = KeyboardButton("Крипто")
button_spread = KeyboardButton("Спреды")
greet_kb1 = ReplyKeyboardMarkup(resize_keyboard=True).add(button_index).row(button_crypto).row(button_spread)

usd = KeyboardButton("USD")
eur = KeyboardButton("EUR")
cny = KeyboardButton("CNY")
back = KeyboardButton("Главное меню")
greet_curr = ReplyKeyboardMarkup(resize_keyboard=True).add(usd).add(eur).add(cny).row(back)

