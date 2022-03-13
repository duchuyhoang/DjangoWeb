from django.shortcuts import render
from django.views import View

class ProductView(View):
    def get(self, request):
        return render(request, 'product/index.html')