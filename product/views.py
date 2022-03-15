from django.shortcuts import render
from django.views import View
from database.models import Book, BookImage

def getInfor(request, id):
    book = Book.objects.get(idBook = id)
    images = BookImage.objects.filter(idBook = book)
    return render(request, 'product/infor.html', {'book': book, 'images': images})



def get(self, request):
    return render(request, 'product/index.html')

