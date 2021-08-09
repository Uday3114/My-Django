
from .models import AirTicketModel
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class Air_Ticket(forms.ModelForm):
    class Meta:
        model = AirTicketModel
        fields = '__all__'



class SignupForm(UserCreationForm):
    password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {'email':'Email'}