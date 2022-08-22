from django.contrib import admin

# Register your models here.
from AdminApp.views import Ingredient, Item, Requirements
from CustomerApp.models import Order

admin.site.register(Ingredient)
admin.site.register(Item)
admin.site.register(Requirements)
admin.site.register(Order)
