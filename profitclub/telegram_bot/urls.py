from django.urls import path
from . import views

app_name = 'telegram_bot'

urlpatterns = [
    path('get_curr/', views.get_curr, name='get_curr'),
]
