from django.contrib import admin
from .models import Skill, Job, JobSkill

admin.site.register(Skill)
admin.site.register(Job)
admin.site.register(JobSkill)
