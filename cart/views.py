from django.shortcuts import render
from django.http import JsonResponse
import json
from django.contrib.auth.decorators import login_required
from .models import Cart, CartDetail
from product.models import Product

# Create your views here.
def cart(request):
    user_cart = Cart.objects.filter(user=request.user, is_paid=False).first()
    user_cart_details = user_cart.cartdetail_set.all()


    return render(request, 'cart/cart.html',{'user_cart_details':user_cart_details})


# @login_required(login_url="/account/login/")
def add_to_cart(request):
    data = json.loads(request.body.decode('utf-8'))
    if request.method == 'POST':
        product = Product.objects.filter(id=data.get('productid'), is_active=True, is_delete=False).first()
        if product:
            current_cart, created = Cart.objects.get_or_create(user=request.user, is_paid=False)
            current_cart_detail = current_cart.cartdetail_set.filter(product=product).first()
            if current_cart_detail is not None:
                current_cart_detail.count += 1
                current_cart_detail.save()
            else:
                new_detail = CartDetail(cart=current_cart, product=product, count=1)
                new_detail.save()
        return JsonResponse({'data':'success'})

def delete_form_cart(request):
    data = json.loads(request.body.decode('utf-8'))
    product_id = data.get('productid')
    user_cart = Cart.objects.filter(user=request.user, is_paid=False).first()
    user_cart_details = user_cart.cartdetail_set.all()
    for item in user_cart_details:
        if item.id == product_id:
            item.delete()
    return JsonResponse({'data':'success'})
