from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Donor



class DonorSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class DonorUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields= ['username','first_name','last_name','email'] 


class DonorProfileForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ['Donar_Employmenr_Type','Donor_Phone_Number' , 'Donor_Donations_list']