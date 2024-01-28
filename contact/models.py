from django.db import models

# Create your models here.
class ContactUs(models.Model):
    subject = models.CharField(max_length=300)
    message = models.TextField()
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=300)
    phone = models.CharField(max_length=13)
    created = models.DateTimeField(auto_now_add=True)
    read_by_admin = models.BooleanField(default=False)
    admin_response = models.TextField(null=True, blank=True)

    class Meta():
        verbose_name_plural = 'contact us'