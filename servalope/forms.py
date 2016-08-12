from django.forms import Form, ModelForm
from django import forms
from servalope.models import *

class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'first_name',
            'last_name',
            'email'
        ]
