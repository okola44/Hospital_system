from django.db import models

# Create your models here.
class Patient(models.Model):
    name=models.CharField(max_length=10,blank=True,null=True)
    email=models.EmailField(unique=True,blank=True,null=True)
    gender=models.CharField(max_length=20,blank=True,null=True)
    phone_number=models.CharField(max_length=15,blank=True,null=True)
    date_of_birth=models.DateField()
    bloodgroup=models.CharField(max_length=5,blank=True,null=True)
    address=models.CharField(max_length=20,blank=True,null=True)

    def __str__(self):
        return self.name

