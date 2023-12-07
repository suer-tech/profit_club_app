from profitclub.stock_parser.services.parser import format_number, get_price
import services.parsing_config as investing


class Control:
    stock = {}
    get_price(stock['name'], stock['url'], stock['xpath'], stock['xpath_proc'])

for currency in curr_arr:
    formatted_value = format_number(currency[1])
    formatted_proc = format_number(currency[2])
    proc_without_brackets = formatted_proc.replace("(", "").replace(")", "")


for stock in investing.currencies: