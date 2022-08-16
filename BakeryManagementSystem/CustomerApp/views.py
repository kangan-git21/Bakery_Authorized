from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from AdminApp.models import Item
from AdminApp.serializers import ItemSerializer
from CustomerApp.models import Order
from CustomerApp.serializers import OrderSerializer

"""Items available in bakery, customer can see"""


class AvailableItems(APIView):
    def get(self, request):
        get_item = Item.objects.all()
        item_serializer = ItemSerializer(get_item, many=True)
        return Response(item_serializer.data)


""" Shopping Cart for what customer orders and view it later"""


class ShoppingCart(APIView):
    def post(self, request):
        if request.user.is_superuser:
            return Response({'User': 'Not Allowed'}, status=status.HTTP_403_FORBIDDEN)
        else:
            serializer = OrderSerializer(data=request.data)
            items_all = Order.objects.filter(item=request.data['item'])
            if serializer.is_valid():
                serializer.save()
                return Response({'Items': 'Ordered'}, status=status.HTTP_201_CREATED)
            return Response({'Note': "Can't proceed"}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request):
        if request.user.is_superuser:
            return Response({'User': 'Not Allowed'}, status=status.HTTP_403_FORBIDDEN)
        else:
            item = Order.objects.all()
            serializer = OrderSerializer(item, many=True)
            return Response(serializer.data)

    def patch(self, request):
        if request.user.is_superuser:
            return Response({'User': 'Not Allowed'}, status=status.HTTP_403_FORBIDDEN)
        else:
            previous_list = Order.objects.get(item=request.data['item'])
            if previous_list is not None:
                previous_list.quantity -= request.data['quantity']
            return Response(previous_list)


"""Cart History"""


class OrderHistory(APIView):
    def get(self, request):
        if request.user.is_superuser:
            return Response({'User': 'Not Allowed'}, status=status.HTTP_403_FORBIDDEN)
        else:
            show_item = Order.objects.all()
            serializer_history = OrderSerializer(show_item, many=True)
            return Response(serializer_history.data)









# Create your views here.
