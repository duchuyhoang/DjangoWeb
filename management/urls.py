from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from . import views
urlpatterns = [
    path('', views.AddProduct),
    path('addProduct', views.AddProduct),
	path('handleAddBook',csrf_exempt(views.handleAddProduct))
]
