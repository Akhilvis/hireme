from django.contrib import admin

from .models import CandidateBasicInfo, CandidateResume


class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(CandidateResume, AuthorAdmin)
admin.site.register(CandidateBasicInfo, AuthorAdmin)