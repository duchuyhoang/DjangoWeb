from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render

from pythonDjangoEcommerce.common.ultils import getUserInfo, renderWithPermission
from datetime import datetime
# Create your views here.


def index(request: HttpRequest):
    tab = request.GET.get('tab', None)
    print(request.user.id)
    if(request.user.id is None):
        return HttpResponseRedirect('/home')
    else:
        try:
            userInfo = getUserInfo(request)[0]
            userInfo["birthday"] = datetime.strftime(
                userInfo["birthday"], '%Y-%m-%d')
            return render(request, 'index.html', {
                "tab": tab,
                "userInfo": userInfo,
                "user": request.user
            })
        except IndexError:
            return render(request, 'index.html', {
                "tab": tab,
                # "userInfo": userInfo,
                "user": request.user
            })
