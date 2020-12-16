from django.contrib import admin

# Register your models here.
from .models import Donor , Charity



admin.site.register(Donor)
admin.site.register(Charity)