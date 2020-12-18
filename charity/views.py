from django.shortcuts import redirect, render
from .forms import CharitySignupForm , CharityUserForm , CharityProfileForm  , mydonations
from django.contrib.auth import authenticate, login
from .models import Charity
from donation.models import Donation
from django.urls import reverse
# Create your views here.


def CharitySignup(request):
    if request.method=="POST":
        form = CharitySignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('charity/profile')
    else:
        form = CharitySignupForm()
    return render(request,'registration/CharitySignup.html',{'form':form})




def CharityProfileView(request):
    CharityProfile = Charity.objects.get(Charity_user=request.user)
    return render(request,'registration/profile.html',{'profile': CharityProfile})




def CharityProfileEdit(request):
    CharityProfile = Charity.objects.get(Charity_user=request.user)

    if request.method=='POST':
        userform = CharityUserForm(request.POST,instance=request.user)
        profileform = CharityProfileForm(request.POST,request.FILES,instance=profile )
        if CharityUserForm.is_valid() and CharityProfileForm.is_valid():
            CharityUserForm.save()
            myprofile = CharityProfileForm.save(commit=False)
            myprofile.user = request.user
            myprofile.save()
            return redirect(reverse('registration:profile'))

    else :
        userform = CharityUserForm(instance=request.user)
        profileform = CharityProfileForm(instance=CharityProfile)

    return render(request,'registration/profile_edit.html',{'userform':CharityUserForm , 'profileform':CharityProfileForm})





def CharityDonationView(request):
    CharityProfile = Charity.objects.get(Charity.Charity_Donations_list == request.Charity.Charity_Donations_list)
    print("$$$$$$$$$$$$$$$$$$$$$$$$$")
    print(CharityProfile)
    return render(request,'mydonations.html',{'mydonations': CharityProfile})




