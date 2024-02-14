from django.shortcuts import render
from .models import (
    Skill,
    Education,
    Experience,
    Awards,
    Cervices,
    OurProjects,
)


def resume_page(request):
    skills = Skill.objects.all()
    education = Education.objects.all()
    experience = Experience.objects.all()
    awards = Awards.objects.all()
    cervices = Cervices.objects.all()
    our_projects = OurProjects.objects.all()
    ctx = {
        'skills': skills,
        'education': education,
        'experience': experience,
        'awards': awards,
        'cervices': cervices,
        'our_projects': our_projects,
    }
    return render(request, 'main/index.html', ctx)