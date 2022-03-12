from urllib import request
from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
# Create your views here.


def index(req):
	response=HttpResponse()
	response.write("<h1>Hello world</h1>")
	return render(req,"index.django-html",{
		'content':not True
	})
	# return response