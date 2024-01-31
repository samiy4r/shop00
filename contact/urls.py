from django.urls import path
from . import views

app_name='lightshop'
urlpatterns = [
    path('', views.contact, name='contact')
]