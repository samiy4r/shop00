from django.urls import path
from . import views

app_name='account'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_page, name='login'),
    path('activate-account/<str:activate_code>', views.activateAccount,name='activate_account'),
    path('forget-password/', views.forget_password_email_page, name='forget_password_email'),
    path('forget-password/<str:activate_code>', views.forget_password, name='forget_password'),
    path('logout/', views.logout_page, name='logout')
]