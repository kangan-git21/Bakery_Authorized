from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .models import Ingredient, Item, LoginUser

"""User (from django)"""


class UserSerializer(serializers.ModelSerializer):
    def create(self, *args, **kwargs):
        user = super().create(*args, **kwargs)
        p = user.password
        user.set_password(p)
        user.save()
        return user

    def update(self, *args, **kwargs):
        user = super().update(*args, **kwargs)
        p = user.password
        user.set_password(p)
        user.save()
        return user

    class Meta:
        model = User
        fields = '__all__'


"""Login User"""


"""Login User"""


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginUser
        fields = ['username', 'password']


"""Ingredients"""


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['name', 'quantity', 'cost_price']


"""Item"""


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['item_name', 'quantity']

