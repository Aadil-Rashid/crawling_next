from django.contrib.auth import REDIRECT_FIELD_NAME
from django.http import HttpResponse
from django.shortcuts import redirect

message = '<h3 style="color: red;"> You are not allowed to view this page, as this page is only for Non-admin users </h3>'

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('users:dashboard')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func

# This will be only for my non-admin users
def nonAdmin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == "Non-admin":
            return view_func(request, *args, **kwargs)

        if group == "Super-admin":
            return redirect('users:superAdminDashboard')
    return wrapper_func
  


# # this will be for my Non-admin users:

# def allowed_users(allowed_roles=[]):
#     def decorator(view_func):
#         def wrapper_func(request, *args, **kwargs):
#             group = None
#             if request.user.groups.exists():
#                 group = request.user.groups.all()[0].name
#             if group in allowed_roles:
#                 return view_func(request, *args, **kwargs)
#             else:
#                 return HttpResponse(message)
#         return wrapper_func
#     return decorator

