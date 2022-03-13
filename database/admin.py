from django.contrib import admin
from .models import Category,Book,Publisher,Author,Address,Order,Cart,User,Shipment,Payment,BookItem;

admin.site.register([Category,Book,Publisher,Author,Address,Order,Cart,User,Shipment,Payment,BookItem])
# Register your models here.
