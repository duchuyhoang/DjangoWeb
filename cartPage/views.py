from django.http import HttpRequest
from django.shortcuts import render
from django.views import View

# Create your views here.


def index(request: HttpRequest):
    cart = request.session.get("cart")
    listItems = []
    if(cart is not None):
        listItems = request.session.get("cart")["items"] if request.session.get("cart")[
            "items"] is not None else []
    print(listItems)
    return render(request, 'cart.html', {
        "listItems": listItems
    })
