from django.core.management.base import BaseCommand

from profitclub.telegram_bot.bot import *
from profitclub.telegram_bot.telegram_services.telegram_config import *

from ...parser import parsing



class Command(BaseCommand):
    help = 'Запуск'

    def handle(self, *args, **options):
        parsing()
        self.stdout.write(self.style.SUCCESS('Задача запущена'))

        start_telegram_handlers(dp)