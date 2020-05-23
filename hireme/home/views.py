import json

from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render
from random import randrange

from django.views.decorators.csrf import csrf_exempt

bg_colors = ('bg-primary', 'bg-warning', 'bg-info', 'bg-danger', 'bg-success', 'bg-dark')

# Create your views here.
from candidate.models import CandidateBasicInfo, CandidateResume


def home_new(request):
    return render(request, 'home.html')


def home(request):
    context = {}
    context['all_roles'] = json.dumps((CandidateBasicInfo.get_all_roles()[0]))
    # context['recent_candidates'] = CandidateBasicInfo.objects.order_by('-id')[:3]
    return render(request, 'homenew.html', context)

@csrf_exempt
def LoadRecentCandidates(request):
    context = {}
    last_index = None
    all_candidates = CandidateBasicInfo.objects.select_related('resume').order_by('-id')[:10].values()
    for cand in all_candidates:
        if randrange(0, len(bg_colors)) != last_index:
            last_index = randrange(0, len(bg_colors))
            cand['color'] = bg_colors[last_index]
            cand['resume_url'] = get_resume_url(cand['resume_id'])
        else:
            cand['color'] = bg_colors[randrange(0, len(bg_colors))]

    context['recent_candidates'] = list(all_candidates)
    print(context['recent_candidates'])
    return JsonResponse(context)


def get_resume_url(resume_id):
    resume_url = CandidateResume.objects.get(pk=resume_id).resume.url
    resume_url = 'media/' + resume_url.split('media/')[2]
    print("Resume url.... ", resume_url)

    return resume_url