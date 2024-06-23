from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from django import forms
from .models import Profile


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={"class":"focus:outline-none", 'placeholder':'mail@test.com'}))
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={"class":"focus:outline-none", 'placeholder':'user'}))
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={"class":"focus:outline-none", 'placeholder':'pass1'}))
    password2 = forms.CharField(required=True , widget=forms.PasswordInput(attrs={"class":"focus:outline-none", 'placeholder':'pass2'}))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'contact_number']