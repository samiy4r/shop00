from django.urls import path
from . import views

app_name='lightshop'
urlpatterns = [
    path('index/', views.contact, name='contact'),
    path('', views.add, name='add'),
]