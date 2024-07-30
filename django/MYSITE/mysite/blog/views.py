# views.py
from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def blog_view(request, cat_name=None, author_username=None):
    posts = Post.objects.filter(status=1)
    if cat_name:
        posts = posts.filter(category__name=cat_name)
    if author_username:
        posts = posts.filter(author__username=author_username)
    posts = Paginator(posts, 3)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)


def latest_blog_posts(request):
    posts = Post.objects.filter(status=1).order_by('-published_date')
    context = {'posts': posts}
    return render(request, 'website/index.html', context)

def blog_single(request, pid):
    posts = Post.objects.filter(status=1)
    post = get_object_or_404(posts, pk=pid)

    previous_post = posts.filter(pk__lt=post.pk).order_by('-pk').first()
    next_post = posts.filter(pk__gt=post.pk).order_by('pk').first()

    context = {
        'post': post,
        'previous_post': previous_post,
        'next_post': next_post
    }
    return render(request, 'blog/blog-single.html', context)

def blog_test(request):
    posts = Post.objects.filter(status=1)
    context = {'posts': posts}
    return render(request, 'website/test.html', context)

def blog_category(request, cat_name):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__name=cat_name)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)

def blog_search(request):
    posts = Post.objects.filter(status=1)
    query = request.GET.get('s')
    if query:
        posts = posts.filter(content__contains=query)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)
