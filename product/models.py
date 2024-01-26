from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=300)
    price = models.IntegerField()
    slug = models.SlugField()

    def __str__(self):
        return self.title