from django.db import models
from ckeditor.fields import RichTextField
from django.utils.safestring import mark_safe
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save
from django.utils import timezone


class Skill(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    persentage = models.IntegerField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='main/skills/', blank=True, null=True)

    def __str__(self):
        return self.name


class Education(models.Model):
    studied_at = models.CharField(max_length=255, blank=True, null=True)
    direction = models.CharField(max_length=322, blank=True, null=True)
    starting_date = models.DateField(null=True, blank=True)
    ending_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.studied_at


class Experience(models.Model):
    job_title = models.CharField(max_length=256, blank=True, null=True)
    worked_at = models.CharField(max_length=322, blank=True, null=True)
    starting_date = models.DateField(null=True, blank=True)
    ending_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.job_title


class Awards(models.Model):
    name = models.CharField(max_length=254, blank=True, null=True)
    where_is_it = models.CharField(max_length=322, blank=True, null=True)
    when_was_it = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Cervices(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='main/services/', blank=True, null=True)

    def __str__(self):
        return self.name


class OurProjects(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='main/projects/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    projects_number = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name
