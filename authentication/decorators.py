from functools import wraps
from django.contrib import messages
from django.shortcuts import redirect
 
def check_permission(perm_codename):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.has_perm(perm_codename):
                return view_func(request, *args, **kwargs)
            else:
                messages.error(request, "You do not have permission to access. Please contact the administrator.")
                return redirect('unauthorized')  # Customize the route as needed
        return _wrapped_view
    return decorator
 