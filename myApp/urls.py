from django.urls import path,include
from myApp.views import *



urlpatterns = [
    path('',home,name='home'),

    path('aa/',aa,name='home'),
]