from django.urls import path, include
from .views import Login, Signout, SignUp
from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
    path('login', csrf_exempt(Login)),
    path('signOut', csrf_exempt(Signout)),
    path('signUp', csrf_exempt(SignUp))
]
