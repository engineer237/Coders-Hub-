from dataclasses import fields
from django.forms import ModelForm
from hub.models import Room, User
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User


class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar','name','username', 'email', 'bio']
        # fields = '__all__'