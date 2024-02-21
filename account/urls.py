from django.urls import path
from . import views


app_name='account'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_page, name='login'),
    path('activate-account/<str:activate_code>', views.activateAccount)
]