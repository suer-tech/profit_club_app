from ...stock_parser.models import Stocks


def get_curr():
    currencies = Stocks.objects.all()
    curr_data = [{curr.stock, curr.price, curr.change_percent} for curr in currencies]

    return curr_data