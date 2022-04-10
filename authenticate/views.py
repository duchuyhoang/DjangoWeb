from django.shortcuts import render
from django.http.request import HttpRequest
from django.http import HttpResponseNotFound, JsonResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
import datetime
from django.core.files.storage import FileSystemStorage
from database.models import UserInfo


def Login(request: HttpRequest):
    if(request.method == "POST"):
        user = authenticate(
            username=request.POST["email"], password=request.POST["password"])
        login(request, user)
        request.session['user'] = "huy"
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
            print(file_url)
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
    except:
        return HttpResponseBadRequest("Something wrong")


def Signout(request: HttpRequest):
    if(request.user.id is not None and request.method == "POST"):
        logout(request)
        return HttpResponseRedirect("/home")
    else:
        return HttpResponseNotFound("Session")
