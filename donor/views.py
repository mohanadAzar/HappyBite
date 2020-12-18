from django.shortcuts import redirect, render
from .forms import DonorSignupForm , DonorUserForm , DonorProfileForm
from django.contrib.auth import authenticate, login
from .models import Donor
from django.urls import reverse
# Create your views here.


def DonorSignup(request):
    if request.method=="POST":
        form = DonorSignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('/donor/profile')
    else:
        form = DonorSignupForm()
    return render(request,'registration/DonorSignup.html',{'form':form})




def DonorProfileView(request):
    DonorProfile = Donor.objects.get(Donor_user=request.user)
    return render(request,'registration/profile.html',{'profile': DonorProfile})




def DonorProfileEdit(request):
    DonorProfile = Donor.objects.get(Donor_user=request.user)

    if request.method=='POST':
        userform = DonorUserForm(request.POST,instance=request.user)
        profileform = DonorProfileForm(request.POST,request.FILES,instance=profile )
        if DonorUserForm.is_valid() and DonorProfileForm.is_valid():
            DonorUserForm.save()
            myprofile = DonorProfileForm.save(commit=False)
            myprofile.user = request.user
            myprofile.save()
            return redirect(reverse('registration:profile'))

    else :
        userform = DonorUserForm(instance=request.user)
        profileform = DonorProfileForm(instance=DonorProfile)

    return render(request,'registration/profile_edit.html',{'userform':DonorUserForm , 'profileform':DonorProfileForm})
