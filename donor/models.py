from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from donation.models import Donation
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Donor(models.Model):
    Donor_user = models.OneToOneField(User, on_delete=models.CASCADE)

    Donor_Slug = models.SlugField(blank=True, null=True)

    Donar_Employmenr_Type = models.CharField( max_length=30)
    Donor_Phone_Number = PhoneNumberField()
    #location 
    Donor_Donations_list = models.ForeignKey( Donation , on_delete=models.CASCADE , blank=True, null=True)


    def save(self, *args, **kwargs): 
      if not self.Donor_Slug:
          self.Donor_Slug = slugify(self.Donor_user) 
      super(Donor , self).save(*args , **kwargs)


    def __str__(self):
        return str(self.Donor_user)



    @receiver(post_save, sender=User)
    def create_Donor_user_profile(sender, instance, created, **kwargs):
        if created:
            Donor.objects.create(Donor_user=instance)