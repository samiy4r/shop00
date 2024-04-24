from django.urls import path
from . import views


app_name = 'user_panel'


urlpatterns = [
    path('profile-info/',views.profile_info,name='profile_info'),
    path('profile-edit/',views.profile_edit,name='profile_edit'),
    
]
