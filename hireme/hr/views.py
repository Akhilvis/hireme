import json

from django.http import JsonResponse
from django.shortcuts import render
from fuzzywuzzy import process

# Create your views here.
from candidate.models import CandidateBasicInfo
from django.views.decorators.csrf import csrf_exempt


def home(request):
    context = {}
    context['all_roles'] = json.dumps((CandidateBasicInfo.get_all_roles()[0]))
    context['recent_candidates'] = CandidateBasicInfo.objects.order_by('-id')[:3]

    return render(request, 'employer_home.html', context)


@csrf_exempt
def SearchCandidate(request):
    dict = {}
    data = json.loads(request.body)
    print(5555, request.body)
    keyword = data.get('search_keyword', None)
    modified_keyword = keyword.lower().replace('software', ' ').strip()
    if keyword:
        all_roles, all_role_ids = CandidateBasicInfo.get_all_roles()
        top3_candidates = process.extract(modified_keyword, all_roles)[:3]
        print(77, top3_candidates)
        print("all_roles >>>>   ", all_roles)
        candidates_ids = [all_roles.index(cand[0])+1 for cand in top3_candidates]
        dict['recent_candidates'] = list(
            CandidateBasicInfo.objects.filter(id__in=candidates_ids).values().order_by('-id')[:3])
        print(88, dict['recent_candidates'])

        print(666666666666666666, dict)
    return JsonResponse(dict)


@csrf_exempt
def LoadRecentCandidates(request):
    dict = {}
    dict['recent_candidates'] = list(CandidateBasicInfo.objects.values().order_by('-id')[:3])
    print("4444444444444444444444444", dict)
    return JsonResponse(dict)
