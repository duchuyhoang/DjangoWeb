from django.http import HttpRequest, HttpResponseNotFound, HttpResponse
from django.shortcuts import render
from django.core import serializers
from database.models import Book, BookItem, Cart, BookImage

# Create your views here.


def addToCart(request: HttpRequest):
    newCartInfo = {
        "cart": "",
        "items": []
    }

    if request.session.get("cart") is None:
        newCart = Cart.objects.create()
        newCart.save()
        newCartInfo = {
            "cart": newCart.idCart,
            "items": []
        }
    else:
        newCartInfo = request.session.get("cart")

    if(request.method == "POST"):
        book = Book.objects.all().filter(idBook=request.POST.get("id_product"))
        if(len(book) == 0):
            return HttpResponseNotFound("Id not found")
        currentCart = Cart.objects.get(idCart=newCartInfo["cart"])
        selectedBook = book.values()[0]
        bookImage = BookImage.objects.all().filter(idBook=book[0].idBook)
        imageList = bookImage.values()
        bookItem = {
            "idBook": book[0].idBook,
            "name": book[0].name,
            "cart": currentCart.idCart,
            "quantity": request.POST.get("quantity"),
            "realPrice":selectedBook["price"],
            "price": selectedBook["price"] -
            selectedBook["price"]*(selectedBook["salePrice"]),
            "image": imageList[0]["image"] if len(imageList) > 0 else ""
        }

        # bookItemJson = serializers.serialize('json', [bookItem])
        isBookExist = False

        for index, item in enumerate(newCartInfo["items"]):
            # for obj in serializers.deserialize('json', item):
            # _bookItem = obj.object
            # print(_bookItem.idBook["idBook"],selectedBook["idBook"])
            # print(item)
            if(item["idBook"] == selectedBook["idBook"]):
                # _bookItem.quantity += int(bookItem.quantity)
                isBookExist = True
                newCartInfo["items"][index]["quantity"] = int(
                    newCartInfo["items"][index]["quantity"]) + int(bookItem["quantity"])
                # = serializers.serialize('json', [
                #                                                     _bookItem])

        if(isBookExist is False):
            newCartInfo["items"].append(bookItem)

        print(newCartInfo)
        request.session["cart"] = newCartInfo

    return HttpResponse("Ok")


def deleteAnItem(request: HttpRequest):
    idProduct = request.POST.get("idProduct")
    if(request.method == "POST" and idProduct is not None):
        currentCart = request.session.get("cart")

        if(currentCart is not None):
            listItem = currentCart["items"]
            for index, item in enumerate(listItem):
                if(str(item["idBook"]) == str(idProduct)):
                    print("ok")
                    del listItem[index]
                    break
        currentCart["items"] = listItem
        request.session["cart"] = currentCart

    return HttpResponse("Ok")


# def payCart(request:HttpRequest):
