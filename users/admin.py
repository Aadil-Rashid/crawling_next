from django.contrib import admin
from django.contrib.auth import get_user_model


from .models import UserModel 

@admin.register(UserModel)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'email', 'first_name', 'mobile_number', 'is_active',]
    list_filter = ['is_active', 'is_staff', 'is_superuser',]
    ordering = ('created',)