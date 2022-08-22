from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from django.contrib import admin
from django.urls import path
from AdminApp.views import UserSignUp, UserLogOut, UserLogIn, IngredientList, CalculatePrice
from CustomerApp.views import ShoppingCart, AvailableItems, OrderHistory

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', CalculatePrice.as_view()),
    path('ingredientList/', IngredientList.as_view()),
    path('login/', UserLogIn.as_view()),
    path('logout/', UserLogOut.as_view()),
    path('signup/', UserSignUp.as_view()),
    path('item_list', ShoppingCart.as_view()),
    path('history/', OrderHistory.as_view()),
    path('showItems/', AvailableItems.as_view()),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]
