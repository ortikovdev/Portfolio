from django.contrib import admin

from .models import (
    About,
    ContactMe,
)


@admin.register(ContactMe)
class ContactMeAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone_number', 'address',)


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'middle_name', 'job_title', 'date_of_birth', 'resume')
    search_fields = ('name', 'surname', 'middle_name', 'job_title', 'date_of_birth')
    readonly_fields = ('date_of_birth', 'resume')



