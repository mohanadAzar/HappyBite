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
    Charity_Name = Charity_user.name# models.CharField( max_length=30)
    Charity_Slug = models.SlugField(blank=True, null=True)
    Charity_Email = models.EmailField( max_length=254)
    Charity_Phone_Number = PhoneNumberField()
    #Charity_Location
    #Charity_license img
    Charity_Donations_list = models.ForeignKey( Donation , on_delete=models.CASCADE , blank=True, null=True)

    

    def save(self, *args, **kwargs): 
      if not self.Charity_Slug:
          self.Charity_Slug = slugify(self.Charity_Name) 
      super(Charity , self).save(*args , **kwargs)



    def __str__(self):
        return self.Charity_Name



    @receiver(post_save, sender=User)
    def create_Charity_user_profile(sender, instance, created, **kwargs):
        if created:
            Charity.objects.create(Charity_user=instance)

    

class Donor(models.Model):
    Donor_user = models.OneToOneField(User, on_delete=models.CASCADE)
    Donor_Name = models.CharField( max_length=30)
    Donor_Slug = models.SlugField(blank=True, null=True)
    Donor_Email = models.EmailField( max_length=254)
    Donar_Employmenr_Type = models.CharField( max_length=30)
    Donor_Phone_Number = PhoneNumberField()
    #location 
    Donor_Donations_list = models.ForeignKey( Donation , on_delete=models.CASCADE , blank=True, null=True)


    def save(self, *args, **kwargs): 
      if not self.Donor_Slug:
          self.Donor_Slug = slugify(self.Donor_Name) 
      super(Donor , self).save(*args , **kwargs)

    def __str__(self):
        return self.Donor_Name



    @receiver(post_save, sender=User)
    def create_Donor_user_profile(sender, instance, created, **kwargs):
        if created:
            Donor.objects.create(Donor_user=instance)