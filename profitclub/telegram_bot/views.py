from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from ..stock_parser.models import Stocks


@csrf_exempt
def get_curr(request):
    if request.method == 'GET':
        user_id = request.GET.get('user_id')

        currencies = Stocks.objects.all()
        curr_data = [{curr.stock, curr.price, curr.change_percent} for curr in currencies]

        return JsonResponse(curr_data)
