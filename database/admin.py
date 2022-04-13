from django.contrib import admin
from .models import Category,Book,Publisher,Author,Address,Order,Cart,Shipment,Payment,BookItem, BookImage, Province, Ward, District,UserInfo;
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

class UserInline(admin.StackedInline):
    model = UserInfo
    can_delete = False
    verbose_name_plural = 'auth_user'
class UserAdmin(BaseUserAdmin):
    inlines = (UserInline,)

UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register([Category,Book,Publisher,Author,Address,Order,Cart,Shipment,Payment,BookItem, BookImage, Province, Ward, District])
