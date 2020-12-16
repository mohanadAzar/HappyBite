from django.db import models
from charity.models import Charity
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Beneficiary  (models.Model):
    Charity = models.ForeignKey(Charity, related_name='job_owner', on_delete=models.CASCADE , blank=True, null=True)
    Name = models.CharField( max_length=50)
    Address = models.CharField( max_length=50)
    Phone_Number = PhoneNumberField()
    Social_Status = models.CharField( max_length=50)
    Family_Members_Number = models.IntegerField(default=1)




