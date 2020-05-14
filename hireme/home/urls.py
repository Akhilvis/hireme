
from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('home', home_new, name='home-page'),
    path('load_recent_candidates', LoadRecentCandidates, name='load-recent-candidates'),
    path('', home, name='home-page'),
]
