from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from apps.blog.forms import CommentForm
from apps.blog.models import Article, Comment


def blog_view(request):
    blogs = Article.objects.order_by('-id')
    category = request.GET.get('cat')
    tag = request.GET.get('tag')
    q = request.GET.get('q')
    if q:
        q = Q(title__icontains=q)
        blogs = blogs.filter(q).order_by('-id')
    if category:
        blogs = blogs.filter(category__title__exact=category)
    if tag:
        blogs = blogs.filter(tags__name__exact=tag)
    paginator = Paginator(blogs, 5)
    ctx = {
        'blogs': blogs,
    }
    return render(request, 'blog/blog.html', ctx)


def blog_detail(request, slug):
    blog = get_object_or_404(Article, slug=slug)
    cid = request.GET.get('cid')
    top_blogs = Article.objects.order_by('-id')[:3]
    tag = request.GET.get('tag')
    category = request.GET.get('cat')
    comments = Comment.objects.filter(blog_id=blog.id, top_level_comment_id__isnull=True)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.parent_id = cid
            comment.save()
            messages.success(request, 'Your comment has been added.')
            return redirect('.#comment-form-replay')
    ctx = {
        'blog': blog,
        'top_blogs': top_blogs,
        'tag': tag,
        'category': category,
        'comments': comments,
        'form': form,
    }
    return render(request, 'blog/single.html', ctx)


