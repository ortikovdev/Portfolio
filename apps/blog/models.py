from django.db import models
from ckeditor.fields import RichTextField
from django.utils.safestring import mark_safe
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save
from django.utils import timezone
from pip._vendor.rich.markup import Tag


class Tag(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField()
    image = models.ImageField(upload_to='static/')
    slug = models.SlugField(editable=False, null=True, blank=True)
    is_quote = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    categories = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)
    top_level_comment_id = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='static/', null=True, blank=True)
    message = models.TextField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def children(self):
        if not self.parent:
            return self.Comment.objects.filter(top_level_comment_id=self.id)
        return None
    #
    # def get_image(self):
    #     if self.image:
    #         return mark_safe(f"<a href="{self.image.url} target="_blank"><img src="{self.image.url} width=50 height=50"/></a>")
    #     return "-"


    def blog_pre_save(sender, instance, *args, **kwargs):
        if not instance.slug:
            instance.slug = slugify(instance.title + "-" + timezone.now().strftime("%Y%m%d"))

    pre_save.connect(blog_pre_save, sender=Blog)

    def comment_pre_save(sender, instance, *args, **kwargs):
        if instance.parent:
            if instance.parent.top_level_comment_id:
                instance.top_level_comment_id = instance.parent.top_level_comment_id
            else:
                instance.top_level_comment_id = instance.parent.top_level_comment_id

    # pre_save.connect(comment_pre_save, sender=Comment)
