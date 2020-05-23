import json
from random import randrange

from django.http import JsonResponse
from django.shortcuts import render
from fuzzywuzzy import process

# Create your views here.
from candidate.models import CandidateBasicInfo
from django.views.decorators.csrf import csrf_exempt

from home.views import bg_colors, get_resume_url


def home(request):
    context = {}
    context['all_roles'] = json.dumps((CandidateBasicInfo.get_all_roles()[0]))
    context['recent_candidates'] = CandidateBasicInfo.objects.order_by('-id')[:6]
    return render(request, 'employer_home.html', context)


@csrf_exempt
def SearchCandidate(request):
    dict = {}
    data = json.loads(request.body)
    keyword = data.get('search_keyword', None)
    modified_keyword = keyword.lower().replace('software', ' ').strip()
    if keyword:
        all_roles, all_role_ids = CandidateBasicInfo.get_all_roles()
        top3_candidates = process.extract(modified_keyword, all_roles)[:3]
        print('top3_candidates....   ', top3_candidates)
        candidates_ids = [all_roles.index(cand[0])+1 for cand in top3_candidates]
        all_candidates = CandidateBasicInfo.objects.filter(id__in=candidates_ids).order_by('-id')[:3].values()

        last_index = None
        for cand in all_candidates:
            if randrange(0, len(bg_colors)) != last_index:
                last_index = randrange(0, len(bg_colors))
                cand['color'] = bg_colors[last_index]
                cand['resume_url'] = get_resume_url(cand['resume_id'])
            else:
                cand['color'] = bg_colors[randrange(0, len(bg_colors))]


        dict['recent_candidates'] = list(all_candidates)
    return JsonResponse(dict)
