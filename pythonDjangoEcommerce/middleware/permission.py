from django.http import Http404, HttpRequest, HttpResponseNotFound

def permission(get_response):
    def middleware(request: HttpRequest):
        response = get_response(request)
        return response
    return middleware
