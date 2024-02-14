from django.http import HttpResponseRedirect
from django.urls import reverse
from functools import wraps

def redirect_if_authenticated(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            # Redirect to home page (or any other page you wish)
            return HttpResponseRedirect(reverse('core:index'))
        else:
            return view_func(request, *args, **kwargs)
    return _wrapped_view