
from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('add_resume', AddResume, name='add-resume'),
    path('upload_resume', UploadResume, name='add-resume'),
    path('add_candidate_data', AddCandidateData, name='add_cand_data'),
]
