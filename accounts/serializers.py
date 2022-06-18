from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from rest_framework import serializers


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']


class LoginUserForm(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
