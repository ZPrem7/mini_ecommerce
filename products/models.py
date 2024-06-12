from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()

class Category(models.Model):
    name = models.CharField(max_length=100)
    image=models.ImageField(upload_to="uploads/",null=True,blank=True)
    description=models.TextField(max_length=500,null=False,blank=False)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    categories =models.ForeignKey(Category,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField()
    image = models.ImageField(upload_to='uploads/',null=True,blank=True)
    tags = models.ManyToManyField(Tag)
    

    def __str__(self):
        return self.title

