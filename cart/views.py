from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse, HttpResponse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import Cart, CartDetail
from product.models import Product
from django.utils import timezone
import json
import requests

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

def add_count(request):
    data = json.loads(request.body.decode('utf-8'))
    product_id = data.get("productid")
    cart_valou = CartDetail.objects.filter(id=product_id).first()
    x = cart_valou.count
    x = x +1
    updatet_stat = CartDetail.objects.filter(id=product_id).update(count= x )
    print(x)
    return JsonResponse({"data" : '1' })


def minus_count(request):
    data = json.loads(request.body.decode('utf-8'))
    product_id = data.get("productid")
    cart_valou = CartDetail.objects.filter(id=product_id).first()
    x = cart_valou.count
    x = x  - 1
    updatet_stat = CartDetail.objects.filter(id=product_id).update(count= x )
    print(x)
    return JsonResponse({"data" : '1' })

# ? sandbox merchant
# if settings.SANDBOX:
# sandbox = 'sandbox'
# else:
sandbox = 'www'

ZP_API_REQUEST = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
ZP_API_VERIFY = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
ZP_API_STARTPAY = f"https://{sandbox}.zarinpal.com/pg/StartPay/"

# total_amount = 1000  # Rial / Required
description = "lightshop"  # Required
phone = 'YOUR_PHONE_NUMBER'  # Optional
CallbackURL = 'http://127.0.0.1:8000/cart/verify/'

def send_request(request):
    current_cart, created = Cart.objects.get_or_create(user=request.user, is_paid=False)
    total_amount = current_cart.calculate_total_price() * 63000

    data = {
        "MerchantID": settings.ZP_MERCHANT_ID,
        "Amount": total_amount,
        "Description": description,
        "Phone": phone,
        "CallbackURL": CallbackURL,
    }
    data = json.dumps(data)
    # set content length by data
    headers = {'content-type': 'application/json', 'content-length': str(len(data))}
    try:
        response = requests.post(ZP_API_REQUEST, data=data, headers=headers)

        if response.status_code == 200:
            response = response.json()
            if response['Status'] == 100:
                url = f"{ZP_API_STARTPAY}{response['Authority']}"
                return redirect(url)
                # return {'status': True, 'url': ZP_API_STARTPAY + str(response['Authority']),'authority': response['Authority']}
            else:
                print('failed '*20)
                return HttpResponse(f"{response['Status']}")
        return response

    except requests.exceptions.Timeout:
        return {'status': False, 'code': 'timeout'}
    except requests.exceptions.ConnectionError:
        return {'status': False, 'code': 'connection error'}


@login_required
def verify(request):
    print(request.user)
    authority = request.GET['Authority']
    current_cart, created = Cart.objects.get_or_create(user=request.user, is_paid=False)
    total_amount = current_cart.calculate_total_price() * 63000

    data = {
        "MerchantID": settings.ZP_MERCHANT_ID,
        "Amount": total_amount,
        "Authority": authority,
    }
    data = json.dumps(data)
    # set content length by data
    headers = {'content-type': 'application/json', 'content-length': str(len(data)) }
    response = requests.post(ZP_API_VERIFY, data=data,headers=headers)

    if response.status_code == 200:
        response = response.json()
        if response['Status'] == 100:
            current_cart.is_paid = True
            current_cart.payment_date = timezone.now()
            current_cart.save()
            return HttpResponse(f'payment is succesful')
        else:
            return HttpResponse(f"payment failed")
    return response