from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from .models import CandidateResume


def AddResume(request):
    return render(request, 'upload_resume.html')


@csrf_exempt
def UploadResume(request):
    print(request.FILES)
    resume = request.FILES['file']
    print(resume)
    resume_obj = CandidateResume.objects.create(resume=resume)
    print(resume_obj.pk)
    return JsonResponse({'resume_id': resume_obj.pk})
