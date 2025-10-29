from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            'first_name', 'last_name', 'email',
            'role', 'school', 'gender', 'marital_status',
            'password1', 'password2'
        ]


class EmailAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label="Email", max_length=254)

    class Meta:
        model = CustomUser
        fields = ['email', 'password']