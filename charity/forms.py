from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Charity



class CharitySignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class CharityUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields= ['username','first_name','last_name','email'] 


class CharityProfileForm(forms.ModelForm):
    class Meta:
        model = Charity
        fields = ['Charity_Phone_Number','Charity_Donations_list']



class mydonations(forms.ModelForm):
    class Meta:
        model = Charity
        fields = ['Charity_Donations_list']