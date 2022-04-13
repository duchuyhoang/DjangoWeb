from django.http import Http404, HttpRequest, HttpResponseNotFound

from pythonDjangoEcommerce.common.ultils import getUserInfo


def userInfo(get_response):
    def middleware(request: HttpRequest):
        if(request.user.id is not None):
            request.userInfo = getUserInfo(request)[0] or None
        else:
            request.userInfo = None
        response = get_response(request)
        return response
    return middleware
