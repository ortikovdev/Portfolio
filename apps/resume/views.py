from django.shortcuts import render, redirect

from .models import (
    Skill,
    Education,
    Experience,
    Award,
    Services,
    Projects,
    Numbers,
)


def resume_page(request):
    skills = Skill.objects.all()
    education = Education.objects.all()
    experience = Experience.objects.all()
    awards = Award.objects.all()
    cervices = Services.objects.all()
    our_projects = Projects.objects.all()
    numbers = Numbers.objects.all()
    ctx = {
        'skills': skills,
        'education': education,
        'experience': experience,
        'awards': awards,
        'cervices': cervices,
        'our_projects': our_projects,
        'numbers': numbers,
    }
    return render(request, 'main/index.html', ctx)