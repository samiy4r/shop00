from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.core.paginator import Paginator

# Create your views here.
def product_detail(request, slug):
    data = Product.objects.get(slug=slug)


    return render(request, 'product/single-product.html',{'product':data})

def home(request):
    products = Product.objects.all().order_by()
    paginator = Paginator(products, 2)
    page_obj = paginator.get_page(request.GET)

    return render(request,'product/home.html',{'page_obj':page_obj, 'paginator':paginator})
