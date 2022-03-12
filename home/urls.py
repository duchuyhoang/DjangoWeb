from django.urls import path
import home.views as views
urlpatterns = [
    path('',views.index),
	# path("home/",home.index)
]