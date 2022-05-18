from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.core import serializers
from django.contrib.auth.models import User
from database.models import OrderStatus, Ward, Province, District, Payment, OrderType, Cart, BookItem, Shipment, Address, Order, Book
# Create your views here.
defaultOrderStatus = 1


def index(request: HttpRequest):
    listDistrict = list(District.objects.all().values())
    listProvince = list(Province.objects.all().values())
    listWard = list(Ward.objects.all().values())
    payment = list(Payment.objects.all().values())
    orderType = list(OrderType.objects.all().values())
    cartInfo = request.session.get("cart")
    listItem = cartInfo["items"] if cartInfo is not None else []
    total = 0
    for item in listItem:
        total += float(item["price"])*float(item["quantity"])
    return render(request, "checkout.html", {
        "listDistrict": listDistrict,
        "listProvince": listProvince,
        "listWard": listWard,
        "listItem": listItem,
        "listPaymentType": payment,
        "listOrderType": orderType,
        "total": total
    })


def checkout(request: HttpRequest):
    if(request.user.id is None):
        return HttpResponseBadRequest("Need to login")

    if(request.session.get("cart") is None):
        return HttpResponseBadRequest("Need a cart")

    if(request.method == "POST"):
        body = request.POST
        cart = request.session.get("cart")
        user = User.objects.get(id=request.user.id)
        district = District.objects.get(id=body.get("receiverDistrict"))
        ward = Ward.objects.get(id=body.get("receiverWard"))
        province = Province.objects.get(id=body.get("receiverCity"))
        address = Address.objects.create(
            province=province, ward=ward, district=district, note=body.get("receiverAddressNote"))
        address.save()
        shipment = Shipment.objects.create(
            address=address, message=body.get("receiverOrderNote"))
        shipment.save()
        payment = Payment.objects.get(
            idPaymentType=body.get("receiverPayment"))
        listItem = []
        cartDb = Cart.objects.get(idCart=cart["cart"])
        orderStatus = OrderStatus.objects.get(idStatus=defaultOrderStatus)
        for item in cart["items"]:
            book = Book.objects.get(idBook=item["idBook"])
            if(book is not None):
                bookItem = BookItem.objects.create(
                    idBook=book, totalPrice=float(item["price"])*float(item["quantity"]), quantity=item["quantity"], cart=cartDb)
                bookItem.save()
                listItem.append(bookItem)

        order = Order.objects.create(
            cart=cartDb,
            customer=user,
            shipment=shipment,
            status=orderStatus,
            payment=payment,
            receiverFirstName=body.get("receiverFirstName"),
            receiverLastName=body.get("receiverLastName"),
            receiverEmail=body.get("receiverEmail")
        )
        order.save()
        request.session["cart"] = None
        return HttpResponse("Order successful")
    else:
        return HttpResponseBadRequest("Failed")
