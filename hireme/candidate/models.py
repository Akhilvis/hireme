
from django.db import models


# Create your models here.
class CandidateResume(models.Model):
    resume = models.FileField(upload_to='media/resume')


class CandidateBasicInfo(models.Model):
    name = models.CharField(max_length=200)
    mobile = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    role = models.CharField(max_length=100, default='Software Engineer')
    total_experience = models.FloatField(default=0.0)
    summary = models.CharField(max_length=150, null=True)
    resume = models.ForeignKey(CandidateResume, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return '{0} - resume > {1}'.format(self.email, self.resume.id)

    @staticmethod
    def get_all_roles():
        return list(CandidateBasicInfo.objects.values_list('role', flat=True)), list(CandidateBasicInfo.objects.values_list('id', flat=True))
