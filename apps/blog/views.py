from django.shortcuts import render, get_object_or_404, redirect
from apps.blog.models import Blog


def blog_view(request):
    blogs = Blog.objects.all()
    ctx = {
        'blogs': blogs,
    }
    return render(request, 'blog/blog.html', ctx)


def blog_detail(request, slug):
    detail = get_object_or_404(Blog, slug=slug)
    ctx = {
        'blog': detail
    }
    return render(request, 'blog/single.html', ctx)


