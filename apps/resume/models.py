from django.db import models
from ckeditor.fields import RichTextField
from django.utils.safestring import mark_safe
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save
from django.utils import timezone


class Education(models.Model):
    school_name = models.CharField(max_length=255)
    years = models.CharField(max_length=10)
    direction = models.CharField(max_length=255)
    description = models.TextField()
    created_date = models.DateField(auto_now_add=True)


class Experience(models.Model):
    company_name = models.CharField(max_length=255)
    years = models.CharField(max_length=10)
    job_name = models.CharField(max_length=255)
    description = models.TextField()
    created_date = models.DateField(auto_now_add=True)


class Award(models.Model):
    award_name = models.CharField(max_length=255)
    years = models.CharField(max_length=10)
    where = models.CharField(max_length=255)
    description = models.TextField()
    created_date = models.DateField(auto_now_add=True)


class Skill(models.Model):
    title = models.CharField(max_length=255)
    percent = models.IntegerField()
    last_week = models.IntegerField()
    last_year = models.IntegerField()
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class Services(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    link = models.URLField(max_length=255)
    icon = models.ImageField(upload_to='icons/')
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Projects(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    image = models.ImageField(upload_to='projects/')
    link = models.URLField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Projects'


class Numbers(models.Model):
    title = models.CharField(max_length=255)
    number = models.IntegerField()
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Numbers'