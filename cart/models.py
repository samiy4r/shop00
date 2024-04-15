from django.db import models
from account.models import User
from product.models import Product
# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)
    payment_date = models.DateTimeField(null=True, blank=True)

    def calculate_total_price(self):
        total_price = 0
        if self.is_paid:
            for cart_detail in self.cartdetail_set.all():
                total_price += cart_detail.final_price * cart_detail.count
        else:
            for cart_detail in self.cartdetail_set.all():
                total_price += cart_detail.product.price * cart_detail.count
        return int(total_price)
    
class CartDetail(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    final_price = models.IntegerField(null=True, blank=True)
    count = models.IntegerField()
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)


    def get_total_price(self):
        return self.product.price * self.count