from django.core.management.base import BaseCommand

from ... bot import run_bot


class Command(BaseCommand):
    help = 'Запуск'

    def handle(self, *args, **options):
        run_bot()
        self.stdout.write(self.style.SUCCESS('Задача запущена'))

