from django.db import models

# Create your models here.
class ContactUs(models.Model):
    subject = models.CharField(max_length=300)
    full_name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    message = models.TextField()
    created = models.DateField(auto_now_add=True)
    read_by_admin = models.BooleanField(default=False)

    class Meta():
        verbose_name_plural = 'contact us'