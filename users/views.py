from .models import UserModel
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .decorators import unauthenticated_user, nonAdmin_only


from .forms import UserRegisterForm, UserEditForm
from django.contrib.auth.models import Group, Permission

# from django.contrib.contenttypes.models import ContentType

from crawling_next.authorization import superAdmin_permissions, nonAdmin_permissions


class UserRegisterView(CreateView):
    model = UserModel
    template_name = 'aspect/register.html'
    form_class = UserRegisterForm
    success_url = '/'
    def form_valid(self, form):
        user = form.save()
        userType = form.cleaned_data.get('userType')
        if userType == 'superAdmin':
            perm = Permission.objects.get(codename='super_Admin_permission')
        else:
            perm = Permission.objects.get(codename='non_Admin_permission')
        user.user_permissions.add(perm)
        print("----has superadminpermission: -> ",user.has_perm('users.super_Admin_permission'))  
        print("----has nonAdmin permission: -> ",user.has_perm('users.non_Admin_permission'))        
        return super(UserRegisterView, self).form_valid(form)




@login_required
def superAdminView(request):
    return render(request, 'aspect/super_admin_dashboard.html')

class UserDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'aspect/dashboard.html';

class UserProfileView(LoginRequiredMixin, UpdateView):
    model = UserModel
    template_name = 'aspect/profile.html';
    form_class = UserEditForm
    success_url = reverse_lazy('users:dashboard')

class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = UserModel
    success_url = reverse_lazy('users:delete-confirmation')


   



@unauthenticated_user
# @nonAdmin_only
def loginPageView(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('users:dashboard')
		else:
			messages.info(request, 'Username OR password is incorrect')

	return render(request, 'aspect/login.html')








# @login_required
# def userdashboardView(request):
#     return render(request, 'aspect/dashboard.html')

# @login_required
# def userProfileView(request):
#     if request.method == 'POST':
#         user_form = UserEditForm(instance=request.user, data=request.POST)
#         if user_form.is_valid():
#             user_form.save()
#             return redirect('users:dashboard')
#     else:
#         user_form = UserEditForm(instance=request.user)
#     context = {'user_form': user_form}
#     return render(request, 'aspect/profile.html', context)

# @login_required
# def userDeleteView(request):
#     user = UserModel.objects.get(user_name=request.user)
#     user.is_active = False
#     user.delete()
#     return redirect('users:delete-confirmation')



    # def get_object(self):
    #     id_ = self.kwargs.get('pk')
    #     return get_object_or_404(UserModel, id=id_,)
    
    # success_message = "User Data updated successfully"

    # permet de retourner a l'URL pointant vers le membre modifie
   
    # def get(self, request, **kwargs):
    #     self.object = UserModel.objects.get(username=self.request.user)
    #     form_class = self.get_form_class()
    #     form = self.get_form(form_class)
    #     context = self.get_context_data(object=self.object, form=form)
    #     return self.render_to_response(context)

    # def get_object(self, queryset=None):
    #     return self.request.user



# from django.http import  HttpResponseRedirect

# def UserRegisterView(request):
#     if request.method == "POST":
#         print("---------------post request received")
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             Testemail = form.cleaned_data['email']
#             user.email = Testemail
#             print("userEmail---------->", Testemail)
#             user.set_password(form.cleaned_data['password1'])
#             user.save()
#             return redirect('users:login')
#     else:
#         form = UserRegisterForm()
#     context = {'form': form, }
#     return render(request, 'aspect/register.html', context)

# class UserRegisterView(CreateView):
#     model = UserModel
#     template_name = 'aspect/register.html'
#     form_class = UserRegisterForm
#     success_url = '/'
    # def form_valid(self, form):
    #     print('************', form)
    #     print('**********instanceof Form:  ---**', form.instance)

    #     form.save()
    #     return super(UserRegisterView, self).form_valid(form)


# def UserRegisterView(request):
#     if request.method == "POST":
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             print('form is validated')
#             userType = request.POST.get('user_type', 'off')
#             user = form.save()
#             # if usertype is on make superadmin  
#             if userType == 'on':
#                 perm = Permission.objects.get(codename='super_Admin_permission')
#             else:
#                 perm = Permission.objects.get(codename='non_Admin_permission')

#             user.user_permissions.add(perm)

#             content_type = ContentType.objects.get_for_model(UserModel) 
#             user_permissions = Permission.objects.filter(content_type = content_type)
#             print('********_Permission on Model_*********')
#             print([p.codename for p in user_permissions])  

#             res1 = user.has_perm('users.view_usermodel')
#             print("----has view permission: -> ",res1)   
#             print("----has superadminpermission: -> ",user.has_perm('users.super_Admin_permission'))  
#             print("----has nonAdmin permission: -> ",user.has_perm('users.non_Admin_permission'))  

#             return redirect('users:login')
#     else:
#         form = UserRegisterForm()

#     context = {'form': form, }
#     return render(request, 'aspect/register.html', context)
