from django.urls import path
from authentication.views import login, logout, register 

app_name = 'authentication'

urlpatterns = [
    path('logout/', logout, name='logout'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
]