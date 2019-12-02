from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        #model will interact with the User, when this form validates it creates a new user
        fields = ['username', 'email', 'password1', 'password2']

#completed form that inherits from UserCreationForm that adds the email field

#models form works with a specific database model
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

