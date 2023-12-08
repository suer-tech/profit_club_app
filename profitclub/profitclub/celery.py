from celery.schedules import crontab
import os
from celery import Celery


# Установка переменной окружения для использования настроек Django в Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'profitclub.settings')

# Создание экземпляра Celery
celery_app = Celery('profitclub')

# Загрузка настроек из файла settings.py проекта Django
celery_app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматическое обнаружение и регистрация задач из файлов tasks.py
celery_app.autodiscover_tasks()

celery_app.conf.beat_schedule = {
    'your-periodic-task': {
        'task': 'profitclub.stock_parser.parsing_tasks.async_parsing_task',
        'schedule': crontab(minute='*/10'),  # Например, каждые 10 минут
    },
}