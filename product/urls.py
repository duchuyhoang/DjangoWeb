from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.get, name='index'),
    path('infor/<int:id>', views.getInfor),
]
