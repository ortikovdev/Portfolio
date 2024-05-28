from django.db import models
from ckeditor.fields import RichTextField
from django.utils.safestring import mark_safe
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save
from django.utils import timezone


class About(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    job_title = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateField()
    about = RichTextField()
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)

    def __str__(self):
        return self.name


class Jobs(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class ContactMe(models.Model):
    address = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    github_url = models.URLField(max_length=255, blank=True, null=True)
    linkedin_url = models.URLField(max_length=255, blank=True, null=True)
    instagram_url = models.URLField(max_length=255, blank=True, null=True)
    telegram_url = models.URLField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = 'Contact Me'


class YourContact(models.Model):
    your_name = models.CharField(max_length=255)
    your_email = models.EmailField(max_length=255, blank=True, null=True)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.your_name