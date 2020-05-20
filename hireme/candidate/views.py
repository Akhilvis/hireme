from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from .models import CandidateResume, CandidateBasicInfo


def AddResume(request):
    return render(request, 'upload_resume.html')


@csrf_exempt
def UploadResume(request):
    resume = request.FILES['file']
    resume_obj = CandidateResume.objects.create(resume=resume)
    request.session['resume_id'] = resume_obj.pk
    return JsonResponse({})


@csrf_exempt
def AddCandidateData(request):
    name = request.POST.get('name', '')
    email = request.POST.get('email', '')
    mobile = request.POST.get('mobile', '')
    role = request.POST.get('role', 'Software Engineer')
    experience = request.POST.get('experience', 0)
    summary = request.POST.get('summary', '')
    resume_id = request.session.get('resume_id', None)
    if resume_id:
        CandidateBasicInfo.objects.create(
            name=name.title(),
            mobile=mobile,
            email=email,
            role=role,
            total_experience=experience,
            summary=summary,
            resume=CandidateResume.objects.get(pk=resume_id)
        )
    else:
        print("Resume not uploaded....")
        return JsonResponse({"status": 0})

    request.session['resume_id'] = None
    return JsonResponse({"status": 1})
