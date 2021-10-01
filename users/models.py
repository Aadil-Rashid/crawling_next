from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
# from django.core.mail import send_mail

class CustomAccountManager(BaseUserManager):
    """Define a model manager for User model with no usernammodel_detaile field."""

    def create_user(self, email, user_name, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError(_('You must provide an email address'))

        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, **extra_fields)
        user.set_password(password)
        user.save()
        return user


    def create_superuser(self, email, user_name, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, user_name, password, **extra_fields)
   

class UserModel(AbstractBaseUser, PermissionsMixin):
    
    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    middle_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)

    # User information
    about = models.TextField(_('about'), max_length=500, blank=True)
    mobile_number = models.CharField(max_length=15, blank=True)
   

    # User Status
    is_active =  models.BooleanField(default=True)
    is_staff  =  models.BooleanField(default=False)
    created   =  models.BooleanField(default=False)
    updated   =  models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name']

    class Meta:
        verbose_name = "Users"
        verbose_name_plural = "Users"

    # def get_absolute_url(self):
    #     return reverse("users:profile", kwargs={"id": self.id})
    

    def __str__(self):
        return self.user_name

    

    
