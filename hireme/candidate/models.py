from django.db import models


# Create your models here.

class CandidateBasicInfo(models.Model):
    name = models.CharField(max_length=200)
    mobile = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    resume_id = models.IntegerField()


class CandidateResume(models.Model):
    resume = models.FileField(upload_to='media/resume')
