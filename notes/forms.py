from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    admin_key = forms.CharField(required=False, help_text="Leave blank unless you're an admin.")

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "admin_key")
