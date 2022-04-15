from django.http import Http404, HttpRequest, HttpResponseNotFound

from pythonDjangoEcommerce.common.ultils import getUserInfo


def userInfo(get_response):
    def middleware(request: HttpRequest):
        userInfo = getUserInfo(request)
        print(userInfo)
        if(request.user.id is not None and len(userInfo) != 0):
            request.userInfo = userInfo[0] or None
        else:
            request.userInfo = None
        response = get_response(request)
        return response
    return middleware
