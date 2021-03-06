from django.shortcuts import render
from django.http.request import HttpRequest
from django.http import HttpResponseNotFound, JsonResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
import datetime
from django.core.files.storage import FileSystemStorage
from database.models import UserInfo
from django.db import IntegrityError
import json


def Login(request: HttpRequest):
    if(request.method == "POST"):
        user = authenticate(
            username=request.POST["email"], password=request.POST["password"])
        if(user is None or user.is_anonymous is True):
            return HttpResponseNotFound("Wrong email or password")

        login(request, user)
		# request.session.
        # request.session['user'] = "huy"
        return JsonResponse({"message": "ok"})
    else:
        return HttpResponseNotFound("Wrong email or password")


def SignUp(request: HttpRequest):
    try:
        if(request.method == "POST"):
            submitData = request.POST
            avatar = request.FILES['avatar']
            userId = User.objects.latest('id').id+1
            fs = FileSystemStorage(location="uploads/")
            filename = fs.save(avatar.name, avatar)
            file_url = fs.url(filename)
            user = User(
                id=userId,
                username=submitData["name"],
                is_superuser=False,
                is_staff=False,
                email=submitData["email"],
                date_joined=datetime.datetime.now(),
                password=make_password(submitData["password"])
            )
            userInfo = UserInfo(
                phone=submitData["phone"],
                user=user,
                birthday=submitData["birthday"],
                avatar=file_url
            )
            user.save()
            userInfo.save()
            return JsonResponse({"message": "ok", "status": 200})
        else:
            return HttpResponseBadRequest("Something wrong")
    except IntegrityError as e:
        errorMessage = ''
        print(str(e))
        if "email" in str(e):
            errorMessage = 'Email exist'
        return HttpResponseBadRequest(json.dumps({
            "error": errorMessage
        }))


def Signout(request: HttpRequest):
    if(request.user.id is not None and request.method == "POST"):
        logout(request)
        return HttpResponseRedirect("/home")
    else:
        return HttpResponseNotFound("Session")
