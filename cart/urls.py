from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from . import views
urlpatterns = [
    # path('', views.AddProduct),
    path('addToCart', csrf_exempt(views.addToCart)),
	path("removeItem",csrf_exempt(views.deleteAnItem))
    # path('handleAddBook',csrf_exempt(views.handleAddProduct))
]
