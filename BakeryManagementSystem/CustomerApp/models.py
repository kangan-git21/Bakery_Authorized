from django.db import models
from AdminApp.models import Item


class Order(models.Model):
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.item} of {self.quantity}"


