from django.urls import path
from .views import *

urlpatterns = [
    path('registration/', registration_page, name='rp'),
    path('login/', login_page, name='lp'),
]