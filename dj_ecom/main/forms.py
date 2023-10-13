from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from .models import Customer

class CustomerRegForm(UserCreationForm):

    username =forms.CharField(widget=forms.TextInput(attrs={'autofocus':'True', 'class':'form-control'}))
    email =forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 =forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 =forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User 
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):

    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':'True', 'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))

class UserUpdateForm(forms.ModelForm):
    # email = forms.EmailField(required=False)
    # first_name = forms.CharField(required=False)
    # last_name = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
        }

class CustomerProfileForm(forms.ModelForm):
    
    class Meta:
        model = Customer
        fields = ['mobile','state','zipcode']
        widgets = {
            'state': forms.TextInput(attrs={'class':'form-control'}),
            'mobile': forms.TextInput(attrs={'class':'form-control'}),
            'zipcode': forms.TextInput(attrs={'class':'form-control'}),
        }

