from django.shortcuts import render
from django.views import View
from database.models import Book, BookImage
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from pythonDjangoEcommerce.common.ultils import renderWithPermission


def getInfor(request, id):
    book = Book.objects.get(idBook=id)
    images = BookImage.objects.filter(idBook=book)
    return renderWithPermission(request, "guest", render(request, 'product/infor.html', {'book': book, 'images': images}), HttpResponseRedirect('/home'))


def get(self, request):
    return render(request, 'product/index.html')