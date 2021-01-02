from django.contrib import admin

# Register your models here.
from .models import Charity , Beneficiary



admin.site.register(Charity)
admin.site.register(Beneficiary)