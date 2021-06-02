from django.db import models

#TODO Fix imports


class User(models.Model):
    first_name=models.CharField(max_length=45)
    last_name=models.CharField(max_length=45)
    phone_number=models.CharField(max_length=45)
    password=models.CharField(max_length=45)
    city=models.CharField(max_length=45)
    #orders=
    #cart
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
