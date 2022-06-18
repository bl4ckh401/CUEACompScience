from django.urls import path
from .views import GetCSRFToken, LogUserOut, LoginUser, RegisterUser

urlpatterns = [
    path('register/', RegisterUser.as_view()),
    path('login/', LoginUser.as_view()),
    path('logout/', LogUserOut.as_view()),
    path('getcsrf/', GetCSRFToken.as_view()),
]
