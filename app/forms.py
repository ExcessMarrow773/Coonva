from django import forms
from django.contrib.admin.widgets import AdminSplitDateTime
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "password1", "password2")

class CustomAuthenticationForm(AuthenticationForm):
    pass
