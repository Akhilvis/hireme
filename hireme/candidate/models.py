from django.db import models


# Create your models here.
class CandidateResume(models.Model):
    resume = models.FileField(upload_to='media/resume')

class CandidateBasicInfo(models.Model):
    name = models.CharField(max_length=200)
    mobile = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    role = models.CharField(max_length=100, default='Software Engineer')
    total_experience = models.IntegerField(default=0)
    resume = models.ForeignKey(CandidateResume, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return '{0} - resume > {1}'.format(self.email, self.resume.id)
