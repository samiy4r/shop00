from django.db import models

# Create your models here.
class ContactUs(models.Model):
    subject = models.CharField(max_length=300,null=True)
    message = models.TextField(null=True)
    full_name = models.CharField(max_length=200,null=True)
    email = models.EmailField(max_length=300,null=True)
    phone = models.CharField(max_length=13,null=True)
    created = models.DateTimeField(auto_now_add=True)
    read_by_admin = models.BooleanField(default=False,null=True)
    admin_response = models.TextField(null=True, blank=True)
    class Meta():
        verbose_name_plural = 'contact us'