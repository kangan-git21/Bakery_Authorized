from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status

from .serializers import IngredientSerializer, UserSerializer, LoginSerializer
from .models import Ingredient, Item, Requirements


from rest_framework.views import APIView
from rest_framework.response import Response

"""Sign Up the user"""


class UserSignUp2(APIView):
    def get(self, request):
        user_details = User.objects.all()
        serializer = UserSerializer(user_details, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'serializer': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)


"""Login User"""


class UserLogIn(APIView):

    @csrf_exempt
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = request.data['username']
            password = request.data['password']
            x = authenticate(username=username, password=password)
            if x is not None:
                login(request, x)
                return Response({"user": "Logged in"}, status=status.HTTP_200_OK)
            else:
                return Response({"Credentials": "invalid"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"Serializer": "invalid"}, status=status.HTTP_404_NOT_FOUND)


"""Logout the user"""


class UserLogOut(APIView):

    def get(self, request):
        logout(request)
        return Response({'User': 'Logged Out'}, status=status.HTTP_200_OK)


""" Ingredients--> Add them, Fetch them, Update them"""


class IngredientList(APIView):
    def get(self, request):
        if not request.user.is_superuser:
            return Response({'User': 'Not Allowed'}, status=status.HTTP_403_FORBIDDEN)
        else:
            ingredients = Ingredient.objects.all()
            serializer = IngredientSerializer(ingredients, many=True)
            return Response(serializer.data)

    def post(self, request):
        if not request.user.is_superuser:
            return Response({'User': 'Not Allowed'}, status=status.HTTP_403_FORBIDDEN)
        else:
            serializer = IngredientSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'items': 'Ingredients Created'}, status=status.HTTP_201_CREATED)
            return Response({'List': 'Not Valid'}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        if not request.user.is_superuser:
            return Response({'User': 'Not Allowed'}, status=status.HTTP_403_FORBIDDEN)
        else:
            previous_ingredients = Ingredient.objects.get(name=request.data['name'])
            if previous_ingredients is not None:
                previous_ingredients.quantity += request.data['quantity']
                previous_ingredients.save()
                return Response({'items': 'Ingredients updated'}, status=status.HTTP_200_OK)
            else:
                return Response({'Ingredient': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)


"""cCalculating price of One respective item"""


class CalculatePrice(APIView):
    def get(self, request):
            item = Item.objects.all()
            selling_price_dict = {}
            for i in item:
                ingredient = Requirements.objects.filter(need_item=i)
                amount = 0
                for x in ingredient:
                    # return HttpResponse(x.need_ingredients.cost_price)]]
                    amount += x.need_ingredients.cost_price * x.need_quantity
                    amount += amount*20//100
                    selling_price_dict[i.item_name] = amount
            return Response(selling_price_dict.items())



