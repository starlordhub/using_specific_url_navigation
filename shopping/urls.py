from django.urls import path
from shopping.views import *
app_name='selecting'

urlpatterns=[

    path('shopping/',shopping, name='shopping'),
]