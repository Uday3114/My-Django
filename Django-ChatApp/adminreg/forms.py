from django import forms
from .models import ChatReg
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from chat.models import UserProfile

class AdminChat(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'

class SignupForm(UserCreationForm):
    password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {'email':'Email'}