from django.db import models
from account.models import User
from product.models import Product
# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)
    payment_date = models.DateTimeField(null=True, blank=True)

    # def __str__(self) -> str:
    #       return self.user.email
    
class CartDetail(models.Model):
        product = models.ForeignKey(Product, on_delete=models.CASCADE)
        final_price = models.IntegerField(null=True, blank=True)
        count = models.IntegerField()
        cart = models.ForeignKey(Cart, on_delete=models.CASCADE)