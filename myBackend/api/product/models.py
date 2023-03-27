from api.category.models import Category
from django.db import models

class Product(models.Model):
    name= models.CharField(max_length=20)
    description= models.CharField(max_length=150)
    price= models.CharField(max_length=20)
    stock= models.CharField(max_length=20)
    is_active= models.BooleanField(default=True,blank=True)
    # image= models.ImageField(upload_to='images/',blank=True,null=True)
    category= models.ForeignKey(Category,on_delete=models.SET_NULL,blank=True,null=True)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name