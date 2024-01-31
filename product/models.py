from django.db import models
from django.utils.text import slugify
# Create your models here.



class ProductCategory(models.Model):
    title = models.CharField(max_length=64)
    def __str__(self):
        return self.title 

class Product(models.Model):
    title = models.CharField(max_length=300)
    price = models.IntegerField()
    short_description =models.CharField(max_length=260)
    description = models.TextField(help_text="describe the product here")
    slug = models.SlugField()
    category = models.ManyToManyField(ProductCategory)
    is_active = models.BooleanField()
    is_delete = models.BooleanField(default= False)


    def __str__(self):
        return self.title 
    