from django.urls import path
from .views import *

urlpatterns = [
    path('registration/', registration_page, name='rp'),
    path('login/', login_page, name='lp'),
    path('logout/', user_logout, name='logout'),
    path('profile/<int:user_id>/', profile_view, name='profile'),
    path('profiles/', profiles_all, name='profiles_all')
]