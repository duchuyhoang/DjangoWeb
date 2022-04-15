from django.shortcuts import render
from django.views import View
from database.models import Book, BookImage


class HomeView(View):
    def get(self, request):
        list_book = Book.objects.all()
        # list_book_display
        listBook = []
        for item in list_book:
            images = BookImage.objects.filter(idBook=item)
            image = ''
            if len(images)>0:
                image = images[0].image
            listBook.append(
                {
                    'idBook': item.idBook,
                    'quantity': item.quantity,
                    'name': item.name,
                    'image': image,
                    'description': item.description,
                    'publisher_id': item.publisher_id,
                    'price': item.price,
                    'salePrice': item.salePrice,
                    'priceSale': item.price-item.price*item.salePrice
                }
            )
        for item in listBook:
            print(item)
        context = {"listBook": listBook}
        return render(request, 'homepage/index.html', context)
