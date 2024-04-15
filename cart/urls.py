from django.urls import path
from . import views

app_name='cart'
urlpatterns = [
    path('', views.cart , name='cart'),
    path('addtocart/', views.add_to_cart, name='add_to_cart'),
    path('deleteformcart/', views.delete_form_cart, name='delete_form_cart'),
    path('addcount/', views.add_count, name='add_count'),
    path('minuscount/', views.minus_count, name='minus_count'),
    path('pay/', views.send_request, name='pay'),
    path('verify/', views.verify , name='verify'),
]


