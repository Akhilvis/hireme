
from django.contrib import admin
from django.urls import path, include
from .views import *



urlpatterns = [
    path('search_candidate', home, name='home-page'),
    path('search_with_keyword', SearchCandidate, name='search-with-keyword'),
]
