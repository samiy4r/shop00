from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=300)
    price = models.IntegerField()
    slug = models.SlugField()
    category = models.ManyToManyField()
    is_active = models.BooleanField()
    is_delete = models.BooleanField(default= False)
    short_description =models.TextField(max_length=260)


    def __str__(self):
        return self.title