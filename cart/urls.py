from django.urls import path
from . import views

app_name='cart'
urlpatterns = [
    path('', views.cart , name='contact'),
    path('addtocart/', views.add_to_cart, name='add_to_cart'),
    path('deleteformcart/', views.delete_form_cart, name='delete_form_cart')

]


