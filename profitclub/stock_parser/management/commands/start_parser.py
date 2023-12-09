from django.core.management.base import BaseCommand
from ...parser import parsing


class Command(BaseCommand):
    help = 'Запуск'

    def handle(self, *args, **options):
        parsing()
        self.stdout.write(self.style.SUCCESS('Задача запущена'))
