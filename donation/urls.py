from django.urls import include, path
from . import views


app_name='donation'

urlpatterns = [
    
    path('',views.donation_list , name='donation_list'),



]
