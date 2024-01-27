from django.db import models

# Create your models here.



class ProductCategory(models.Model):
    title = models.CharField(max_length=64)
    def __str__(self):
        return self.title 

class Product(models.Model):
    title = models.CharField(max_length=300)
    price = models.IntegerField()
    slug = models.SlugField()
    category = models.ManyToManyField(ProductCategory)
    is_active = models.BooleanField()
    is_delete = models.BooleanField(default= False)
    short_description =models.CharField(max_length=260)
    description = models.TextField(help_text="descibe the product here")


    def __str__(self):
        return self.title 
    

