from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from .forms import (PwdResetConfirmForm, PwdResetForm, UserLoginForm)
from .import views

app_name = 'users'

urlpatterns = [
     path('register/', views.UserRegisterView.as_view(), name='register'),

     # User DashBoard
     # path('dashboard/', views.userdashboardView, name='dashboard'),
     path('dashboard/', views.UserDashboardView.as_view(), name='dashboard'),


     path('profile/<int:pk>/', views.UserProfileView.as_view(), name='profile'),
     path('profile/delete_user/<int:pk>', views.UserDeleteView.as_view(), name='delete-user'),
     path('profile/delete_confirm/', TemplateView.as_view(
          template_name="aspect/delete_confirm.html"), name='delete-confirmation'),


     path('', auth_views.LoginView.as_view(
          template_name='aspect/login.html', form_class=UserLoginForm), name='login'),
     path('logout/', auth_views.LogoutView.as_view(template_name='aspect/logout.html',), name='logout'),



     path('password_reset/',
          auth_views.PasswordResetView.as_view(
               template_name="password_reset/reset_form.html",
               success_url='password_reset_done',
               email_template_name='password_reset/reset_email.html',
               form_class=PwdResetForm),
          name='pwdreset'),

     path('password_reset/password_reset_done/',
          TemplateView.as_view(
               template_name="password_reset/reset_status.html"),
          name='password_reset_done'),

     path('password_reset_confirm/<uidb64>/<token>',
          auth_views.PasswordResetConfirmView.as_view(
               template_name='password_reset/reset_confirm.html',
               success_url='password_reset_complete/',
               form_class=PwdResetConfirmForm),
          name="password_reset_confirm"),

     path('password_reset_confirm/Mg/password_reset_complete/',
          TemplateView.as_view(
               template_name="password_reset/reset_complete.html"),
          name='password_reset_complete'),
]
 