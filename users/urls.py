from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from .forms import (PwdResetConfirmForm, PwdResetForm, UserLoginForm)
from .import views

app_name = 'users'


urlpatterns = [
     path('register/', views.UserRegisterView.as_view(), name='register'),

     path('dashboard/users', views.UserDashboardView.as_view(), name='dashboard'),
     # path('superadmin/', views.superAdminView, name="superAdminDashboard"),


     path('profile/<int:pk>/', views.UserProfileView.as_view(), name='edit'),
     path('profile/delete_user/<int:pk>', views.UserDeleteView.as_view(), name='delete-user'),
     path('profile/delete_confirm/', TemplateView.as_view(
          template_name="users/aspect/delete_confirm.html"), name='delete-confirmation'),


     # path('', views.loginPageView, name='login'),

      path('', auth_views.LoginView.as_view(
          template_name='users/aspect/login.html', form_class=UserLoginForm), name='login'),

     path('logout/', auth_views.LogoutView.as_view(template_name='users/aspect/logout.html',), name='logout'),



     path('password_reset/',
          auth_views.PasswordResetView.as_view(
               template_name="users/password_reset/reset_form.html",
               success_url='password_reset_done',
               email_template_name='users/password_reset/reset_email.html',
               form_class=PwdResetForm),
          name='pwdreset'),

     path('password_reset/password_reset_done/',
          auth_views.PasswordResetDoneView.as_view(
               template_name="users/password_reset/reset_status.html"),
          name='password_reset_done'),

     path('password_reset_confirm/<uidb64>/<token>',
          auth_views.PasswordResetConfirmView.as_view(
               template_name='users/password_reset/reset_confirm.html',
               success_url='password_reset_complete/',
               form_class=PwdResetConfirmForm),
          name="password_reset_confirm"),

     path('password_reset_confirm/MTk/password_reset_complete/',
          auth_views.PasswordResetCompleteView.as_view(
               template_name="users/password_reset/reset_complete.html"),
          name='password_reset_complete'),

     # path('password_reset_confirm/MTc/password_reset_complete/',
     #      TemplateView.as_view(
     #           template_name="password_reset/reset_complete.html"),
     #      name='password_reset_complete'),
]
 




# user.has_perm('users.add_usermodel')

# urlpatterns = [
#      path('password_reset/',
#           auth_views.PasswordResetView.as_view(
#                template_name="password_reset/reset_form.html",
#                success_url='password_reset_done',
#                email_template_name='password_reset/reset_email.html',
#                form_class=PwdResetForm),
#           name='pwdreset'),

#      path('password_reset/password_reset_done/',
#           auth_views.PasswordResetDoneView.as_view(
#                template_name="password_reset/reset_status.html"),
#           name='password_reset_done'),

#      path('password_reset_confirm/<uidb64>/<token>/',
#           auth_views.PasswordResetConfirmView.as_view(
#                template_name='password_reset/reset_confirm.html',
#                success_url='password_reset_complete/',
#                form_class=PwdResetConfirmForm),
#           name="password_reset_confirm"),

#      path('password_reset_complete',
#           auth_views.PasswordResetCompleteView.as_view(
#                template_name="password_reset/reset_complete.html"),
#           name='password_reset_complete'),

# ]
 