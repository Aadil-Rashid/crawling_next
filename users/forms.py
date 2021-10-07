from django import forms
from django.contrib.auth import get_user_model

from django.contrib.auth.forms import (AuthenticationForm, PasswordResetForm, SetPasswordForm)


from .models import UserModel 

from django.contrib.auth.forms import UserCreationForm


USER_TYPE = (
    ("superAdmin", "Super Admin"),
    ("nonAdmin", "Non Admin"),
)

class UserRegisterForm(UserCreationForm):
    user_name = forms.CharField(label="Enter Username", min_length=4, max_length=50, )
    email = forms.EmailField(label="Enter email", max_length=150, error_messages={'required':'Sorry, you will need an email for registration purpose'})
    userType = forms.ChoiceField(choices=USER_TYPE, widget=forms.RadioSelect)
    # class meta gives us nested name space for configurations and keeps the configurations in one place
    class Meta:
        model = get_user_model()
        fields = ("userType", "user_name", "email", "password1", 'password2')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_name'].widget.attrs.update(
            {'placeholder': 'Enter Username'}
        )
        self.fields['email'].widget.attrs.update(
            { 'placeholder': 'Enter Email Id'}
        )
        self.fields['password1'].widget.attrs.update(
            {'placeholder': 'Password'}
        )
        self.fields['password2'].widget.attrs.update(
            {'placeholder': 'Retype Password'}
        )
       


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'mb-2 mt-2',
            'placeholder': 'abc@def.com', 
            'id':'login-user'
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class':'mb-5 mt-1',
            'placeholder': 'Password',
            'id': 'login-pwd',
        }
    ))


# User edit form
class UserEditForm(forms.ModelForm):

    email = forms.EmailField(
        label='Account Email (can not be changed)', max_length=200, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'email', 'id': 'form-email', 'readonly': 'readonly'}))

    user_name = forms.CharField(
        label='Account Username (can not be changed)', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Username', 'id': 'form-firstname', 'readonly': 'readonly'}))

    first_name = forms.CharField(
        label='First Name',  widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Firstname', 'id': 'form-firstname'}))
    
    middle_name = forms.CharField(
        label='Middle Name',  widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Middlename', 'id': 'form-middlename'}))

    last_name = forms.CharField(
        label='Last Name', widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Lastname', 'id': 'form-lastname'}))

    about = forms.CharField(
        label='About', min_length=5, widget=forms.Textarea(
            attrs={'class': 'form-control mb-3', 'placeholder': 'about', 'id': 'form-about'}))

    mobile_number = forms.CharField(
        label='Mobile Number', max_length=15, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Mobile Number', 'id': 'form-mobilenumber'}))

    class Meta:
        model = UserModel
        fields = ('email', 'user_name', 'first_name', 'middle_name', 'last_name', 'mobile_number', 'about')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_name'].required = True
        self.fields['email'].required = True



# Password Reset form
class PwdResetForm(PasswordResetForm):
    email = forms.EmailField(max_length=254, widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Email', 'id': 'form-email'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        user = UserModel.objects.filter(email=email)
        if not user:
            raise forms.ValidationError(
                'Unfortunatley we can not find your account, Please Register new one')
        return email


class PwdResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label='New password', widget=forms.PasswordInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'New Password', 'id': 'form-newpass'}))
    new_password2 = forms.CharField(
        label='Repeat password', widget=forms.PasswordInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'New Password', 'id': 'form-new-pass2'}))

