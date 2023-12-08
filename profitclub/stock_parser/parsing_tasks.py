from celery import shared_task
from .models import Stocks
from .services.parser import format_number, get_price
from .services.parsing_config import *


def create_data(category, stock_category):
    result_arr = []
    for stock in stock_category:
        price_arr = get_price(stock['name'], stock['url'], stock['xpath'], stock['xpath_proc'])
        result_arr.append(price_arr)

    for result in result_arr:
        formatted_value = format_number(result[1])
        formatted_proc = format_number(result[2])
        proc_without_brackets = formatted_proc.replace("(", "").replace(")", "")

        Stocks.stock = result[0]
        Stocks.category = category
        Stocks.price = formatted_value
        Stocks.change_percent = proc_without_brackets

@shared_task
def async_parsing_task():
    create_data('Валюты', currencies)
    create_data('Товары', comodities)
    create_data('Индексы', index)
