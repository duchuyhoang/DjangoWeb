from django.contrib import admin
from .models import Category,Book,Publisher,Author,Address,Order,Cart,User,Shipment,Payment,BookItem, BookImage, Province, Ward, District;

admin.site.register([Category,Book,Publisher,Author,Address,Order,Cart,User,Shipment,Payment,BookItem, BookImage, Province, Ward, District])
# Register your models here.
