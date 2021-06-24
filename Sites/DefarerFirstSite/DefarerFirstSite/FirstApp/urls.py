from django.contrib import admin
from django.urls import path

from .views import *


urlpatterns = [
    # path('test/', test_view)
    path('first_page/', first_page),
    path('all_games', all_games_view)
]
