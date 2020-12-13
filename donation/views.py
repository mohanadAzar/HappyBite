from django.shortcuts import render
from .models import Donation
# Create your views here.






def donation_list(request):
    donation_list = Donation.objects.all()

    context ={
        'donations' : donation_list ,
    }
    return render(request ,'donation/donation_list.html' ,context )
