from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactsForm
from .models import (
    About,
    ContactMe,
)


def about_view(request):
    about = About.objects.all()
    contact_me = ContactMe.objects.all()
    form = ContactsForm()
    if request.method == 'POST':
        form = ContactsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your contact!')
            return redirect('.#contact-form')
    ctx = {
        'about': about,
        'contact_me': contact_me,
    }
    return render(request, 'main/index.html', ctx)


