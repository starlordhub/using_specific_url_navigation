from django.urls import path
from food.views import *
app_name='eating'

urlpatterns=[

    path('food/',food, name='food'),
]