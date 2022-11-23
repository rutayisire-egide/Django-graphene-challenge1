from django.db import models

# Create your models here.

class UserModel(models.Model):

    name = models.CharField(null=False,blank=False,max_length=50)
    email = models.CharField(null=False,blank=False,max_length=50,unique=True)
    phone = models.CharField(null=False,blank=False,max_length=50)
 
    def __str__(self):
        return self.name
