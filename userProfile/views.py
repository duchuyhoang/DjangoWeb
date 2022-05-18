from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from database.models import BookItem, Order, BookImage

from pythonDjangoEcommerce.common.ultils import getUserInfo, renderWithPermission
from datetime import datetime

# Create your views here.

#


def index(request: HttpRequest):
    tab = request.GET.get('tab', None)
    if(request.user.id is None):
        return HttpResponseRedirect('/home')
    else:
        listOrders = list(Order.objects.all().filter(customer_id=request.user.id)
                          .select_related('status', "cart", "shipment", "payment"))
        # print('xx', listOrders[1].cart.paymentTypeName)
        for index, order in enumerate(listOrders):
            listItem = BookItem.objects.all().filter(cart_id=order.cart.idCart).values()
            order.listItem = listItem
            rawDate = order.date
            # order.date = datetime(rawDate.year)
            # print(order.date.isoformat())
            # order.date = datetime.strptime(order.date,'%d/%m/%y')
        try:
            userInfo = getUserInfo(request)[0]

            userInfo["birthday"] = datetime.strftime(
                userInfo["birthday"], '%Y-%m-%d')
            return render(request, 'index.html', {
                "tab": tab,
                "userInfo": userInfo,
                "user": request.user,
                "listOrders": listOrders
            })
        except IndexError:
            return render(request, 'index.html', {
                "tab": tab,
                # "userInfo": userInfo,
                "user": request.user,
                "listOrders": listOrders
            })
