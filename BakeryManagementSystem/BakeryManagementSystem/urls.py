"""BakeryManagementSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import  include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from AdminApp.views import CalculatePrice, IngredientList, UserLogIn, UserSignUp2, UserLogOut
from CustomerApp.views import ShoppingCart, OrderHistory, AvailableItems

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', CalculatePrice.as_view()),
    path('ingredientList/', IngredientList.as_view()),
    path('login/', UserLogIn.as_view()),
    path('logout/',UserLogOut.as_view()),
    path('signup/', UserSignUp2.as_view()),
    path('item_list', ShoppingCart.as_view()),
    path('history/', OrderHistory.as_view()),
    path('showItems/', AvailableItems.as_view()),
    #path('check/', check),

]
