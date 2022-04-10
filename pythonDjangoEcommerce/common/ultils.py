from .constants import permissions


def renderWithPermission(request, per, successRender, failedRender):
    userPermission = permissions
    requiredPermissionValue = permissions[per]
    maxPermissionValue = permissions["guest"]
    if(request.user.is_staff is not True and "is_staff" in userPermission):
        del userPermission['is_staff']
    if(request.user.is_superuser is not True and "is_superuser" in userPermission):
        del userPermission['is_superuser']

    for key in userPermission:
        if(userPermission[key] > maxPermissionValue):
            maxPermissionValue = userPermission[key]

    return successRender if maxPermissionValue >= requiredPermissionValue else failedRender
