from database.models import UserInfo
from .constants import permissions
import string
import random


def renderWithPermission(request, per, successRender, failedRender):
    userPermission = permissions
    requiredPermissionValue = permissions[per]
    maxPermissionValue = permissions["guest"]
    if("is_staff" in userPermission and request.user.is_staff is not True):
        del userPermission['is_staff']
    if("is_superuser" in userPermission and request.user.is_superuser is not True):
        del userPermission['is_superuser']

    for key in userPermission:
        if(userPermission[key] > maxPermissionValue):
            maxPermissionValue = userPermission[key]

    return successRender if maxPermissionValue >= requiredPermissionValue else failedRender


def getUserInfo(request):
    return UserInfo.objects.all().filter(user_id=request.user.id)


def generateRandomString(length):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))
