from django.db import models
from django.contrib.auth.models import User
import datetime
import os

class Catagory(models.Model):
    Name=models.CharField(max_length=30)
    Image=models.ImageField(upload_to="Catagory_Image/%d%m%Y",blank=False,null=True)
    Description=models.CharField(max_length=200,default=" " ) 
    Status=models.BooleanField(default=False,help_text="0-show,1-Hidden") 
    Created_at=models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.Name

class Product(models.Model):
    Catagory=models.ForeignKey(Catagory,on_delete=models.CASCADE)
    Name=models.CharField(max_length=30,default=" ",blank=False)
    Seller=models.CharField(max_length=30,default=" ",blank=False)
    Product_Image=models.ImageField(upload_to="Product_Image/%d%m%Y",blank=False,null=True)
    Quantity=models.IntegerField(default=" ")
    Original_price=models.FloatField(default=" ")
    Selling_price=models.FloatField(default=" ")
    Description=models.CharField(max_length=200,default=" " )
    Status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
    Trending=models.BooleanField(default=False,help_text="0-default,1-Trending") 
    created_at=models.DateField(auto_now=True)

    def __str__(self):
        return self.Name
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Product=models.ForeignKey(Product,on_delete=models.CASCADE)
    Product_qty=models.IntegerField(null=False,blank=False)
    created_at=models.DateField(auto_now=True)

    @property
    def total_cost(self):
        return self.Product_qty*self.Product.Selling_price

class Favourite(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Product=models.ForeignKey(Product,on_delete=models.CASCADE)
    created_at=models.DateField(auto_now=True)
