from django.db import models

# Create your models here.

class Charity(models.Model):
    
    
    Name = models.CharField( max_length=50)

    
