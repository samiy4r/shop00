from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here.
def product_detail(request, slug):
    data = Product.objects.get(slug=slug)
    return render(request, 'product/product_detail.html',{'product':data})