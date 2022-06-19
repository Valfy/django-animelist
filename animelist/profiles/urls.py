from django.urls import path
from .views import *

urlpatterns = [
    path('registration/', registration_page, name='rp'),
    path('login/', login_page, name='lp'),
    path('logout/', user_logout, name='logout'),
    path('change_password/', change_password, name='cpp'),
    path('profile/<int:user_id>/', profile_view, name='profile'),
    path('profiles/', profiles_all, name='profiles_all'),
    path('profile_settings/<int:user_id>/', profile_settings, name='profile_settings')
]