from django.contrib import admin
from .models import Resume, EducationHistory, Job, Skill
# Register your models here.


admin.site.register(Resume)
admin.site.register(EducationHistory)
admin.site.register(Job)
admin.site.register(Skill)
