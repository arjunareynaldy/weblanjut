from django.contrib.auth.models import User
from django.shortcuts import render

# Create your models here. 
class Biodata(models.Model):
    user =models.OneToOneField(User, on_delete=models.CASCADE)
    alamat = models.TextField() 
    telp = models.CharField(max_length=14)

    def __str__(self):
        return self.user 