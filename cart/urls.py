from django.urls import path
from . import views

app_name='cart'
urlpatterns = [
    path('', views.home , name='contact'),
    path('addtocart', views.add_to_cart, name='add_to_cart')
]


