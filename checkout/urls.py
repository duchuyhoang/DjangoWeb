from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
	path("",views.index),
	path("check",csrf_exempt(views.checkout))
]