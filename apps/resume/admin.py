from django.contrib import admin
from .models import (
    Skill,
    Education,
    Experience,
    Award,
    Services,
    Projects,
    Numbers,
)

admin.site.register(Skill)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Award)
admin.site.register(Services)
admin.site.register(Projects)
admin.site.register(Numbers)