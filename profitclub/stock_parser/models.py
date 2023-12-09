from django.db import models


class Stocks(models.Model):
    stock = models.CharField(primary_key=True, max_length=30)
    category = models.CharField(max_length=30)
    price = models.IntegerField()
    change_percent = models.CharField(max_length=30)

    def __str__(self):
        return self.stock

    def save_to_database(self):
        self.save()
