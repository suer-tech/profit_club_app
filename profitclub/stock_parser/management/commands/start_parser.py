from django.core.management.base import BaseCommand
from ...parsing_tasks import async_parsing_task


class Command(BaseCommand):
    help = 'Запуск'

    def handle(self, *args, **options):
        # Вызов вашей асинхронной задачи
        async_parsing_task.delay()
        self.stdout.write(self.style.SUCCESS('Задача запущена'))