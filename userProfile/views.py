from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from tomlkit import date
from pythonDjangoEcommerce.common.ultils import renderWithPermission
from datetime import datetime
# Create your views here.


def index(request: HttpRequest):
	tab = request.GET.get('tab', None)
	print(tab)
	if(request.userInfo is None):
		return HttpResponseRedirect('/home')
	else:
		userInfo = request.userInfo
		userInfo.birthday = datetime.strftime(userInfo.birthday, '%Y-%m-%d')
		return render(request, 'index.html', {
			"tab": tab,
			"userInfo": request.userInfo,
			"user": request.user
		})
