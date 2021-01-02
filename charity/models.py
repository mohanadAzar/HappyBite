from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from donation.models import Donation
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



# Create your models here.
class Charity(models.Model):
    Charity_user = models.OneToOneField(User, on_delete=models.CASCADE)
    Charity_Slug = models.SlugField(blank=True, null=True)
    Charity_Phone_Number = PhoneNumberField(blank=True, null=True)
    #Charity_Location
    #Charity_license img
    Charity_Donations_list = models.ForeignKey( Donation , on_delete=models.CASCADE , blank=True, null=True)
    

    

    def save(self, *args, **kwargs): 
      if not self.Charity_Slug:
          self.Charity_Slug = slugify(self.Charity_user) 
      super(Charity , self).save(*args , **kwargs)



    def __str__(self):
        return str(self.Charity_user)



    # @receiver(post_save, sender=User)
    # def create_Charity_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Charity.objects.create(Charity_user=instance)

# beneficarie class model 

class Beneficiary  (models.Model):
    charity = models.ForeignKey(Charity,  on_delete=models.CASCADE , blank=True, null=True)
    Name = models.CharField( max_length=50)
    Address = models.CharField( max_length=50)
    Phone_Number = PhoneNumberField(blank = True)
    Social_Status = models.CharField( max_length=50)
    Family_Members_Number = models.IntegerField(default=1)
    
    def __str__(self):
        return self.Name
    
    


    
