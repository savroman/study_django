from .settings import PORTAL_URL

def students_proc(request):
    return {'PORTAL_URL': {{ request.scheme }} :// {{ request.META.HTTP_HOST }} {{ request.path }}}
