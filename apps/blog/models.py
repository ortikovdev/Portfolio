from django.db import models
from ckeditor.fields import RichTextField
from django.utils.safestring import mark_safe
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save
from django.utils import timezone


class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='static/')
    slug = models.SlugField(editable=False, null=True, blank=True)
    is_quote = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class SubArticle(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='subarticles')
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='static/')
    upper_text = RichTextField()
    bottom_text = RichTextField()


class Comment(models.Model):
    blog = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name='parents')
    top_level_comment_id = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='article/comments', null=True, blank=True)
    message = models.TextField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def children(self):
        if not self.parent:
            return Comment.objects.filter(top_level_comment_id=self.id)
        return None

    # def get_image(self):
    #     if self.image:
    #         return mark_safe(f"<a href={self.image.url} target='_blank'><img src={self.image.url} width=50 height=50"/></a>")
    #     return "-"


def article_pre_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title + "-" + str(timezone.now().strftime("%Y%m%d-%H")))


# pre_save.connect(article_pre_save, sender=Article)


def comment_pre_save(sender, instance, *args, **kwargs):
    if instance.parent:
        if instance.parent.top_level_comment_id:
            instance.top_level_comment_id = instance.parent.top_level_comment_id
        else:
            instance.top_level_comment_id = instance.parent.id


pre_save.connect(comment_pre_save, sender=Comment)
