from unicodedata import category
from django.http import HttpRequest, HttpResponseBadRequest, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from database.models import BookImage, Book, Category, District, Ward, Province, Category, Publisher, Author
from pythonDjangoEcommerce.common.ultils import generateRandomString, getUserInfo, renderWithPermission
from django.core import serializers
import numpy as np
import json
from django.core.files.storage import FileSystemStorage


def getCurrentPathAction(request):
    action = ""
    try:
        action = request.path.split('/')[2]
    except:
        pass
    return action


def mapQuerySet(item):
    newDict = item.__dict__
    # _state, *rest = newDict
    if("_state" in newDict):
        del newDict["_state"]
    return newDict


def AddProduct(request: HttpRequest):
    listWard = Ward.objects.all()
    listDistrict = District.objects.all()
    listProvince = Province.objects.all()
    listCategory = Category.objects.all()
    listPublisher = Publisher.objects.all()
    listAuthor = Author.objects.all()

    # print(json.dumps(list(map(mapQuerySet,listProvince))))
    # print(list(map(mapQuerySet, listProvince)))

    return renderWithPermission(request, "is_superuser", render(request, 'product/AddProduct.html', {
        "action": getCurrentPathAction(request),
        "userInfo": request.userInfo,
        "listProvince": list(map(mapQuerySet, listProvince)),
        "listDistrict": list(map(mapQuerySet, listDistrict)),
        "listWard": list(map(mapQuerySet, listWard)),
        "listCategories": list(map(mapQuerySet, listCategory)),
        "listPublisher": list(map(mapQuerySet, listPublisher)),
        "listAuthor": list(map(mapQuerySet, listAuthor)),
    }), HttpResponseRedirect('/home'))


def handleAddProduct(request: HttpRequest):
    fs = FileSystemStorage(location="uploads/")

    if(request.method == "POST"):
        try:
            submitData = request.POST
            print(submitData)
            newBook = Book(
                name=submitData["bookName"],
                quantity=submitData["bookQuantity"],
                description=submitData["bookDescription"],
                publisher_id=submitData["bookManufacture"],
                price=submitData["bookPrice"],
                salePrice=submitData["salePrice"],
            )
            newBook.save()
            categories = submitData["bookCategory"].split(",")
            if(categories[0] is not ''):
                for categoryId in categories:
                    newBook.category.add(categoryId)

            for file in request.FILES.getlist("bookImage[]"):
                fileName = fs.save(file.name, file)
                file_url = fs.url(fileName)
                print('url', file_url)
                bookImage = BookImage(
                    image=file_url,
                    idBook=newBook
                )
                bookImage.save()

            return JsonResponse({"message": "Success"})
        except:
            return HttpResponseBadRequest("Something wrong")

    return HttpResponseBadRequest("Something wrong")
