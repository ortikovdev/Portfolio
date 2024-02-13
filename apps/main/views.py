from django.shortcuts import render, redirect
from django.contrib import messages
from .models import (
    About,
    ContactMe,
)


def about_view(request):
    about = About.objects.all()
    contact_me = ContactMe.objects.all()
    ctx={
        'about': about,
        'contact_me': contact_me,
    }

    return render(request, 'main/index.html', ctx)


