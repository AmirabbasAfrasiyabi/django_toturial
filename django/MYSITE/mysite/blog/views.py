# views.py
from django.shortcuts import render, get_object_or_404 , redirect
from blog.models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from blog.forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate


def blog_view(request, cat_name=None, author_username=None , tag_name = None,):
    if request.user.is_authenticated:
        posts = Post.objects.filter(status=1)
        if cat_name:
            posts = posts.filter(category__name=cat_name)
        if author_username:
            posts = posts.filter(author__username=author_username)
        if tag_name:
            posts = posts.filter(tags__name__in=[tag_name])
            # posts = posts.filter(tag__name=tag_name)
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
    else:
        return render(request, 'accounts/login.html')


def blog_single(request, pid):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=pid, status=True)
        
        # Increase the view count
        post.counted_views += 1
        post.save()

        # Fetch only active comments
        comments = post.comments.filter(active=True)
        new_comment = None

        if request.method == 'POST':
            comment_form = CommentForm(data=request.POST)
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.post = post
                new_comment.active = True  # Mark the comment as active
                new_comment.save()
                return redirect(post.get_absolute_url())
        else:
            comment_form = CommentForm()

        previous_post = Post.objects.filter(pk__lt=post.pk, status=True).order_by('-pk').first()
        next_post = Post.objects.filter(pk__gt=post.pk, status=True).order_by('pk').first()

        context = {
            'post': post,
            'comments': comments,
            'new_comment': new_comment,
            'comment_form': comment_form,
            'previous_post': previous_post,
            'next_post': next_post
        }
        return render(request, 'blog/blog-single.html', context)
    else:
        return render(request, 'accounts/login.html')

def latest_blog_posts(request):
    posts = Post.objects.filter(status=1).order_by('-published_date')
    context = {'posts': posts}
    return render(request, 'website/index.html', context)


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
