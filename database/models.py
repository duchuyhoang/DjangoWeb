from asyncio.windows_events import NULL
from email.policy import default
from pickle import TRUE
from threading import local
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.


from django.contrib.auth.models import User
User._meta.get_field('email')._unique = True
User._meta.get_field('username')._unique = False

class UserRole(models.Model):
    idRole = models.AutoField(primary_key=True)
    roleName = models.CharField(max_length=50)

    class Meta:
        db_table = 'userRole'

    def __str__(self):
        return self.roleName


class Province(models.Model):
    id = models.CharField(max_length=8, unique=True, primary_key=True)
    name = models.TextField()
    type = models.TextField()

    class Meta:
        db_table = 'province'

    def __str__(self):
        return self.type + " "+self.name


class District(models.Model):
    id = models.CharField(max_length=8, unique=True, primary_key=True)
    name = models.TextField()
    type = models.TextField()
    province_id = models.ForeignKey(Province, on_delete=models.CASCADE)

    class Meta:
        db_table = 'district'

    def __str__(self):
        return self.type + " "+self.name


class Ward(models.Model):
    id = models.CharField(max_length=8, unique=True, primary_key=True)
    name = models.TextField()
    type = models.TextField()
    province = models.ForeignKey(Province, on_delete=models.CASCADE, null=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'ward'

    def __str__(self):
        return self.type + " "+self.name


class Address(models.Model):
    id_address = models.AutoField(primary_key=True)
    province = models.ForeignKey(
        Province, null=True, on_delete=models.SET_NULL)
    district = models.ForeignKey(
        District, null=True, on_delete=models.SET_NULL)
    ward = models.ForeignKey(Ward, null=True, on_delete=models.SET_NULL)
    note = models.TextField(max_length=255, default=NULL)

    class Meta:
        db_table = 'address'

    def __str__(self):
        return "Province:"+self.province.name + " District:" + self.district.name + " Ward:"+self.ward.name


# class User(models.Model):
#     idAccount = models.AutoField(primary_key=True)
#     userName = models.CharField(max_length=100)
#     password = models.CharField(max_length=50)
#     birthday = models.DateTimeField(null=False)
#     gender = models.CharField(max_length=20)
#     phone = models.CharField(max_length=11)
#     role = models.ForeignKey(UserRole, on_delete=models.SET_NULL, null=True)
#     address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)

#     def __str__(self):
#         return self.userName

#     class Meta:
#         db_table = 'customer'


class Author(models.Model):
    idAuthor = models.AutoField(primary_key=True)
    name = models.TextField(max_length=255, null=False)
    age = models.IntegerField(null=False, default=0)

    class Meta:
        db_table = "author"

    def __str__(self):
        return self.name


class Publisher(models.Model):
    idPublisher = models.AutoField(primary_key=True)
    name = models.TextField(max_length=255, null=False)
    location = models.TextField(max_length=255, null=False)
    delFlag = models.BooleanField(default=False)

    class Meta:
        db_table = "publisher"

    def __str__(self):
        return self.name


class Category(models.Model):
    idCategory = models.AutoField(primary_key=True)
    name = models.TextField(max_length=255, null=False)
    delFlag = models.BooleanField(default=False)

    class Meta:
        db_table = "category"

    def __str__(self):
        return self.name


class Book(models.Model):
    idBook = models.AutoField(primary_key=True)
    quantity = models.IntegerField(null=False)
    name = models.TextField(max_length=255, null=False)
    image = models.ImageField(null=False, upload_to="uploads/")
    description = models.TextField(max_length=255, default="")
    publisher = models.ForeignKey(
        Publisher, on_delete=models.SET_NULL, null=True)
    category = models.ManyToManyField(Category)
    price = models.FloatField(default=0)
    salePrice = models.FloatField(default=0)

    class Meta:
        db_table = "book"

    def __str__(self):
        return self.name


class Cart(models.Model):
    idCart = models.AutoField(primary_key=True)
    totalPrice = models.FloatField(default=0)
    createAt = models.TimeField(auto_now_add=True, blank=True)

    class Meta:
        db_table = "cart"

    def __str__(self):
        return "cart " + str(self.idCart)


class BookItem(models.Model):
    idBookItem = models.AutoField(primary_key=True)
    idBook = models.ForeignKey(Book, null=True, on_delete=models.SET_NULL)
    totalPrice = models.FloatField(default=0)
    quantity = models.IntegerField(default=0)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

    class Meta:
        db_table = "book_item"

    def __str__(self):
        return "Book " + str(self.idBook)


class Shipment(models.Model):
    idShipment = models.AutoField(primary_key=True)
    message = models.TextField(null=True)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = "shipment"

    def __str__(self):
        return "Shipment " + str(self.idShipment)


class OrderStatus(models.Model):
    idStatus = models.AutoField(primary_key=True)
    name: models.CharField(max_length=100)

    class Meta:
        db_table = "order_status"

    def __str__(self):
        return self.name


class Payment(models.Model):
    idPaymentType = models.AutoField(primary_key=True)
    paymentTypeName = models.CharField(max_length=100)

    class Meta:
        db_table = "payment"

    def __str__(self):
        return self.paymentTypeName


class Order(models.Model):
    idOrder = models.AutoField(primary_key=True)
    date = models.TimeField(auto_now_add=True, blank=True)
    status = models.ForeignKey(
        OrderStatus, on_delete=models.SET_NULL, null=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    shipment = models.ForeignKey(
        Shipment, on_delete=models.SET_NULL, null=True)
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = "order"

    def __str__(self):
        return "Order "+str(self.idOrder)


class BookImage(models.Model):
    idBookImage = models.AutoField(primary_key=TRUE)
    idBook = models.ForeignKey(
        Book, null=True, on_delete=models.SET_NULL
    )
    image = models.ImageField(null=True, upload_to="uploads/")

    class Meta:
        db_table = "book_image"


class UserInfo(models.Model):
    phone = models.TextField(max_length=11)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    avatar = models.ImageField(null=True, upload_to="uploads/")
    birthday = models.DateField(default=datetime.datetime.now())

    class Meta:
        db_table = "user_info"
