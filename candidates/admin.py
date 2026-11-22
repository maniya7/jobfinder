from django.contrib import admin
from .models import Candidate, Resume, Experience, Education, CandidateSkill

admin.site.register(Candidate)
admin.site.register(Resume)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(CandidateSkill)